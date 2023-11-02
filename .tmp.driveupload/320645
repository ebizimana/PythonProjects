from twilio.rest import Client
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import requests


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = "AC7f7ede5024d11fe87a5cb51efd48a838"
        self.auth_token = "a6909300e3f809c43ef0a2e84cfd8439"

    def send_text(self, flight_info):
        text = f"flight from {flight_info['city_from']}-{flight_info['fly_from']} to {flight_info['city_to']}-" \
               f"{flight_info['fly_to']} leaving on {flight_info['out_date']} coming back in " \
               f"{flight_info['city_from']} on {flight_info['return_date']} " \
               f"is available for only ${flight_info['price']}"
        print(text)
        client = Client(self.account_sid, self.auth_token)
        message = client.messages \
            .create(body=text,
                    from_='+12182766209',
                    to='+12763127011')
        print(message.status)

    def send_email(self, flight_info):
        # Email Content
        email_body = f"flight from {flight_info['city_from']}-{flight_info['fly_from']} to {flight_info['city_to']}-" \
                     f"{flight_info['fly_to']} leaving on {flight_info['out_date']} coming back in " \
                     f"{flight_info['city_from']} on {flight_info['return_date']} " \
                     f"is available for only ${flight_info['price']}"

        url = f"https://www.google.co.uk/flights?hl=en#fIt={flight_info['fly_from']}.{flight_info['fly_to']}." \
              f"{flight_info['out_date']}*{flight_info['fly_to']}." \
              f"{flight_info['fly_from']}.{flight_info['return_date']}"

        msg = MIMEMultipart()
        msg['Subject'] = 'New Low Price Flight!'
        text = MIMEText(f"{email_body}\n {url}")
        msg.attach(text)

        # Send Email to myself
        my_email = "elieb7842@gmail.com"
        password = "pudnyw-9Vygzi-zywmys"

        # Send Email to the clients
        # Get Clients Emails
        get_url = "https://api.sheety.co/6361c8e40a3faddb4f9fe508a668cead/flightDeals/users"
        response = requests.get(url=get_url)
        response.raise_for_status()
        data = response.json()
        emails = data['users']

        # Send email to clients
        for entry in emails:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(to_addrs=entry['email'], from_addr=my_email, msg=msg.as_string())
