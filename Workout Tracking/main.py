import requests
from datetime import datetime

APP_ID = "b8c1b68d"
API_KEY = "30844f8c87df2b6c4365e2f224c82dc2	"
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_ENDPOINT = "https://api.sheety.co/6361c8e40a3faddb4f9fe508a668cead/myWorkouts/sheet1"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": input("Tell me which exercises you did: "),
    "gender": "male",
    "weight_kg": 68,
    "height_cm": 190.5,
    "age": 27
}

response = requests.post(url=NUTRITIONIX_ENDPOINT, json=parameters, headers=headers)
data = response.json()

# Get the date and time
date = datetime.now().strftime("%x")
time = datetime.now().strftime("%X")

# Saving Data into google sheets
sheety_headers = {
    "Authorization": "Basic ZWJpemltYW5hOm15V29ya291dHNzcHJlYWRzaGVldA=="
}

for entry in data["exercises"]:
    exercise = entry["name"]
    duration = entry["duration_min"]
    calories = entry["nf_calories"]
    sheety_params = {
        "sheet1": {
            "date": date,
            "time": time,
            "exercise": exercise.title(),
            "duration": duration,
            "calories": calories
        }
    }
    sheety_resp = requests.post(url=SHEETY_ENDPOINT, json=sheety_params, headers=sheety_headers)
    print(sheety_resp.text)

