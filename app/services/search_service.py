import os
import logging
from typing import List

import requests

logger = logging.getLogger(__name__)


class SearchService:

    def search(self, query: str) -> List[str]:
        api_key = os.getenv("SERPER_API_KEY")

        if not api_key:
            logger.warning("SERPER_API_KEY not set; returning empty results")
            return []

        url = "https://google.serper.dev/search"

        payload = {"q": query}

        headers = {
            "X-API-KEY": api_key,
            "Content-Type": "application/json",
        }

        try:
            response = requests.post(url, json=payload, headers=headers, timeout=5)
            response.raise_for_status()
        except requests.RequestException as exc:
            logger.warning("Search request failed: %s", exc)
            return []

        try:
            data = response.json()
        except ValueError:
            logger.warning("Invalid JSON response from search API")
            return []

        results = [
            item.get("snippet")
            for item in data.get("organic", [])
            if item.get("snippet")
        ]

        return results