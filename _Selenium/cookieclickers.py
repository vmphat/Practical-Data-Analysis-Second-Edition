# Reference: https://github.com/techwithtim/SeleniumTutorial/blob/main/cookieclickers.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service()
driver = webdriver.Chrome(service=service)

# Step 1: Open the browser and navigate to the website
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Step 2: Wait and select the language
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located(
        (By.XPATH, "//*[contains(text(), 'English')]"))
)
language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()

# Step 3: Wait for the game to load
cookie_id = "bigCookie"
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, cookie_id))
)
cookie = driver.find_element(By.ID, cookie_id)

n_cookies_id = "cookies"
product_price_prefix = "productPrice"
product_prefix = "product"
while True:
    cookie.click()
    cookies_count_str = driver.find_element(By.ID, n_cookies_id).text
    n_cookies = int(cookies_count_str.split(" ")[0].replace(",", ""))

    for i in range(4):
        product_price_id: str = product_price_prefix + str(i)
        product_price: str = driver.find_element(
            By.ID, product_price_id).text.replace(",", "")

        if not product_price.isdigit():
            continue

        if n_cookies >= int(product_price):
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break
