import requests
from src.config import Config
from duckduckgo_search import DDGS

class BingSearch:
    def __init__(self):
        self.config = Config()
        self.bing_api_key = self.config.get_bing_api_key()
        self.bing_api_endpoint = self.config.get_bing_api_endpoint()
        self.query_result = None

    def search(self, query):
        headers = {"Ocp-Apim-Subscription-Key": self.bing_api_key}
        params = {"q": query, "mkt": "en-US"}

        try:
            response = requests.get(self.bing_api_endpoint, headers=headers, params=params)
            response.raise_for_status()
            self.query_result = response.json()
            return self.query_result
        except Exception as err:
            return err

    def get_first_link(self):
        return self.query_result["webPages"]["value"][0]["url"]

class DuckDuckGoSearch:
    def search(self, query):
        try:
            self.query_result = DDGS().text(query, max_results=5)
            return self.query_result
        except Exception as err:
            return err

    def get_first_link(self):
        return self.query_result[0]["href"]