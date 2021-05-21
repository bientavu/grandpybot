from grandpy.geocoding import GeocodingClient
import urllib.request
from io import BytesIO
import json

class TestGeocodingClient:

    def test_http_return(self, monkeypatch):
        results = {
            'address': 'Rond point des Messageries Maritimes, 13600 La Ciotat, France',
            'lat': 43.1736217,
            'lng': 5.60509
            }

        def mockreturn(request):
            return BytesIO(json.dumps(results).encode())

        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

        client = GeocodingClient()
        result = client.search("mairie de la ciotat")
        assert result == results

