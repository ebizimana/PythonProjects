from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_driver_path = "/Users/eliebizimana/Downloads/Software/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver_path))

# , "pikeville"
cities = ["grundy", "bristol", "abingdon", "tazewell"]
# cities = ["grundy"]

all_cities_events = []

for city in cities:
    city_url = f"https://www.eventbrite.com/d/va--{city}/events/"
    # driver.implicitly_wait(10)
    driver.get(url=city_url)

    # Get events details
    events_section_tag = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".small_city_fallback--bucket-wrapper")))
    events_link_tag = events_section_tag.find_elements(by=By.CSS_SELECTOR, value=".eds-g-cell a.eds-event-card-content__action-link")
    events_date_tag = events_section_tag.find_elements(by=By.CSS_SELECTOR, value=".eds-g-cell div.eds-event-card-content__sub-title")
    events_location_tag = events_section_tag.find_elements(by=By.CSS_SELECTOR, value=".eds-g-cell div.card-text--truncated__one")
    events_price_tag = events_section_tag.find_elements(by=By.CSS_SELECTOR, value=".eds-g-cell div.eds-l-mar-top-1:nth-child(2)")
    events_name_tag = events_section_tag.find_elements(by=By.CSS_SELECTOR, value=".eds-g-cell div.eds-event-card__formatted-name--is-clamped")

    # Get the individual lists
    events_links = [link.get_attribute("href") for link in events_link_tag]
    events_names = [name.text for name in events_name_tag]
    events_dates = [date.text for date in events_date_tag]
    events_locations = [location.text for location in events_location_tag]
    events_prices = [price.text for price in events_price_tag]

    # Create a singular list with all events
    events = []
    for index in range(8):
        try:
            event = {
                "name": events_names[index],
                "date": events_dates[index],
                "location": events_locations[index],
                "price": events_prices[index],
                "link": events_links[index]
            }
            events.append(event)
        except IndexError:
            pass

    all_cities_events = [{
        "city_name": city,
        "city_events": events
    }]
    print(all_cities_events)







