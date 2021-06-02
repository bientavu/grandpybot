from grandpy.geocoding import GeocodingClient


GET_RESPONSE = {
    "results": [
        {
            "address_components": [
                {
                    "long_name": "Rond point des Messageries Maritimes",
                    "short_name": "Rond point des Messageries Maritimes",
                    "types": [
                        "route"
                    ]
                },
                {
                    "long_name": "La Ciotat",
                    "short_name": "La Ciotat",
                    "types": [
                        "locality",
                        "political"
                    ]
                },
                {
                    "long_name": "Bouches-du-Rhône",
                    "short_name": "Bouches-du-Rhône",
                    "types": [
                        "administrative_area_level_2",
                        "political"
                    ]
                },
                {
                    "long_name": "Provence-Alpes-Côte d'Azur",
                    "short_name": "Provence-Alpes-Côte d'Azur",
                    "types": [
                        "administrative_area_level_1",
                        "political"
                    ]
                },
                {
                    "long_name": "France",
                    "short_name": "FR",
                    "types": [
                        "country",
                        "political"
                    ]
                },
                {
                    "long_name": "13600",
                    "short_name": "13600",
                    "types": [
                        "postal_code"
                    ]
                }
            ],
            "formatted_address": "Rond point des Messageries Maritimes, 13600 La Ciotat, France",
            "geometry": {
                "location": {
                    "lat": 43.1736217,
                    "lng": 5.60509
                },
                "location_type": "GEOMETRIC_CENTER",
                "viewport": {
                    "northeast": {
                        "lat": 43.1749706802915,
                        "lng": 5.606438980291502
                    },
                    "southwest": {
                        "lat": 43.1722727197085,
                        "lng": 5.603741019708498
                    }
                }
            },
            "place_id": "ChIJTyLVWnOvyRIRsddgmzdGBL0",
            "plus_code": {
                "compound_code": "5JF4+C2 La Ciotat, France",
                "global_code": "8FM75JF4+C2"
            },
            "types": [
                "city_hall",
                "establishment",
                "local_government_office",
                "point_of_interest"
            ]
        }
    ],
    "status": "OK"
}

response_to_test = {
                    "address": "Rond point des Messageries Maritimes, 13600 La Ciotat, France",
                    "lat": 43.1736217,
                    "lng": 5.60509
                }

def test_get_geocoding_info(monkeypatch):
    
    class FakeResponse:
        def raise_for_status(self):
            status_code = 200
        
        def json(self):
            return GET_RESPONSE


    def mock_requests_get(url, params):
        return FakeResponse()

    monkeypatch.setattr("requests.get", mock_requests_get)

    client = GeocodingClient()
    results = client.search("mairie de la ciotat")

    assert results == response_to_test
