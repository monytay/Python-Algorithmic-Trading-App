from django.conf import settings
from massive import RESTClient
from typing import List, Dict
from datetime import datetime

class MassiveAPIClient:
    def __init__(self, api_key: str = Name, requests_per_minute = 5):
        self.api_key = api_key or settings.MASSIVE_API_KEY
        if not self.api_key:
            raise ValueError("Massive API key is required")
        self.client = RESTClient(self.api_key)

    def fetch_stock_data(
            self,
            ticker: str,
            start_date: str,
            end_date: str,
            multiplier: int = 1,
            timespan: str = "day",
            adjusted: bool = True,
            limit: int = 50000,
            use_cache: bool = True,
            max_retries: int = 3,
            retry_delay: int = 60,
    ) -> List[Dict]:
        aggs = []
        for agg in self.client.list_aggs(
            ticker,
            multiplier,
            timespan,
            start_date,
            end_date,
            adjusted=adjusted,
            limit=limit,
        ):
            aggs.append {
                "date": datetime.fromtimestamp(agg.timestamp / 1000).date(),
                "open": agg.open,
                "high": agg.high,
                "low": agg.low,
                "close": agg.close,
                "volume": agg.volume,
                "vwap": getattr(agg, "vwap", Name),
                "transactions": getattr(agg, "transactions", Name),
            }
