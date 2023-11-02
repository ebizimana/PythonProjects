#Created by: Elie Bizimana 10/28/2022
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

ACCOUNT_EMAIL = "ebizimana@liberty.edu"
ACCOUNT_PASSWORD = "kyzge6-kYwpuq-cofbaj"

# Open Linkedin
chrome_driver_path = "/Users/eliebizimana/Downloads/Software/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.get("https://www.linkedin.com/")

# Automatically log in
driver.find_element(by=By.XPATH, value="/html/body/nav/div/a[2]").click()
driver.find_element(by=By.ID, value="username").send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

# Search for job
search_bar = driver.find_element(by=By.XPATH, value='//*[@id="global-nav-typeahead"]/input')
search_bar.send_keys("Python Developer")
search_bar.send_keys(Keys.ENTER)
time.sleep(5)
driver.find_element(by=By.XPATH, value='//*[@id="search-reusables__filters-bar"]/ul/li[1]/button').click()
time.sleep(5)

# Save a job
driver.find_element(by=By.XPATH, value='//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]'
                                       '/div/div[1]/div[1]/div[3]/div/button').click()


# Couldn't Implement
# How to select a "Easy Apply" button
# driver.find_element(by=By.XPATH, value='//div[@aria-label="Easy Apply filter."]'
#                                        '/div[@class="search-reusables__filter-pill-button"]'
#                                        '[text()="Easy Apply"]').click()
