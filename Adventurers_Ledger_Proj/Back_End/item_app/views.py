import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as s
from .models import Item
from .serializers import ItemSerializer
from .utils import get_dice_average

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

class SeedItemsView(APIView):
    """
    POST /seed-weapons/
    Seeds weapon items from the D&D API into the Item model.
    """

    def post(self, request):
        # Check if the Item model is empty and return json response with item data if it is not empty

        EQUIPMENT_CATEGORIES = [
            ('weapon', 'Weapon'),
            ('armor', 'Armor'),
            ('potion', 'Potion'),
            ('tools', 'Tool'),
        ]


        for category_key, category_name in EQUIPMENT_CATEGORIES:
            category_url = f"{API_BASE_URL}/api/2014/equipment-categories/{category_key}"
            response = requests.get(category_url)

            if response.status_code != 200:
                return Response({"error": f"Failed to fetch {category_name} category."}, status=s.HTTP_502_BAD_GATEWAY)

            data = response.json()
            equipment_list = data.get("equipment", [])

            for item_ref in equipment_list:
                try:
                    item_url = f"{API_BASE_URL}{item_ref['url']}"
                    detail_response = requests.get(item_url)

                    if detail_response.status_code != 200:
                        continue

                    item_detail = detail_response.json()
                    name = item_detail.get("name")

                    item_category = item_detail.get("equipment_category", {}).get("name", "misc")

                    damage_dice = item_detail.get("damage", {}).get("damage_dice")
                    damage_avg = get_dice_average(damage_dice) if damage_dice else 0

                    armor_class = item_detail.get("armor_class", {}).get("base", 0)

                    rarity = item_detail.get("rarity", {}).get("name", "common")

                    description = item_detail.get("desc", "")
                    cost_amount = item_detail.get("cost", {}).get("quantity", 0)
                    cost_unit = item_detail.get("cost", {}).get("unit", "gp")

                    # Check if the item already exists in the database
                    if Item.objects.filter(name=name, item_category=item_category).exists():
                        print(f"Item {name} already exists in the database, skipping.")
                        continue

                    # Otherwise, create or update the item
                    item, created = Item.objects.update_or_create(
                        name=name,
                        item_category=item_category,
                        damage=damage_avg,
                        armor_class=armor_class,
                        healing=0,
                        rarity=rarity,
                        description=" ".join(description) if isinstance(description, list) else description,
                        cost_amount=cost_amount,
                        cost_unit=cost_unit,
                        is_starter=False
                    )
                    item.save()

                except Exception as e:
                    print(f"Error processing item {item_ref['name']}: {e}")
                    continue

        return Response(f"{Item.objects.count()} Items have been added to the Data Base", status=s.HTTP_201_CREATED)


