from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
PHONE = os.getenv("PHONE")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4266625322&f_LF=f_AL&f_WT=2&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true")

sign_in_button = driver.find_element(By.XPATH, value='//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
sign_in_button.click()

email = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal_session_key"]')
email.send_keys(EMAIL)
email.send_keys(Keys.ENTER)

password = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal_session_password"]')
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

apply = driver.find_element(By.XPATH, value='//*[@id="jobs-apply-button-id"]/span')
apply.click()

phone = driver.find_element(By.XPATH, value='//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4258138447-14190701169-phoneNumber-nationalNumber"]')
phone.send_keys(PHONE)

next = driver.find_element(By.CSS_SELECTOR, value='footer button')
next.click()

review = driver.find_element(By.CSS_SELECTOR, value='button[data-live-test-easy-apply-review-button]')
review.click()

submit = driver.find_element(By.CSS_SELECTOR, value='button[data-live-test-easy-apply-submit-button]')
submit.click()
