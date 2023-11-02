from datetime import datetime, timedelta


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self.departure_airport_code = "LON"
        self.arrival_airport_code = ""

    def set_flight_dates(self):
        # Get the date for tomorrow
        tomorrow = datetime.today() + timedelta(days=1)
        day = tomorrow.strftime("%d")
        month = int(tomorrow.strftime("%m"))
        year = tomorrow.strftime("%Y")
        tomorrow = f"{day}/{month}/{year}"

        # Get the date for 6 months from now
        month = month + 6
        if month > 12:
            month = month % 6
            year = int(year) + 1
        six_months_from_now = f"{1}/{month}/{year}"
        return tomorrow, six_months_from_now

    def search_params(self, city_from, city_to, cities_data):
        # Find Dates
        dates = self.set_flight_dates()
        date_from = dates[0]
        date_to = dates[1]

        # Find City Codes
        for entry in cities_data:
            if city_from == entry["city"]:
                self.departure_airport_code = entry["iataCode"]
            if city_to == entry["city"]:
                self.arrival_airport_code = entry["iataCode"]

        search_params = {
            "fly_from": self.departure_airport_code,
            "fly_to": self.arrival_airport_code,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 1,
            # "curr": "USD" # for my own
            "curr": "GBP"  # To complete the project
        }
        return search_params
