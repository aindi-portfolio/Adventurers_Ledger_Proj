import random
import requests
import json
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as s
from .models import Quest
from .serializers import QuestSerializer


# QuestView: A view to handle quest retrieval from the DB
class QuestView(APIView):
    """
    GET /explore-quest/
    Returns a random quest and a story from OpenRouter.
    """

    def get(self, request):
        quests = Quest.objects.all() # These 'quests' is a QuerySet of all quests in the DB
        if not quests.exists():
            return Response({"error": "No quests available."}, status=s.HTTP_404_NOT_FOUND)

        # Select a random quest
        quest = random.choice(quests) # This 'quest' is a single Quest object from the DB
        serializer = QuestSerializer(quest)
        print(f"Selected quest: {quest.title}\nDescription: {quest.description}")
        return Response({"quest": serializer.data}, status=s.HTTP_200_OK)

        
# GenQuestView: Takes a quest title and description and submits it to the LLM to generate a quest.
class GenQuestView(APIView):
    def post(self, request):
        # Generate story intro using OpenRouter
        OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")

        quest_title = request.data.get("quest_title")
        quest_description = request.data.get("quest_description")
        
        # Build the prompt for the LLM
        prompt = f"""
        Based on the following quest:
        Title: {quest_title}
        Description: {quest_description}

        Return a JSON object with the following structure:
        {
            {
            "title": "string",
            "description": "string",
            "decision_point": "string",
            "choices": ["Yes", "No"]
            }
        }

        Do not include any explanation or extra text. Just return the JSON object.
        """

        try:
            response = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                    "Content-Type": "application/json",
                    "HTTP-Referer": "http://localhost:8000",  # Optional
                    "X-Title": "QuestEngine",  # Optional
                },
                data=json.dumps({
                    "model": "tngtech/deepseek-r1t2-chimera:free",
                    "messages": [
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                })
            )

            if response.status_code != 200:
                return Response({"error": "LLM failed to generate story."}, status=s.HTTP_502_BAD_GATEWAY)

            content = response.json()["choices"][0]["message"]["content"] # This 'quest' is the generated story
            print(f"Generated story: {content}")
            structured_story = json.loads(content) # Convert the string to a JSON object
            print(f"Structured story: {structured_story}")

        except Exception as e:
            return Response({"error": f"LLM request failed: {str(e)}"}, status=s.HTTP_500_INTERNAL_SERVER_ERROR)

        # Return story
        
        return Response({"quest": structured_story}, status=s.HTTP_200_OK)

class AdvanceQuestView(APIView):
    """
    POST /advance-quest/
    Accepts story history and player choice, returns next story segment + choices.
    """

    def post(self, request):
        OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
        
        print("Incoming Payload:", request.data)
        quest_data = request.data.get("quest") # This is the response from GenQuestView
        player_choice = request.data.get("choice") # player's choice to advance the quest

        if not quest_data or not player_choice:
            print(f"-------Missing quest data or player choice. Error: {s.HTTP_400_BAD_REQUEST}-------")
            return Response({"error": "Missing required fields."}, status=s.HTTP_400_BAD_REQUEST) # Edge case

        # Extract quest title and description
        title = quest_data.get("title")
        description = quest_data.get("description")
        decision_point = quest_data.get("decision_point")
        choices = quest_data.get("choices")

        if not title or not description or not decision_point or not choices:
            return Response({"error": "Incomplete quest structure."}, status=s.HTTP_400_BAD_REQUEST)

        # Build prompt so the LLM responds in JSON format with desired structure
        prompt = f"""
        Quest Title: {title}
        Quest Description: {description}
        Decision Point: {decision_point}
        Player Choice: {player_choice}

        Based on this choice, return a JSON object with the final outcome of the quest. Use this format:
        {{
            "outcome": "success" or "failure",
            "summary": "A one-line immersive description of what happens as a result of the player's choice."
            "health_change": "integer",
            "gold_change": "integer",
            "exp_change": "integer",
            "quest_complete": "boolean"
        }}

        Do not include any extra text or explanation. Just return the JSON object.
        """

        print(f"Prompt for LLM: {prompt}") # Debugging line to see the prompt sent to the LLM
        
        try:
            response = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                    "Content-Type": "application/json"
                },
                data=json.dumps({
                    "model": "tngtech/deepseek-r1t2-chimera:free",
                    "messages": [
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                })
            )

            if response.status_code != 200:
                return Response({"error": "------------LLM failed-------------"}, status=s.HTTP_502_BAD_GATEWAY)

            content = response.json()["choices"][0]["message"]["content"]
            print(f"LLM response: {content}")
        
            final_result = json.loads(content)  # Convert the string to a JSON object
            return Response({"result": final_result}, status=s.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": f"--------LLM request failed: {str(e)}------------"}, status=s.HTTP_500_INTERNAL_SERVER_ERROR)
