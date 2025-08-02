import os
from dotenv import load_dotenv
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()
PROMISED_UP = os.getenv("PROMISED_UP")
PROMISED_DOWN = os.getenv("PROMISED_DOWN")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0
    
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        time.sleep(10)

        go = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a")
        go.click()

        time.sleep(60)
        self.up = self.driver.find_element(By.XPATH, value='//span[@class="result-data-large number result-data-value upload-speed"]').text
        self.down = self.driver.find_element(By.XPATH, value = '//span[@class="result-data-large number result-data-value download-speed"]').text

    
    def tweet_at_provide(self):
        self.driver.get("https://twitter.com/login")

        time.sleep(10)
        email = self.driver.find_element(By.XPATH, value='//input[@name="text" and @type="text"]')
        next = self.driver.find_element(By.XPATH, value= '//span[text()="Next"]/ancestor::button')
        next.click()
        password = self.driver.find_element(By.XPATH, value='//input[@name="password" and @type="password"]')

        email.send_keys(EMAIL)
        password.send_keys(PASSWORD)
        time.sleep(5)
        password.send_keys(Keys.ENTER)

        time.sleep(10)
        tweet_compose = self.driver.find_element(By.XPATH, value='//svg[@aria-hidden="true" and contains(@class, "r-yyyyoo")]')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element(By.XPATH, value='<button aria-disabled="true" disabled="" role="button" tabindex="-1" class="css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-15ysp7h r-4wgw6l r-3pj75a r-o7ynqc r-6416eg r-icoktb r-1ny4l3l" data-testid="tweetButton" type="button" style="background-color: rgb(29, 155, 240); border-color: rgba(0, 0, 0, 0);"><div dir="ltr" class="css-146c3p1 r-bcqeeo r-qvutc0 r-37j5jr r-q4m81j r-a023e6 r-rjixqe r-b88u0q r-1awozwy r-6koalj r-18u37iz r-16y2uox r-1777fci" style="color: rgb(255, 255, 255);"><span class="css-1jxf684 r-dnmrzs r-1udh08x r-1udbk01 r-3s2u2q r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3 r-1b43r93 r-1cwl3u0"><span class="css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3">Post</span></span></div></button>')
        tweet_button.click()

        time.sleep(5)
        self.driver.quit()

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provide()
