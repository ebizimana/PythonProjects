import requests
from twilio.rest import Client

# ---------------------------- CONSTANTS ------------------------------- #
# WEATHER CONSTANTS
API_KEY = "d329753ac371af0ee854511b39692f5a"
MY_LAT = 37.280472
MY_LNG = -82.089142
PARAMETERS = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "exclude": "current,minutely,daily,alerts",
    "appid": API_KEY
}
URL = f"https://api.openweathermap.org/data/2.5/onecall"

# TWILIO CONSTANTS
account_sid = "AC7f7ede5024d11fe87a5cb51efd48a838"
auth_token = "a6909300e3f809c43ef0a2e84cfd8439"


response = requests.get(url=URL, params=PARAMETERS)
response.raise_for_status()
weather_data = response.json()

# My Version
# hourly = weather_data["hourly"]
# for index, hour in enumerate(hourly):
#     if index <= 11:
#         hourly_weather = hour["weather"]
#         for weather in hourly_weather:
#             weather_id = weather["id"]
#             if weather_id < 700:
#                 print("Bring an Umbrella")

# Dr. Angela Yu Version
will_rain = False
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an Umbrella")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today, bring an umbrella",
        from_='+12182766209',
        to='+12763127011'
    )
    print(message.status)
