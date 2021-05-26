import requests
from pprint import pprint


class WikipediaClient:
    """Connection to the wikipedia API to extract data"""
    def __init__(self):
        self.url = "https://fr.wikipedia.org/w/api.php"
        self.params = {
            "format": "json",
            "action": "query",
            "list": "geosearch",
            "gsradius": 10000,
        }
        
    def search(self, latitude, longitude):
        """
        Search throught Media Wiki API using given coordinates
        then extract the data we want : story + full url
        """
        self.params['gscoord'] = f"{latitude}|{longitude}"

        try:
            response = requests.get(self.url, params=self.params)
            response.raise_for_status()
        except requests.RequestException:
            return None
        
        geosearch_data = response.json()
        page_id = geosearch_data['query']['geosearch'][0]['pageid']

        self.params = {
            "format": "json",
            "action": "query",
            "prop": "extracts|info",
            "inprop": "url",
            "exchars": 600,
            "explaintext": True,
            "pageids": page_id
        }
        pprint(page_id)
        try:
            response = requests.get(self.url, params=self.params)
            response.raise_for_status()
        except requests.RequestException:
            return None

        data = response.json()

        extracted_data = {}
        extracted_data['story'] = data['query']['pages'][str(page_id)]['extract']
        extracted_data['fullurl'] = data['query']['pages'][str(page_id)]['fullurl']

        return extracted_data

