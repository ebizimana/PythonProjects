# Made by: Elie B.
# Created:
# Last Updated by: Sept 30, 2023

import time
import random
import smtplib
import requests
import pandas as pd
from gphotospy import authorize
from gphotospy.album import Album
from gphotospy.media import Media
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


# Configuration
my_email = "elieb7842@gmail.com"
password = "nzkwmbwcygggoygx"
sheety_url = "https://api.sheety.co/6361c8e40a3faddb4f9fe508a668cead/prayerList/sheet1"
sheety_headers = {"Authorization": "Bearer prayerList"}


# Function to fetch random pictures
def fetch_random_pictures():
    CLIENT_SECRET_FILE = "gphoto_oauth.json"
    service = authorize.init(CLIENT_SECRET_FILE)

    album_manager = Album(service)
    album_iterator = album_manager.list()
    first_album = next(album_iterator)
    first_album_id = first_album.get("id")

    media_manager = Media(service)
    album_media_list = media_manager.search_album(first_album_id)
    album_media = list(album_media_list)

    random_pictures = [random.choice(album_media) for _ in range(3)]
    picture_urls = [pic.get("baseUrl") for pic in random_pictures]

    return picture_urls


# Function to get the verse of the day
def get_verse_of_the_day():
    url = "https://beta.ourmanna.com/api/v1/get?format=json&order=daily"
    headers = {"Accept": "application/json"}
    response = requests.get(url=url, headers=headers)
    data = response.json()["verse"]["details"]
    verse = data["text"]
    reference = data["reference"]
    return verse, reference


# Function to get the prayers of the day
def fetch_prayers():
    prayer_responses = requests.get(url=sheety_url, headers=sheety_headers).json()["sheet1"]

    # Initialize variables
    starting_id = None
    stopping_id = None
    prayers_of_day = []

    # Find the starting and stopping IDs
    for prayer in prayer_responses:
        if prayer.get("count") == "start":
            starting_id = prayer["id"]
            stopping_id = starting_id + 2

    # Handle the case where "start" is at the end of the list
    if stopping_id >= len(prayer_responses):
        delete_it = starting_id
        starting_id = prayer_responses[0]["id"]
        stopping_id = starting_id + 2
        update_sheety(delete_it,stopping_id)


    #Populate prayers_of_day with the selected prayers
    for prayer in prayer_responses:
        if starting_id <= prayer["id"] <= stopping_id:
            if not prayer.get("name"):
                prayer["name"] = "Anonymous"
            prayers_of_day.append(prayer)

    update_sheety(starting_id,stopping_id)

    return prayers_of_day


# Function to update Sheety
def update_sheety(starting_id,stopping_id):
    # Edit cells to remove and add "start"
    data_remove = {"sheet1": {"count": ""}}
    endpoint_remove = f"{sheety_url}/{starting_id}"
    requests.put(url=endpoint_remove, json=data_remove, headers=sheety_headers)

    data_add = {"sheet1": {"count": "start"}}
    endpoint_add = f"{sheety_url}/{stopping_id}"
    requests.put(url=endpoint_add, json=data_add, headers=sheety_headers)


# Function to get the quote of the day
def get_quote_of_the_day():
    quote_url = "https://zenquotes.io/api/today/"
    quote_response = requests.get(quote_url)
    quote = quote_response.json()[0]['h']
    return quote


# Function to prepare email message
def email_message(recipient_name,image_urls,verse,reference,prayers_of_day,quote):
    msg = MIMEMultipart()
    msg['Subject'] = 'Verse Of The Day'
    msg['From'] = my_email
    msg['To'] = recipient_name

    html_content = f'''
    <!DOCTYPE html>
            <html>
            <head>
                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
                <style>
                    body {{
                        font-family: 'Times New Roman', Times, serif;
                    }}

                    h4 {{
                        text-decoration: underline; /* Underline all h4 elements */
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h2>Dear {recipient_name}</h2>

                    <h4 class="mt-4">Pictures of the day:</h4>
                    <div class="row">
                        <div class="col-md-4">
                            <div class="image-container">
                                <img src="cid:image0" class="img-fluid" style="max-width: 100%; height: auto;">
                            </div>
                        </div>
                        <div class="col-md-4">
                            <div class="image-container">
                                <img src="cid:image1" class="img-fluid" style="max-width: 100%; height: auto;">
                            </div>
                        </div>
                        <div class="col-md-4">
                            <div class="image-container">
                                <img src="cid:image2" class="img-fluid" style="max-width: 100%; height: auto;">
                            </div>
                        </div>
                    </div>

                    <h4 class="mt-4">Verse of the day:</h4>
                    <p>{verse}</p>
                    <p><i>{reference}</i></p>

                    <h4 class="mt-4">Prayers of the day:</h4>
                    <ul>
                        <li><i>{prayers_of_day[0].get("name", "Anonymous")}</i>: {prayers_of_day[0]["prayerRequest"]}</li>
                        <li><i>{prayers_of_day[1].get("name", "Anonymous")}</i>: {prayers_of_day[1]["prayerRequest"]}</li>
                        <li><i>{prayers_of_day[2].get("name", "Anonymous")}</i>: {prayers_of_day[2]["prayerRequest"]}</li>
                    </ul>

                    <h4 class="mt-4">Quote of the day:</h4>
                    <p>{quote}</p>

                    <p>He Lives in You.</p>
                </div>
            </body>
            </html>
    '''

    # Attach the HTML content
    html_part = MIMEText(html_content, 'html')
    msg.attach(html_part)

    # Download and attach the images
    for i, image_url in enumerate(image_urls):
        response = requests.get(image_url)
        if response.status_code == 200:
            image_data = response.content
            image_part = MIMEImage(image_data)
            image_part.add_header('Content-ID', f'<image{i+1}>')  # Add Content-ID for inline image
            msg.attach(image_part)

    return msg


# Function to send an email
def send_email(recipient, message):
    # Set up the SMTP server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    with smtplib.SMTP(smtp_server, smtp_port) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)

        message = message.as_string()

        # Send the email
        connection.sendmail(from_addr=my_email, to_addrs=recipient, msg=message)


# Main function
def main():
    # Send the whole campus
    file = pd.read_csv("all_emails.csv")
    # Test purposes
    # file = pd.read_csv("/home/ebizimana/verse_of_day/Test.csv")
    file_data = file.to_dict(orient="records")

    image_urls = fetch_random_pictures()  # Fetch the images
    verse, reference = get_verse_of_the_day()  # Fetch the verse
    prayers_of_day = fetch_prayers()  # Fetch prayers
    quote = get_quote_of_the_day()  # Fetch the quote

    # Prepare the email message
    for entry in file_data:
        time.sleep(2)
        recipient_email = str(entry["email"])
        recipient_name = entry["name"]
        message = email_message(recipient_name,image_urls,verse,reference,prayers_of_day,quote)
        send_email(recipient_email, message)

if __name__ == "__main__":
    main()
    print("Emails sent successfully.")
