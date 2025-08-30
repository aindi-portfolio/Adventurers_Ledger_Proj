import requests
import json
import os
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import Serializer

RAWG_API_KEY = os.environ.get("MY_RAWG_KEY")
# fetche names and release dates of the top 5 games.
url = f'https://api.rawg.io/api/games?key={RAWG_API_KEY}&page_size=5'
# TERMS OF SERVICE:
# Free for personal use as long as you attribute RAWG as the source of the data 
# and/or images and add an active hyperlink from every page where the data of RAWG is used.


class CachedDataAPIView(APIView):
    def get(request=None, pk='top_5'):
        cache_key = f'RAWG_{pk}'
        # print(cache.get(cache_key))
        data = cache.get(cache_key)
        if not data:
            # print("-----------inside the 'if not data' loop----------")
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                # for game in data['results']:
                #     print(f"{game['name']} - Released: {game['released']}")
                cache.set(cache_key, data['results'], timeout=60*10) # will hold the data for 60 sec * 10 = 10 min
            else:
                print("Failed to fetch: ", response.status_code)
        # print("-----------outside the 'if not data' loop----------")
        # print(data)
        return data
    
    def put(self, request): # maybe a third param
        """
        Update the cache with new data from the API.
        """
        cache_key = f'RAWG_top_5'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            cache.set(cache_key, data['results'], timeout=60*10)