import requests


TEQUILA_ENDPOINT = "https://tequilla-api-kiwi.com"
TEQUILA_API_KEY = "2Em51eGRdWQB5djy6NkNj8EKsrcCGs_V"


class FlightSearch:

    def get_destination_code(self, city_name):
        def get_destination_code(self, city_name):
            # print("get destination codes triggered")
            location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
            headers = {"apikey": TEQUILA_API_KEY}
            query = {"term": city_name, "location_types": "city"}
            response = requests.get(url=location_endpoint, headers=headers, params=query)
            results = response.json()["locations"]
            code = results[0]["code"]
            return code

    #This class is responsible for talking to the Flight Search API.
