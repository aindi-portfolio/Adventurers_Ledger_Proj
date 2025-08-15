from django.urls import path
from .views import QuestView, AdvanceQuestView, GenQuestView

urlpatterns = [
    path("", QuestView.as_view(), name="quest"),
    path("gen-quest", GenQuestView.as_view(), name="gen_quest"),
    path("advance-quest", AdvanceQuestView.as_view(), name="advance_quest"),
]
