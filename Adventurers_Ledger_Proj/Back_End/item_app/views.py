import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as s
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

        STARTER_ITEMS_FOR_CLASSES = [ # For future class selection, these are the starter item by name (not index in D&D API)
            {
                "class": "barbarian",
                "items": ["Handaxe", "Handaxe", "Chain Mail"] # Future enhancement: let user select class and starting weapon
            },
            {
                "class": "fighter",
                "items": ["Longsword", "Shield", "Chain Mail"]
            },
            {
                "class": "wizard",
                "items": ["Quarterstaff", "Spellbook", "Component Pouch"]
            },
            {
                "class": "rogue",
                "items": ["Shortsword", "Dagger", "Leather Armor"]
            }
        ]

        EQUIPMENT_CATEGORIES = [
        ('weapon', 'Weapon'), # left is index in D&D API, right is the name of the item
        ('armor', 'Armor'),
        ('misc', 'Miscellaneous'),
        ('potion', 'Potion'),
        ('tool', 'Tool'), # index 'tools' in D&D API
        ('adventuring_gear', 'Adventuring Gear'),
    ]

        category_url = f"{API_BASE_URL}/api/2014/equipment-categories/weapon"
        response = requests.get(category_url)

        if response.status_code != 200:
            return Response({"error": "Failed to fetch weapon category."}, status=s.HTTP_502_BAD_GATEWAY)

        data = response.json()
        equipment_list = data.get("equipment", [])[:10]

        for item_ref in equipment_list:
            item_url = f"{API_BASE_URL}{item_ref['url']}"
            detail_response = requests.get(item_url)

            if detail_response.status_code != 200:
                continue

            item_detail = detail_response.json()
            name = item_detail.get("name")

            category_list = item_detail.get("equipment_category", "misc")
            item_category = category_list.get("name")

            damage_dice = item_detail.get("damage", {}).get("damage_dice")
            damage_avg = get_dice_average(damage_dice) if damage_dice else 0

            armor_class_list = item_detail.get("armor_class", {})
            armor_class = armor_class_list.get("base", 0) if armor_class_list else 0 # Future enhancement: add armor_class bonus from dex

            rarity_list = item_detail.get("rarity", {})
            rarity = rarity_list.get("name", "common") if rarity_list else "common"

            description = item_detail.get("desc") if item_detail.get("desc") else "" # List of strings, join them

            cost_list = item_detail.get("cost", {})
            cost_amount = cost_list.get("quantity", 0) if cost_list else 0
            cost_unit = cost_list.get("unit", "gp") if cost_list else "gp"

            if damage_dice:
                try:
                    damage_avg = get_dice_average(damage_dice)
                except ValueError:
                    pass

            item, created = Item.objects.update_or_create(
                name=name,
                item_category=item_category,
                damage = damage_avg,  # Average damage from the damage_dice
                armor_class = armor_class,
                healing = 0,  # No healing for weapons
                rarity = rarity,
                description = " ".join(description) if isinstance(description, list) else description,
                cost_amount = cost_amount,
                cost_unit = cost_unit,
                is_starter = False
            )
            item.save()
        return Response(f"{Item.objects.count()} Items with equipment_category 'Weapon' have been added to the Data Base", status=s.HTTP_201_CREATED)



class SeedArmorView(APIView):
    """
    POST /seed-armor/
    Seeds armor items from the D&D API into the Item model.
    """

    def post(self, request):
        if Item.objects.filter(item_type="armor").exists():
            items = Item.objects.filter(item_type="armor")[:10]
            serializer = ItemSerializer(items, many=True)
            return Response(serializer.data, status=s.HTTP_200_OK)

        category_url = f"{API_BASE_URL}/api/2014/equipment-categories/armor"
        response = requests.get(category_url)

        if response.status_code != 200:
            return Response({"error": "Failed to fetch armor category."}, status=s.HTTP_502_BAD_GATEWAY)

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
                    "armor_class": {armor_class} or 0,
                }
            )
            seeded_items.append(item)

        serializer = ItemSerializer(seeded_items, many=True)
        return Response(serializer.data, status=s.HTTP_201_CREATED)
