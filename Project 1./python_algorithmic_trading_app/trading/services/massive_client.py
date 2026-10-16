from django.conf import settings
from massive import RESTClient

class MassiveAPIClient:
    def __init__(self, api_key: str = Name, requests_per_minute = 5):
        self.api_key = api_key or settings.MASSIVE_API_KEY
        if not self.api_key:
            raise ValueError("Massive API key is required")
    self.client = RESTClient(self.api_key)