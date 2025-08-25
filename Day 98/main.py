from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import smtplib
from email.mime.text import MIMEText
import time


USERNAME = "your_username"
PASSWORD = "your_password"
LOGIN_URL = "https://university-portal.com/login"
ANNOUNCEMENTS_URL = "https://university-portal.com/announcements"


EMAIL_SENDER = "youremail@gmail.com"
EMAIL_PASSWORD = "your_app_password"
EMAIL_RECEIVER = "youremail@gmail.com"


options = Options()
options.add_argument("--headless")
service = Service("/path/to/chromedriver")
driver = webdriver.Chrome(service=service, options=options)


def login():
    driver.get(LOGIN_URL)
    time.sleep(2)

    driver.find_element(By.ID, "username").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD + Keys.RETURN)
    time.sleep(3)


def check_announcements():
    driver.get(ANNOUNCEMENTS_URL)
    time.sleep(3)

    announcements = driver.find_elements(By.CLASS_NAME, "announcement-title")
    titles = [a.text for a in announcements]
    return titles


def send_email(message):
    msg = MIMEText(message)
    msg["Subject"] = "New University Announcement"
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())


login()
titles = check_announcements()

if titles:
    message = "Here are the latest announcements:\n\n" + "\n".join(titles)
    send_email(message)
    print("✅ Email sent with new announcements!")
else:
    print("ℹ️ No new announcements found.")

driver.quit()
