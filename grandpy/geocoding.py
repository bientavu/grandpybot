import os
import requests


class GeocodingClient:
    """Connection to the Google Geocoding API to extract data"""
    def __init__(self):
        self.key = os.getenv("GOOGLE_BACK_API_KEY")
        self.url = "https://maps.googleapis.com/maps/api/geocode/json"
        self.params = {
        "key": self.key,
        }
    
    def search(self, search_terms):
        """
        Search throught Google Geocoding API using given keywords
        then extract the data we want : latitude, longitude & address
        """
        self.params['address'] = search_terms

        try:
            response = requests.get(self.url, params=self.params)
            response.raise_for_status()
        except requests.RequestException:
            return None

        data = response.json()

        extracted_data = {}
        extracted_data['lat'] = data['results'][0]['geometry']['location']['lat']
        extracted_data['lng'] = data['results'][0]['geometry']['location']['lng']
        extracted_data['address'] = data['results'][0]['formatted_address']

        return extracted_data
        