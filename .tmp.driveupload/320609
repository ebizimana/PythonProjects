# This file will need to use the DataManager, FlightSearch, FlightData, NotificationManager classes to achieve
# the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

# CLASS OBJECTS
sheet_data = DataManager()
search_flight = FlightSearch()
notify = NotificationManager()

ORIGIN_CITY = "London"

sheet_data.get_data()
for entry in sheet_data.data:
    # Get the city code, update the sheet
    code = search_flight.search_iata(entry["city"])
    sheet_data.fill_in_codes(code, entry["id"])
    info = search_flight.flight_info(ORIGIN_CITY, entry["city"], sheet_data.data)

    try:
        if search_flight.lowest_price(city_to=entry["city"], cities_data=sheet_data.data, price=info['price']):
            # notify.send_text(flight_info=info)
            notify.send_email(flight_info=info)
        else:
            print(f"{info['city_to']}: £{info['price']}. No cheap flight found.")
    except TypeError:
        pass
