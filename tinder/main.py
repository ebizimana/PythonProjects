# Made by Elie Bizimana
# Date: Nov 22, 2022
# Application Name: Auto Tinder Swiping Bot


from time import sleep

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import *


# Global Variables
ACCOUNT_EMAIL = "ebizimana@liberty.edu"
ACCOUNT_PASSWORD = "kosto0-synBez-garxav"

# Open Tinder
chrome_driver_path = "/Users/eliebizimana/Downloads/Software/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.get("https://www.tinder.com/")

# Automatically Login
sleep(2)
driver.find_element(by=By.LINK_TEXT, value='Log in').click()
sleep(2)
driver.find_element(by=By.XPATH, value='/html/body/div[2]/main/div/div[1]/div/div/div[3]/span/div[2]/button').click()
sleep(2)

facebook_login_window = driver.window_handles[1]
driver.switch_to.window(facebook_login_window)
email = driver.find_element(by=By.ID, value='email')
password = driver.find_element(by=By.ID, value='pass')
email.send_keys(ACCOUNT_EMAIL)
password.send_keys(ACCOUNT_PASSWORD)
driver.find_element(by=By.NAME, value='login').click()
sleep(2)
driver.switch_to.window(driver.window_handles[0])

# Dismiss all requests
sleep(5)
driver.find_element(by=By.XPATH, value='/html/body/div[2]/main/div/div/div/div[3]/button[1]').click()
driver.find_element(by=By.XPATH, value='/html/body/div[2]/main/div/div/div/div[3]/button[2]').click()
driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[2]/div/div/div[1]/div[2]/button').click()

# Starting liking
sleep(7)
driver.find_element(by=By.XPATH, value='/html/body/div[2]/main/div/div[2]').click()
sleep(2)
like_button = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/'
                                                     'div[1]/div/div[3]/div/div[4]/button')
for _ in range(99):
    try:
        sleep(2)
        like_button.click()
    except ElementClickInterceptedException:
        try:
            sleep(2)
            driver.find_element(by=By.XPATH, value='/html/body/div[2]/main/div').click()
        except NoSuchElementException:
            continue






