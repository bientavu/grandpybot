from grandpy.wikipedia import WikipediaClient


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
    
    class FakeResponse():
        def raise_for_status(self):
            status_code = 200
        
        def json(self):
            return response_to_test


    def mock_requests_get(url, params):
        return FakeResponse()

    monkeypatch.setattr("requests.get", mock_requests_get)

    client = WikipediaClient()
    results = client.search(48.85837009999999, 2.2944813)

    assert results == response_to_test