import random
import requests
import json
import os
from dotenv import load_dotenv
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as s
from .models import Quest
from .serializers import QuestSerializer

load_dotenv('.env')  # Load environment variables


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
        OPENROUTER_API_KEY = os.environ.get("DEEPSEEK_FREE")  # Update your .env key name

        quest_title = request.data.get("quest_title")
        quest_description = request.data.get("quest_description")
        
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
                    "model": "deepseek/deepseek-r1-0528:free",
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
        OPENROUTER_API_KEY = os.environ.get("DEEPSEEK_FREE")  # Update your .env key name
        quest_title = request.data.get("quest_title")
        quest_description = request.data.get("quest_description")
        history = request.data.get("history", [])
        player_choice = request.data.get("choice")

        if not quest_title or not quest_description or not player_choice:
            return Response({"error": "Missing required fields."}, status=s.HTTP_400_BAD_REQUEST)

        # Build prompt
        prompt = f"""The player begins the quest: {quest_title}. {quest_description} Without breaking the immersion, give 
        me one line for what happens when the player makes that choice. Then give two (one word) options that will drive the story to a successful or failed end."""
        for i, entry in enumerate(history):
            prompt += f"Round {i+1}:\nPlayer chooses: {entry['choice']}\nResult: {entry['response']}\n"
        prompt += f"Player chooses: {player_choice}\n"

        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            data=json.dumps({
                "model": "deepseek/deepseek-r1-0528:free",
                "messages": [{"role": "user", "content": prompt}]
            })
        )

        if response.status_code != 200:
            return Response({"error": "LLM failed"}, status=s.HTTP_502_BAD_GATEWAY)

        content = response.json()["choices"][0]["message"]["content"]

        # Detect ending
        is_complete = "quest is complete" in content.lower() or "quest failed" in content.lower()
        outcome = "success" if "complete" in content.lower() else "failure" if "failed" in content.lower() else None

        return Response({
            "response": content,
            "choices": ["Option A", "Option B"],  # You can parse these from content later
            "is_complete": is_complete,
            "outcome": outcome
        }, status=s.HTTP_200_OK)

