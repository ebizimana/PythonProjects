"""
Name: Call to worship Project
Description:
 - A monthly automotive email that is sent out to all alumni of MMS.
 - Asking them to follow a link to a website
Date Created: Wed September 28, 2022
"""

import smtplib
import pandas
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Prepare the body of the message
msg = """ Hey family 
I hope you are doing well, please join our family by holding a date to record a video for call to worship. 
to know more about it email this person.
"""
# Get all list of emails
file = pandas.read_csv("all_emails.csv")
file_data = file.to_dict(orient="records")

# Send an email to all
my_email = "elieb7842@gmail.com"
password = "dwsovuqytspgbrlo"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     for entry in file_data:
#         time.sleep(5)
#         connection.sendmail(to_addrs=entry["email"], from_addr=my_email, msg=msg.as_string())

# Send and emil to me
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(to_addrs="ebizimana@mmskids.org", from_addr=my_email, msg=msg)

