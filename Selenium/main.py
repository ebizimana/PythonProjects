from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/eliebizimana/Downloads/Software/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver_path))

driver.get("https://www.python.org")
# driver.find_element_by_id("priceblock_ourpice")
# driver.find_element_by_name("q")
# driver.find_element_by_css_selector(".documentation-widget a")
# driver.find_element_by_class_name("")
# driver.find_element_by_xpath("")

event_times = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }
print(events)
driver.quit()


