from django.apps import AppConfig


class ItemAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'item_app'

# from django.apps import AppConfig
# from django.db.utils import OperationalError
# from .models import Item
# import requests

# class ItemAppConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'item_app'

#     def ready(self):
#         try:
#             if Item.objects.count() == 0:
#                 print("Seeding items from D&D API...")
#                 self.seed_items()
#         except OperationalError:
#             # Avoid errors during migrations
#             pass

#     def seed_items(self):
#         url = "https://www.dnd5eapi.co/api/equipment"
#         response = requests.get(url)
#         data = response.json()

#         for entry in data.get("results", [])[:20]:
#             detail = requests.get(f"https://www.dnd5eapi.co{entry['url']}").json()
#             name = detail.get("name")
#             category = detail.get("equipment_category", {}).get("name", "").lower()

#             if "weapon" in category:
#                 item_type = "weapon"
#                 effect = f"{detail.get('damage', {}).get('dice_count', 1)}d{detail.get('damage', {}).get('dice_value', 6)}"
#             elif "armor" in category:
#                 item_type = "armor"
#                 effect = f"AC {detail.get('armor_class', {}).get('base', 10)}"
#             elif "potion" in name.lower():
#                 item_type = "potion"
#                 effect = "Heals HP"
#             else:
#                 item_type = "misc"
#                 effect = ""

#             description = detail.get("desc", [""])[0] if detail.get("desc") else ""

#             Item.objects.get_or_create(
#                 name=name,
#                 defaults={
#                     "item_type": item_type,
#                     "effect": effect,
#                     "description": description,
#                     "is_starter": False,
#                     "image_url": None
#                 }
#             )
