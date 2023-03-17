from pprint import pprint
import requests

SHETTY_PRICES_ENDPOINT = "https://api.sheety.co/1065426cc3b395cf5245578f48c108d7/cópiaDeFlightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):

        response = requests.get(url=SHETTY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHETTY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)