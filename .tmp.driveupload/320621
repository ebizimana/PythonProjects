import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.data = []

    # Get Data
    def get_data(self):
        get_url = "https://api.sheety.co/6361c8e40a3faddb4f9fe508a668cead/flightDeals/prices"
        response = requests.get(url=get_url)
        response.raise_for_status()
        sheet_data = response.json()
        self.data = sheet_data["prices"]

    # Edit the IATA codes
    def fill_in_codes(self, iata_code, row_number):
        put_url = "https://api.sheety.co/6361c8e40a3faddb4f9fe508a668cead/flightDeals/prices"
        params = {
            "price": {
                "iataCode": iata_code,
                "id": row_number
            }
        }
        # Update the data list
        for entry in self.data:
            if entry["id"] == row_number:
                entry["iataCode"] = iata_code

        # Update the sheet
        requests.put(url=f"{put_url}/{params['price']['id']}", json=params)




