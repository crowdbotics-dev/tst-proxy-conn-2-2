
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import TrelloViewSet,TMDBViewSet
router = DefaultRouter()
router.register('trello', TrelloViewSet, basename='trello')
router.register('tmdb', TMDBViewSet, basename='tmdb')

urlpatterns = [
    path("connectors/", include(router.urls)),
]
