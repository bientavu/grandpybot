from grandpy.parser import Parser
from grandpy.geocoding import GeocodingClient
from grandpy.wikipedia import WikipediaClient
from pprint import pprint

class App:

    def answer(self, question):
        # 1. Question nettoyée = utiliser une classe Parser pour
        #    analyser la question et conserver uniquement l'info
        #    utile (c'est à dire l'info de lieu)
        parser = Parser()
        keywords = parser.execute_parser(question)

        # 2. La question nettoyée est envoyée à une API de geocoding
        #    (google) pour obtenir (a) l'adresse du lieu et (b)
        #    les coordonnées de latitude et longitude
        geocoding_client = GeocodingClient()
        geocoding_client_data = geocoding_client.search(keywords)
        latitude = geocoding_client_data['lat']
        longitude = geocoding_client_data['lng']

        # 3. Envoyer la latitude et la longitude à l'API wikipedia
        #    qui va nous envoyer des articles liés à ces coordonnées.
        #    On choisit l'article consernant le lieu le plus proche
        wikipedia_client = WikipediaClient()
        wikipedia_client_data = wikipedia_client.search(latitude, longitude)

        full_data = {}
        full_data['latitude'] = latitude
        full_data['longitude'] = longitude
        full_data['address'] = geocoding_client_data['address']
        full_data['story'] = wikipedia_client_data['story']
        full_data['fullurl'] = wikipedia_client_data['fullurl']
        full_data['grandpy_address'] = "Hello, j'ai trouvé ce que tu m'as demandé :) Voici l'adresse : "
        full_data['grandpy_wiki'] = "J'ai également trouvé une petite anecdote concernant un lieu proche de ton adresse : "

        return full_data
            # Infos récupérées en réponse à la question
        