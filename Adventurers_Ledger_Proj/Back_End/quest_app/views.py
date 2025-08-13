import random
import requests
import json
import os
from dotenv import load_dotenv
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Quest
from .serializers import QuestSerializer

load_dotenv('.env')  # Load environment variables

class ExploreQuestView(APIView):
    """
    GET /explore-quest/
    Returns a random quest and a story intro from OpenRouter.
    """

    def get(self, request):
        quests = Quest.objects.all()
        if not quests.exists():
            return Response({"error": "No quests available."}, status=status.HTTP_404_NOT_FOUND)

        OPENROUTER_API_KEY = os.environ.get("DEEPSEEK_FREE")  # Update your .env key name
        # 🎲 Select a random quest
        quest = random.choice(quests)
        serializer = QuestSerializer(quest)
        print(f"Selected quest: {quest.title}\nDescription: {quest.description}")
        # 🧠 Generate story intro using OpenRouter
        if not OPENROUTER_API_KEY:
            return Response({"error": "Missing OpenRouter API key."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        prompt = f"""The player begins the quest: {quest.title}. {quest.description} Without breaking the immersion, give 
        me a maximum two lines for what happens when the player begins the quest. Then give two options,'Yes' or 'No', for what the player will do next."""

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
                return Response({"error": "LLM failed to generate story."}, status=status.HTTP_502_BAD_GATEWAY)

            story = response.json()["choices"][0]["message"]["content"]

        except Exception as e:
            return Response({"error": f"LLM request failed: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # ✅ Return quest + story
        return Response({
            "quest": serializer.data,
            "story_intro": story
        }, status=status.HTTP_200_OK)


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
            return Response({"error": "Missing required fields."}, status=status.HTTP_400_BAD_REQUEST)

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
            return Response({"error": "LLM failed"}, status=status.HTTP_502_BAD_GATEWAY)

        content = response.json()["choices"][0]["message"]["content"]

        # Detect ending
        is_complete = "quest is complete" in content.lower() or "quest failed" in content.lower()
        outcome = "success" if "complete" in content.lower() else "failure" if "failed" in content.lower() else None

        return Response({
            "response": content,
            "choices": ["Option A", "Option B"],  # You can parse these from content later
            "is_complete": is_complete,
            "outcome": outcome
        }, status=status.HTTP_200_OK)
