import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


chrome_driver_path = "/Users/eliebizimana/Downloads/Software/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.get("http://orteil.dashnet.org/experiments/cookie/")


def reward(money):
    if 15 <= money < 111:
        driver.find_element(by=By.ID, value="buyCursor").click()
    elif 111 <= money < 500:
        driver.find_element(by=By.ID, value="buyGrandma").click()
    elif 500 <= money < 2000:
        driver.find_element(by=By.ID, value="buyFactory").click()
    elif 2000 <= money < 7000:
        driver.find_element(by=By.ID, value="buyMine").click()
    elif 7000 <= money < 50000:
        driver.find_element(by=By.ID, value="buyShipment").click()
    elif 50000 <= money < 1000000:
        driver.find_element(by=By.ID, value="buyAlchemy lab").click()
    elif 1000000 <= money < 123456789:
        driver.find_element(by=By.ID, value="buyPortal").click()
    else:
        driver.find_element(by=By.ID, value="buyTime machine").click()


cookie = driver.find_element(by=By.CSS_SELECTOR, value="#cookie")
timeout = time.time() + 5
while True:
    cookie.click()

    if time.time() > timeout:
        money_now = int(driver.find_element(by=By.CSS_SELECTOR, value="#money").text.replace(",", ""))
        reward(money_now)
        timeout = time.time() + 5








