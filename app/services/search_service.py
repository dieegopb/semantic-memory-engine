import os
import requests

class SearchService:

    def search(self, query: str):
        api_key = os.getenv("SERPER_API_KEY")

        url = "https://google.serper.dev/search"

        payload = {
            "q": query
        }

        headers = {
            "X-API-KEY": api_key,
            "Content-Type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)

        data = response.json()

        results = [
            item.get("snippet")
            for item in data.get("organic", [])
        ]

        return results