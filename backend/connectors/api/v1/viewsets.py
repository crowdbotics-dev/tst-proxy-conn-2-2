
import requests
import base64
import urllib.parse
from django.conf import settings
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

class BaseConnectorViewSet(viewsets.GenericViewSet):
    BASE_URL = None
    AUTH_TYPE = None
    USERNAME = None
    PASSWORD = None
    TOKEN = None
    SECRET = None
    QUERY_NAME = None
    
    def _generate_basic_token(self):
        return base64.b64encode(f"{self.USERNAME}:{self.PASSWORD}".encode("utf-8")).decode("utf-8")

    def _get_authorization_value(self):
        if self.AUTH_TYPE == "basic":
            return f"Basic {self._generate_basic_token()}"
        if self.AUTH_TYPE == "bearer":
            return f"Bearer {self.TOKEN}"
        return ""

    def _get_headers(self):
        return {"Authorization": self._get_authorization_value()}

    def _get_params(self):
        if not self.QUERY_NAME:
            return {}
        return {self.QUERY_NAME: self.SECRET}

    def _api_call(self, url, request_type="get", payload=None, headers=None, params=None):
        payload = payload or {}
        headers = headers or {}
        params = params or {}
        base_url = self.BASE_URL.endswith("/") and self.BASE_URL or f"{self.BASE_URL}/"
        url = urllib.parse.urljoin(base_url, url.lstrip("/"))
        response = requests.request(request_type, url, data=payload, params={**self._get_params(), **params}, headers={**self._get_headers(), **headers})
        try:
            return response.json()
        except Exception:
            return {}

class TrelloViewSet(BaseConnectorViewSet):
    SECRET = settings.TRELLO_SECRET
    QUERY_NAME = "token"
    BASE_URL = "https://api.trello.com/1/"
    AUTH_TYPE = "apiKey"
    IDENTIFIER = "TRELLO"
    
    @action(detail=False, methods=["get"], url_path="search")
    def search(self, request, *args, **kwargs):
        params = request.query_params
        payload = request.data
        data = self._api_call("/search", request_type="get", payload=payload, params=params)
        return Response(data)
 
