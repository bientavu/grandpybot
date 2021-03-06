from tests.test_geocoding import GET_RESPONSE
from grandpy.wikipedia import WikipediaClient


GET_RESPONSE = {
    "batchcomplete": "",
    "query": {
        "geosearch": [
            {
                "pageid": 1359783,
                "ns": 0,
                "title": "Tour Eiffel",
                "lat": 48.858296,
                "lon": 2.294479,
                "dist": 8.2,
                "primary": ""
            },
            {
                "pageid": 4641538,
                "ns": 0,
                "title": "Le Jules Verne",
                "lat": 48.85825,
                "lon": 2.2945,
                "dist": 13.4,
                "primary": ""
            },
            {
                "pageid": 1869201,
                "ns": 0,
                "title": "Exposition universelle de Paris de 1889",
                "lat": 48.8583,
                "lon": 2.29417,
                "dist": 24.1,
                "primary": ""
            },
            {
                "pageid": 5828872,
                "ns": 0,
                "title": "Buste de Gustave Eiffel par Antoine Bourdelle",
                "lat": 48.85869444,
                "lon": 2.29444444,
                "dist": 36.2,
                "primary": ""
            },
            {
                "pageid": 2689115,
                "ns": 0,
                "title": "Rives de la Seine à Paris",
                "lat": 48.85889,
                "lon": 2.29333,
                "dist": 102.2,
                "primary": ""
            },
            {
                "pageid": 5422123,
                "ns": 0,
                "title": "Avenue Gustave-Eiffel",
                "lat": 48.857388,
                "lon": 2.29463,
                "dist": 109.7,
                "primary": ""
            },
            {
                "pageid": 5422017,
                "ns": 0,
                "title": "Allée Jean-Paulhan",
                "lat": 48.859347,
                "lon": 2.295585,
                "dist": 135.3,
                "primary": ""
            },
            {
                "pageid": 7488373,
                "ns": 0,
                "title": "Grande lunette de l'exposition universelle de Paris 1900",
                "lat": 48.8575,
                "lon": 2.29289,
                "dist": 151.4,
                "primary": ""
            },
            {
                "pageid": 4424460,
                "ns": 0,
                "title": "Allée des Refuzniks",
                "lat": 48.857388,
                "lon": 2.293028,
                "dist": 152.4,
                "primary": ""
            },
            {
                "pageid": 5422039,
                "ns": 0,
                "title": "Allée Paul-Deschanel",
                "lat": 48.859428,
                "lon": 2.296124,
                "dist": 168.2,
                "primary": ""
            }
        ]
    }
}

GET_RESPONSE_2 = {
    "batchcomplete": "",
    "query": {
        "pages": {
            "1359783": {
                "pageid": 1359783,
                "ns": 0,
                "title": "Tour Eiffel",
                "extract": "La tour Eiffel  est une tour de fer puddlé de 324 mètres de hauteur (avec antennes) située à Paris, à l’extrémité nord-ouest du parc du Champ-de-Mars en bordure de la Seine dans le 7e arrondissement. Son adresse officielle est 5, avenue Anatole-France.\nConstruite en deux ans par Gustave Eiffel et ses collaborateurs pour l’Exposition universelle de Paris de 1889, et initialement nommée « tour de 300 mètres », elle est devenue le symbole de la capitale française et un site touristique de premier plan : il s’agit du troisième site culturel français payant le plus visité en 2015, avec 5,9 millions...",
                "contentmodel": "wikitext",
                "pagelanguage": "fr",
                "pagelanguagehtmlcode": "fr",
                "pagelanguagedir": "ltr",
                "touched": "2021-05-26T08:13:23Z",
                "lastrevid": 183268945,
                "length": 133333,
                "fullurl": "https://fr.wikipedia.org/wiki/Tour_Eiffel",
                "editurl": "https://fr.wikipedia.org/w/index.php?title=Tour_Eiffel&action=edit",
                "canonicalurl": "https://fr.wikipedia.org/wiki/Tour_Eiffel"
            }
        }
    }
}

response_to_test = {
            'fullurl': 'https://fr.wikipedia.org/wiki/Tour_Eiffel',
            'story': 'La tour Eiffel  est une tour de fer puddlé de 324 mètres de hauteur '
            '(avec antennes) située à Paris, à l’extrémité nord-ouest du parc du '
            'Champ-de-Mars en bordure de la Seine dans le 7e arrondissement. Son '
            'adresse officielle est 5, avenue Anatole-France.\n'
            'Construite en deux ans par Gustave Eiffel et ses collaborateurs '
            'pour l’Exposition universelle de Paris de 1889, et initialement '
            'nommée « tour de 300 mètres », elle est devenue le symbole de la '
            'capitale française et un site touristique de premier plan : il '
            's’agit du troisième site culturel français payant le plus visité en '
            '2015, avec 5,9 millions...'
            }

def test_get_wikipedia_info(monkeypatch):
    
    class FakeResponse:
        responses = iter([GET_RESPONSE, GET_RESPONSE_2])

        def raise_for_status(self):
            status_code = 200   

        def json(self):
            return next(self.responses)

    def mock_requests_get(url, params):
        return FakeResponse()
            
    monkeypatch.setattr("requests.get", mock_requests_get)

    client = WikipediaClient()
    results = client.search(48.85837009999999, 2.2944813)

    assert results == response_to_test
