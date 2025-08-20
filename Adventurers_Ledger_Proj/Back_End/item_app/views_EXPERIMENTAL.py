import asyncio
import aiohttp
from django.db import transaction
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as s
from .models import Item, ShopItem
from .serializers import ItemSerializer
from .utils_EXPERIMENTAL import get_dice_average

API_BASE_URL = "https://www.dnd5eapi.co"

class GetItemByNameView(APIView):
    """
    GET /item-by-name/
    Fetches item details by name from the D&D API and returns it in JSON format.
    """

    def get(self, request):
        item_name = request.query_params.get('name')
        if not item_name:
            return Response({"error": "Item name is required."}, status=s.HTTP_400_BAD_REQUEST)

        item_url = f"{API_BASE_URL}/api/2014/equipment/{item_name.lower().replace(' ', '-')}"
        response = requests.get(item_url)

        if response.status_code != 200:
            return Response({"error": "Item not found."}, status=s.HTTP_404_NOT_FOUND)

        item_data = response.json()
        serializer = ItemSerializer(data=item_data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=s.HTTP_200_OK)


class GetRandomItem(APIView):

    def get(self, request):
        try:
            item_list = []
            count = int(request.query_params.get('count', 1))
            while len(item_list) < count:
                # Fetch a random item from the database making sure that they don't repeat
                items = Item.objects.order_by('?')[:count]
                if not items:
                    break
                print(f"Item list: {item_list}")
                item_list.extend(items)
            # print(f"Randomly selected {len(items)} items from the database.")
            serializer = ItemSerializer(item_list, many=True)
            # print(f"Returning {len(serializer.data)} random items.")
            return Response(serializer.data, status=s.HTTP_200_OK)
        except Exception as e:
            print(f"Error occurred while fetching random items: {e}")
            return Response({"error": "An error occurred while fetching random items."}, status=s.HTTP_500_INTERNAL_SERVER_ERROR)

        


class SeedItemsView(APIView):
    def post(self, request):
        EQUIPMENT_CATEGORIES = ['weapon', 'armor', 'potion', 'tools']
        existing_items = set(Item.objects.values_list('name', flat=True))
        new_items = []

        async def fetch_item_detail(session, url):
            async with session.get(url) as resp:
                if resp.status != 200:
                    return None
                return await resp.json()

        async def fetch_all_items():
            async with aiohttp.ClientSession() as session:
                tasks = []
                for category in EQUIPMENT_CATEGORIES:
                    category_url = f"{API_BASE_URL}/api/2014/equipment-categories/{category}"
                    async with session.get(category_url) as resp:
                        if resp.status != 200:
                            continue
                        data = await resp.json()
                        for item_ref in data.get("equipment", []):
                            item_url = f"{API_BASE_URL}{item_ref['url']}"
                            tasks.append(fetch_item_detail(session, item_url))
                return await asyncio.gather(*tasks)

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        item_details = loop.run_until_complete(fetch_all_items())

        for detail in item_details:
            if not detail:
                continue
            name = detail.get("name")
            if name in existing_items:
                continue

            damage_dice = detail.get("damage", {}).get("damage_dice") if "damage" in detail else None
            damage_avg = get_dice_average(damage_dice) if damage_dice else 0

            new_items.append(Item(
                name=name,
                item_category=detail.get("equipment_category", {}).get("name", "misc"),
                damage=damage_avg,
                armor_class=detail.get("armor_class", {}).get("base", 0),
                healing=0,
                rarity=detail.get("rarity", {}).get("name", "common"),
                description=" ".join(detail.get("desc", [])) if isinstance(detail.get("desc"), list) else detail.get("desc", ""),
                cost_amount=detail.get("cost", {}).get("quantity", 0),
                cost_unit=detail.get("cost", {}).get("unit", "gp"),
                is_starter=False
            ))

        # Bulk insert
        with transaction.atomic():
            Item.objects.bulk_create(new_items)

        return Response(f"{len(new_items)} new items added to the database.", status=s.HTTP_201_CREATED)
