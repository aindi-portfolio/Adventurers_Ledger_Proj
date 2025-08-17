import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as s
from .serializers import Monster, MonsterSerializer
from .utils import get_dice_average
import random

API_BASE_URL = "https://www.dnd5eapi.co"


class SeedMonstersView(APIView):
    """
    POST /seed-weapons/
    Seeds weapon items from the D&D API into the Monster model.
    """

    def post(self, request):
        """
        1ST PULL: Fetches list of monsters and another url that takes to each monster
        2ND PULL: Fetches each monster's details from the provided url in the first pull
        """

        # 1ST PULL: Fetches list of monsters by challenge rating
        challenge_rating = request.data.get("challenge_rating")
        monsters_by_CR = f"{API_BASE_URL}/api/2014/monsters?challenge_rating={challenge_rating}"
        response = requests.get(monsters_by_CR)

        if response.status_code != 200:
            return Response({"error": "Failed to fetch weapon category."}, status=s.HTTP_502_BAD_GATEWAY)

        data = response.json()
        
        monster_list = data.get("results", []) # Ensure this key matches the API response structure
        print (f"Total monsters added: {len(monster_list)}")

        # 2ND PULL: Fetches each monster's details from the provided url in the first pull
        for monster_ref in monster_list:
            item_url = f"{API_BASE_URL}{monster_ref['url']}"
            detail_response = requests.get(item_url)

            if detail_response.status_code != 200:
                print(f"Failed the 2ND PULL for monsters")
                continue

            monster_details = detail_response.json()

            name = monster_details.get("name")
            type = monster_details.get("type", "unknown") # Default to "unknown" if not provided
            health = monster_details.get("hit_points", 10) # Default to 10 if not provided
            damage = monster_details.get("hit_dice", "1d10")  # Default to "1d10" if not provided
            damage_avg = get_dice_average(damage)

            armor_list = monster_details.get("armor_class", [])  # Need to use the list because armor_class will be list of dicts
            armor = armor_list[0]["value"] if armor_list else 10 # Value from the first dict in the list, default to 10 if list is empty


            xp = monster_details.get("xp", 50)  # Default to 50 if not provided

            senses = monster_details.get("senses", {}) # passive_perception is nested in senses
            passive_perception = senses.get("passive_perception", 5)  # Default to 5 if not provided
            
            image_path = monster_details.get("image")
            image_url = f"{API_BASE_URL}{image_path}" if image_path else ""


            monster, created = Monster.objects.update_or_create(
                name=name,
                type=type,
                health=health,
                damage = damage_avg,
                armor=armor,
                xp=xp,
                passive_perception=passive_perception,
                image_url=image_url,  
            )
            
            monster.save()

        print (f"Monsters with CR: {challenge_rating} have been added to the Data Base")
        print (f"Total monsters added to the DB: {Monster.objects.count()}")
        return Response(f"{Monster.objects.count()} Monsters with CR: {challenge_rating} have been added to the Data Base", status=s.HTTP_201_CREATED)
    

class RandomMonsterByCR(APIView):
    """
    GET /random-monster/
    Returns a random monster from the Monster model.
    """

    def get(self, request):
        """
        Returns a list of monsters filtered by challenge rating.
        If no challenge rating is provided, it returns a random monster from the entire Monster model.
        If no mosters with the provided challenge rating are found, then triggers SeedMonstersView to seed the monsters.
        """
        
        challenge_rating = request.GET.get("challenge_rating")
        
        if challenge_rating:
            try:
                challenge_rating = float(challenge_rating)
                print(f"Challenge Rating provided: {challenge_rating}")
            except ValueError:
                return Response({"error": "Invalid challenge rating."}, status=s.HTTP_400_BAD_REQUEST)

            monsters = Monster.objects.filter(xp__gte=challenge_rating * 100)
            serialized_monsters = MonsterSerializer(monsters, many=True)
            return Response(serialized_monsters.data, status=s.HTTP_200_OK)
        else:
            print("No challenge rating provided, fetching a random monster from the entire Monster model.")
            monsters = Monster.objects.all()
            if not monsters.exists():
                print("No monsters found, seeding monsters.")
                SeedMonstersView().post(request)

        