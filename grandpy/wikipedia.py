import requests
from pprint import pprint


class WikipediaClient:

    def __init__(self):
        self.url = "https://fr.wikipedia.org/w/api.php"
        self.params = {
            "format": "json", # format de la réponse
            "action": "query", # action à réaliser
            "list": "geosearch", # méthode de recherche
            "gsradius": 10000, # rayon de recherche autour des coordonnées GPS fournies (max 10'000 m)
        }
        
    def search(self, latitude, longitude):

        self.params['gscoord'] = f"{latitude}|{longitude}"

        try:
            response = requests.get(self.url, params=self.params)
            response.raise_for_status()
        except requests.RequestException:
            return None
        
        geosearch_data = response.json()

        page_id = geosearch_data['query']['geosearch'][0]['pageid']

        self.params = {
            "format": "json", # format de la réponse
            "action": "query", # action à effectuer
            "prop": "extracts|info", # Choix des propriétés pour les pages requises
            "inprop": "url", # Fournit une URL complète, une URL de modification, et l’URL canonique de chaque page.
            "exchars": 600, # Nombre de caractères à retourner
            "explaintext": True, # Renvoyer du texte brut (éliminer les balises de markup)
            "pageids": page_id
        }

        try:
            response = requests.get(self.url, params=self.params)
            response.raise_for_status()
        except requests.RequestException:
            return None

        data = response.json()

        extracted_data = {}
        extracted_data['story'] = data['query']['pages'][page_id]['extract']
        extracted_data['fullurl'] = data['query']['pages'][page_id]['fullurl']

        return extracted_data

client = WikipediaClient()
result = client.search(48.85837009999999, 2.2944813)
pprint(result)

