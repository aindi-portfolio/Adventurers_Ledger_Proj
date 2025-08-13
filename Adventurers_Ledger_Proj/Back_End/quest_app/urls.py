from django.urls import path
from .views import ExploreQuestView

urlpatterns = [
    path("explore-quest/", ExploreQuestView.as_view(), name="quest"),
]
