import time
import requests
import smtplib
from datetime import datetime

MY_LAT = 37.280472
MY_LNG = -82.089142
MY_EMAIL = "elieb7842@gmail.com"
PASSWORD = "pudnyw-9Vygzi-zywmys"


# if the ISS is close to my current position
def close_by():
    # ISS POSITION
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    # +5 or -5 degree to my location
    min_lng = int(MY_LNG - 5)
    max_lng = int(MY_LNG + 5)
    lng_range = range(min_lng, max_lng)

    min_lat = int(MY_LAT - 5)
    max_lat = int(MY_LAT + 5)
    lat_range = range(min_lat, max_lat)

    if longitude in lng_range and latitude in lat_range:
        return True


# MY POSITION
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    # OUTSIDE DARK
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    hour = datetime.now().hour

    # and it is currently dark
    if hour >= sunset or hour <= sunrise:
        return True


while True:
    time.sleep(60)
    # If ISS is close by and it's nighttime
    if close_by() and is_night():
        with smtplib.SMTP("smtp.google.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg="Subject: Look up for ISS\n\nThe ISS is above")

