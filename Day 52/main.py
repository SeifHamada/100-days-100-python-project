import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
import time

load_dotenv()
SIMILAR_ACCOUNT = os.getenv("SIMILAR_ACCOUNT")
MAIL = os.getenv("MAIL")
PASSWORD = os.getenv("PASSWORD")
IG_LINK = "https://www.instagram.com/accounts/login/"

class InstaFollowers:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
    
    def login(self):
        self.driver.get(IG_LINK)
        time.sleep(5)
        email = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
        email.send_keys(MAIL)
        password = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
        password.send_keys(PASSWORD)
        next = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div[1]/div[3]')
        next.click()
        time.sleep(5)
        not_now = self.driver.find_element(By.XPATH, value="//*[contains(text(), 'Not now')]")
        not_now.click()


    def find_followers(self):
        self.driver.get_link(SIMILAR_ACCOUNT)
        time.sleep(5)
        followers = self.driver.find_element(By.XPATH, value='//*[@id="mount_0_0_pV"]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a/span')
        for _ in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.XPATH, value='//*[@id="scrollview"]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[3]/div/button')

        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)

            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="/html/body/div[8]/div[1]/div/div[2]/div/div/div/div/div/div/button[2]")
                cancel_button.click()

bot = InstaFollowers()
bot.login()
bot.find_followers()
bot.follow()
