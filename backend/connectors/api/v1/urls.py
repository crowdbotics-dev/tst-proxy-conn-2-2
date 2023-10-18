from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import TrelloViewSet, TMDBViewSet, CrowdboticsStagingViewSet

router = DefaultRouter()
router.register("trello", TrelloViewSet, basename="trello")
router.register("tmdb", TMDBViewSet, basename="tmdb")
router.register(
    "crowdboticsstaging", CrowdboticsStagingViewSet, basename="crowdboticsstaging"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
