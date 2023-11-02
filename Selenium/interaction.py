from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/eliebizimana/Downloads/Software/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver_path))

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# articles_num = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
# print(articles_num.text)

# How to click on links
# articles_num.click()
# all_portals = driver.find_element(by=By.LINK_TEXT, value="All portals")

# How to type
# search = driver.find_element(by=By.NAME, value="search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

# CHALLENGE
driver.get("http://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(by=By.NAME, value="fName")
last_name = driver.find_element(by=By.NAME, value="lName")
email = driver.find_element(by=By.NAME, value="email")
search_btn = driver.find_element(by=By.CSS_SELECTOR, value=".btn")

first_name.send_keys("Elie")
last_name.send_keys("B.")
email.send_keys("a@b.c")
search_btn.click()



