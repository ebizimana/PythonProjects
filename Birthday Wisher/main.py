# 1. Update the birthdays.csv
import datetime as dt
import pandas
import smtplib
from random import choice, randint

# Get the date for today
now = dt.datetime.now()
month = now.month
day = now.day

# Get the date in the file
file = pandas.read_csv("birthdays.csv")
data = file.to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv
for entry in data:
    if month == entry['month'] and day == entry['day']:
        # 3a. If step 2 is true, pick a random letter from letter templates
        pick_number = randint(1, 3)
        with open(f"letter_templates/letter_{pick_number}.txt") as file:
            letter = file.read()
            # 3b. Replace the [NAME] with the person's actual name from birthdays.csv
            letter = letter.replace("[NAME]", entry['name'])

        # 4. Send the letter generated in step 3 to that person's email address.
        birthday_person = entry['email']
        my_email = "elieb7842@gmail.com"
        password = "pudnyw-9Vygzi-zywmys"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=birthday_person,
                                msg=f"Subject:Happy Birthday\n\n{letter}")
