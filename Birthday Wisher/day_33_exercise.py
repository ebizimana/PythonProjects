import smtplib
import datetime as dt
from random import choice

# Get the day of the week
now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    # Open File
    with open("quotes.txt", mode="r") as file:
        quotes = file.readlines()
        quote = choice(quotes)

    # Email quote to self
    my_email = "elieb7842@gmail.com"
    password = "pudnyw-9Vygzi-zywmys"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject: Monday Quote\n\n{quote}")





import smtplib

# my_email = "elieb7842@gmail.com"
# password = "pudnyw-9Vygzi-zywmys"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="bizimana.elie@yahoo.com",
#                         msg="Subject:Hello\n\nThis is the body of my email.")

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
#
# date_of_birth = dt.datetime(year=1995, month=3, day=3)

