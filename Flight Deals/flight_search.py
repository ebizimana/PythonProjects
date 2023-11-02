import requests
from flight_data import FlightData


# This class is responsible for talking to the Flight Search API.
class FlightSearch:
    def __init__(self):
        API_KEY = "QcBqpaiy9ZNRczV3cYMhRnYH4bLMFNDM"
        self.headers = {"apikey": API_KEY}

    # Search for City IATA
    def search_iata(self, city):
        location_params = {"term": city}
        LOCATION_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"

        response = requests.get(url=LOCATION_ENDPOINT, params=location_params, headers=self.headers)
        response.raise_for_status()
        data = response.json()["locations"][0]
        return data["code"]

    # Search for cheap flight
    def flight_info(self, city_from, city_to, cities_data):
        flight_info_class = FlightData()

        SEARCH_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
        params = flight_info_class.search_params(city_from=city_from, city_to=city_to, cities_data=cities_data)

        # Get the flight_info
        search_response = requests.get(url=SEARCH_ENDPOINT, params=params, headers=self.headers)
        search_response.raise_for_status()

        try:
            search_data = search_response.json()["data"][0]
            route = search_data["route"][0]

            # Get flight info
            fight_info = {
                "price": search_data["price"],
                "city_from": city_from,
                "fly_from": route["flyFrom"],
                "city_to": city_to,
                "fly_to": route["flyTo"],
                "out_date": route["local_departure"].split("T")[0],
                "return_date": search_data["route"][1]["local_departure"].split("T")[0]
            }
            return fight_info

        except IndexError:
            return print(f"No flights found for {city_to}.")

    def lowest_price(self, city_to, cities_data, price):
        for entry in cities_data:
            if entry["city"] == city_to:
                if price < entry["lowestPrice"]:
                    return True
                else:
                    return False


