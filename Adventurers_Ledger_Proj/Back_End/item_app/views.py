import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer
from .utils import get_dice_average

API_BASE_URL = "https://www.dnd5eapi.co"

class SeedWeaponsView(APIView):
    """
    POST /seed-weapons/
    Seeds weapon items from the D&D API into the Item model.
    """

    def post(self, request):
        # Check if the Item model is empty and return json response with item data if it is not empty
        if Item.objects.exists():
            seeded_items = Item.objects.all()[:10]
            serializer = ItemSerializer(seeded_items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        

        category_url = f"{API_BASE_URL}/api/2014/equipment-categories/weapon"
        response = requests.get(category_url)

        if response.status_code != 200:
            return Response({"error": "Failed to fetch weapon category."}, status=status.HTTP_502_BAD_GATEWAY)

        data = response.json()
        equipment_list = data.get("equipment", [])[:10]

        seeded_items = []

        for item_ref in equipment_list:
            item_url = f"{API_BASE_URL}{item_ref['url']}"
            detail_response = requests.get(item_url)

            if detail_response.status_code != 200:
                continue

            item_detail = detail_response.json()
            name = item_detail.get("name")
            description = item_detail.get("desc", [""])[0] if item_detail.get("desc") else ""
            damage_dice = item_detail.get("damage", {}).get("damage_dice")
            damage_type = item_detail.get("damage", {}).get("damage_type", {}).get("name")
            damage_avg = None

            if damage_dice:
                try:
                    damage_avg = get_dice_average(damage_dice)
                except ValueError:
                    pass

            item, created = Item.objects.update_or_create(
                name=name,
                defaults={
                    "item_type": "weapon",
                    "description": description,
                    "effect": damage_dice,
                    "damage": damage_avg or 0,
                }
            )
            seeded_items.append(item)

        serializer = ItemSerializer(seeded_items, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class SeedArmorView(APIView):
    """
    POST /seed-armor/
    Seeds armor items from the D&D API into the Item model.
    """

    def post(self, request):
        if Item.objects.filter(item_type="armor").exists():
            items = Item.objects.filter(item_type="armor")[:10]
            serializer = ItemSerializer(items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        category_url = f"{API_BASE_URL}/api/2014/equipment-categories/armor"
        response = requests.get(category_url)

        if response.status_code != 200:
            return Response({"error": "Failed to fetch armor category."}, status=status.HTTP_502_BAD_GATEWAY)

        data = response.json()
        equipment_list = data.get("equipment", [])[:10]
        seeded_items = []

        for item_ref in equipment_list:
            item_url = f"{API_BASE_URL}{item_ref['url']}"
            detail_response = requests.get(item_url)
            if detail_response.status_code != 200:
                continue

            item_detail = detail_response.json()
            name = item_detail.get("name")
            description = item_detail.get("desc", [""])[0] if item_detail.get("desc") else ""
            armor_class = item_detail.get("armor_class", {}).get("base", 0)

            item, _ = Item.objects.update_or_create(
                name=name,
                defaults={
                    "item_type": "armor",
                    "description": description,
                    "effect": f"AC {armor_class}",
                    "damage": 0,
                }
            )
            seeded_items.append(item)

        serializer = ItemSerializer(seeded_items, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
