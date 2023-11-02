# Author: Elie Bizimana
# Created On: July 21, 2023 - Friday
# Finished Project: July 21, 2023 - Friday
# Project Name: Twitter Complaint Bot Project

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "/Users/eliebizimana/Downloads/Software/chromedriver"
TWITTER_EMAIL = "v8mn8qwgjq@privaterelay.appleid.com"
TWITTER_USERNAME = "@bizimana_e31434"
TWITTER_PASSWORD = "Zudpe7-xuxzox-tesmoq"


class InternetSpeedTwitterBot:
    def __init__(self, chrome_driver_path):
        # Initialize the ChromeService with the chromedriver path
        self.service = ChromeService(executable_path=CHROME_DRIVER_PATH)
        # Use the service to create the Chrome WebDriver
        self.driver = webdriver.Chrome(service=self.service)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")
        time.sleep(3)
        go_button = self.driver.find_element(by=By.XPATH, value='/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_button.click()

        time.sleep(50)
        self.up = self.driver.find_element(by=By.XPATH, value='/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/'
                                                              'div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]'
                                                              '/span').text
        self.down = self.driver.find_element(by=By.XPATH, value='/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]'
                                                                '/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/'
                                                                'div[2]/span').text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login?redirect_after_login=%2F%3Flang%3Den")

        time.sleep(1)
        email = self.driver.find_element(by=By.XPATH, value='/html/body/div/div/div/div[1]/div/div/div/div/div/div/'
                                                               'div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/'
                                                               'label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div/div/div[1]/div/div/div/div/div/'
                                                    'div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/'
                                                    'div[6]/div').click()
        time.sleep(1)

        username = self.driver.find_element(by=By.XPATH, value='/html/body/div/div/div/div[1]/div/div/div/div/div/div/'
                                                               'div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/'
                                                               'label/div/div[2]/div/input')
        username.send_keys(TWITTER_USERNAME)
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/'
                                                    'div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div').click()
        time.sleep(1)
        password = self.driver.find_element(by=By.XPATH, value='/html/body/div/div/div/div[1]/div/div/div/div/div/div/'
                                                               'div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/'
                                                               'div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/"
                                                    "div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/"
                                                    "div/div").click()
        time.sleep(3)
        message = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]'
                                                              '/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]'
                                                              '/div/div/div/div/div/div/div/div/div/div/label/div[1]'
                                                              '/div/div/div/div/div/div[2]/div/div/div/div/span')
        message.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay "
                          f"for 150down/100up")

        self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div'
                                                    '/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div'
                                                    '/div[2]/div[3]').click()

        time.sleep(2)
        self.driver.quit()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
