
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import TrelloViewSet
router = DefaultRouter()
router.register('trello', TrelloViewSet, basename='trello')

urlpatterns = [
    path("connectors/", include(router.urls)),
]
