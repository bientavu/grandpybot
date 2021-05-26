from grandpy.geocoding import GeocodingClient


response_to_test = {
            'address': 'Rond point des Messageries Maritimes, 13600 La Ciotat, France',
            'lat': 43.1736217,
            'lng': 5.60509
            }

def test_get_geocoding_info(monkeypatch):
    
    class FakeResponse():
        # def raise_for_status(self):
        status_code = 200
        
        def json(self):
            return response_to_test


    def mock_requests_get(url, params):
        return FakeResponse()

    monkeypatch.setattr("requests.get", mock_requests_get)

    client = GeocodingClient()
    results = client.search("mairie de la ciotat")

    assert results == response_to_test

