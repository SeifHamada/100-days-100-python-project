from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep, time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

sleep(3)
try:
    language_button = driver.find_element(By.ID, value="langSelect-EN")
    language_button.click()
    sleep(3)
except NoSuchElementException:
    pass

sleep(3)

cookie = driver.find_element(By.ID, value="bigCookie")
item_ids = [f"product{i}" for i in range(18)]

timeout = time() + 5
five_min = time() + 60 * 5

while True:
    cookie.click()

    if time() > timeout:
        try:
            cookies_element = driver.find_element(By.ID, value="cookies")
            cookie_text = cookies_element.text
            cookie_count = int(cookie_text.split()[0].replace(",", ""))

            products = driver.find_elements(By.CSS_SELECTOR, value="div[id^='product']")

            best_item = None
            for product in reversed(products):
                if "enabled" in product.get_attribute("class"):
                    best_item = product
                    break
            
            if best_item:
                best_item.click()

        except(NoSuchElementException, ValueError):
            pass

        timeout = time() + 5
    
    if time() > five_min:

        try:
            cookie_element = driver.find_element(By.ID, value="cookies")
            print(f"Final result: {cookies_element.text}")
        
        except NoSuchElementException:
            pass
        break
