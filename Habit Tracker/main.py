import requests
from datetime import datetime

USERNAME = "elieb"
TOKEN = "haiejopadnlaeiword"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
headers = {"X-USER-TOKEN": TOKEN}
graph_parameters = {
    "id": GRAPH_ID,
    "name": "Daniel Plan",
    "unit": "Times",
    "type": "int",
    "color": "shibafu"
}
# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now().strftime("%Y%m%d")

pixel_parameters = {
    "date": today,
    "quantity": input("How many times did you pray today? ")
}
response = requests.post(url=pixel_endpoint, json=pixel_parameters, headers=headers)
print(response.text)

pixel_update_endpoint = f"{pixel_endpoint}/20220322"
pixel_update_parameters = {
    "quantity": "7"
}
# response = requests.put(url=pixel_update_endpoint, json=pixel_update_parameters, headers=headers)
# print(response.text)

pixel_delete_endpoint = f"{pixel_endpoint}/20200322"
# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)
