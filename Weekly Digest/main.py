# Made by: Elie B.
# Created: October 10, 2023,
# Last Updated by:

import pandas as pd
import time
import random
import smtplib
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Constant Variables
chrome_driver_path = "/Users/eliebizimana/Downloads/Software/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver_path))
my_email = "elieb7842@gmail.com"
password = "nzkwmbwcygggoygx"


# Get article from Got Questions
def got_questions():
    url = "https://www.gotquestions.net/admin/BackendSubmit/RandomPage?websiteid=1"
    driver.get(url=url)

    article_title = driver.find_element(by=By.XPATH, value="/html/body/main/section[1]/div/h1/span").text
    article_url = driver.current_url
    return article_title, article_url


# Get article from Axis
def culture_translator():
    url = "https://axis.org/resource-category/culture-translator/"
    driver.get(url=url)

    articles = random.sample(driver.find_elements(by=By.CLASS_NAME, value="m-resource-cards__item"), 3)
    selected_articles = []
    for article in articles:
        article_full_text = article.text.split('\n')
        article_text = article_full_text[1]
        article_date = article_full_text[2]
        article_href = article.find_element(by=By.TAG_NAME, value="a").get_attribute("href")
        selected_articles.append({"article_text": article_text,
                                  "article_date": article_date,
                                  "article_href": article_href})

    return selected_articles


# Function to send an email
def send_email(recipient, subject, message):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'html'))

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient,
            msg=msg.as_string()
        )


# Get events happening around
def get_events():
    # , "pikeville"
    # cities = ["grundy", "bristol", "abingdon", "tazewell"]
    cities = ["bristol"]

    all_cities_events = []

    for city in cities:
        city_url = f"https://www.eventbrite.com/d/va--{city}/all-events/"
        # driver.implicitly_wait(10)
        driver.get(url=city_url)

        # Get events details
        # events_section_tag = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, ".search-main-content__events-list")))
        # parent_div = events_section_tag.find_elements(by=By.CSS_SELECTOR, value="Stack_root__1ksk7")
        # child_elements = parent_div.find_elements(by=By.CSS_SELECTOR, value="*")
        # print(child_elements)

        events_section_tag = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".search-main-content__events-list")))

        # Find the parent div with the specified class
        parent_div = events_section_tag.find_element(By.CSS_SELECTOR, ".Stack_root__1ksk7")

        # Find immediate child elements of the parent div
        child_elements = parent_div.find_elements(By.CSS_SELECTOR, "*")

        # Now 'child_elements' contains a list of immediate child elements of the parent div
        for i in range(len(child_elements)):
            print(i)

        # events_link_tag = events_section_tag.find_elements(by=By.CSS_SELECTOR,
        #                                                    value=".Stack_root__1ksk7")
        # events_date_tag = events_section_tag.find_elements(by=By.CSS_SELECTOR,
        #                                                    value=".event-card__clamp-line--one")
        # events_location_tag = events_section_tag.find_elements(by=By.CSS_SELECTOR,
        #                                                        value=".eds-g-cell div.card-text--truncated__one")
        # events_price_tag = events_section_tag.find_elements(by=By.CSS_SELECTOR,
        #                                                     value=".Stack_root__1ksk7 div.discover-horizontal-event-card__price-wrapper"
        #                                                           ":nth-child(2)")
        events_name_tag = events_section_tag.find_elements(by=By.CSS_SELECTOR,
                                                           value=".event-card__clamp-line--two")

        # Get the individual lists
        # events_links = [link.get_attribute("href") for link in events_link_tag]
        # events_names = [name.text for name in events_name_tag]
        # events_dates = [date.text for date in events_date_tag]
        # events_locations = [location.text for location in events_location_tag]
        # events_prices = [price.text for price in events_price_tag]

        # Create a singular list with all events
        # events = []
        # for index in range(8):
        #     try:
        #         event = {
        #             "name": events_names[index],
        #             "date": events_dates[index],
        #             # "location": events_locations[index],
        #             # "price": events_prices[index],
        #             "link": events_links[index]
        #         }
        #         events.append(event)
        #     except IndexError:
        #         pass
        #
        # all_cities_events = [{
        #     "city_name": city,
        #     "city_events": events
        # }]
        # print(all_cities_events)


def main():
    question_title, question_url = got_questions()
    articles = culture_translator()
    print(articles)

    # Prepare the email message
    file = pd.read_csv("/Users/eliebizimana/PycharmProjects/Weekly Digest/all_emails.csv")
    file_data = file.to_dict(orient="records")

    for entry in file_data:
        time.sleep(2)
        recipient_email = str(entry["email"])
        recipient_name = entry["name"]
        email_message = f'''
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
                        hr {{
                            width: 50%
                        }}
                    </style>
                </head>
                <body>
                    <div class="container">
                        <h2>Dear {recipient_name}</h2>

                        <h4 class="mt-6">Question of the day:</h4>
                            <p> 
                                {question_title} 
                                <a href="{question_url}"> Link </a>
                            </p>
                            
                        
                        <hr>

                        <h4 class="mt-6">Articles of the day:</h4>
                        <ul>
                            <li>
                                <strong> {articles[0]["article_text"]} </strong>
                                <i> {articles[0]["article_date"]} </i>
                                <a href="{articles[0]["article_href"]}"> Link </a>
                            </li>
                            <li>
                                <strong> {articles[1]["article_text"]} </strong>
                                <i> {articles[1]["article_date"]} </i>
                                <a href="{articles[1]["article_href"]}"> Link </a>
                            </li>
                            <li>
                                <strong> {articles[2]["article_text"]} </strong>
                                <i> {articles[2]["article_date"]} </i>
                                <a href="{articles[2]["article_href"]}"> Link </a>
                            </li>
                        </ul>

                        <p>He Lives in You.</p>
                    </div>
                </body>
                </html>
                '''
        send_email(recipient_email, 'Weekly Digest', email_message)


if __name__ == "__main__":
    main()
    print("Emails sent successfully.")
