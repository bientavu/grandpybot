import requests
from pprint import pprint
# from grandpy.parser import Parser

class GeocodingClient:
    
    def __init__(self):
        self.key = "AIzaSyDlR0cRia0TQImFqBM0d0pN22oVHEBgLxs"
        self.url = "https://maps.googleapis.com/maps/api/geocode/json"
        self.params = {
        "key": self.key,
        }
    
    def search(self, search_terms):
        self.params['address'] = search_terms

        try:
            response = requests.get(self.url, params=self.params)
            response.raise_for_status()
        except requests.RequestException:
            return None
        
        pprint(response.json())

client = GeocodingClient()
client.search("tour eiffel")
