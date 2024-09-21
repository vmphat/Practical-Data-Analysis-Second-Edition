from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time


service = Service()
driver = webdriver.Chrome(service=service)

driver.get("https://www.gold.org/")
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "value"))
)

with open("goldPrice.out", "w") as f:
    for _ in range(10):
        date_time: str = datetime.now() \
                                 .strftime("%Y-%m-%d %I:%M:%S%P")
        gold_price: str = driver \
            .find_element(By.CLASS_NAME, "value") \
            .text.replace(",", "")

        # Write to file
        f.write(f"{date_time} {gold_price}\n")
        # Print to console
        print(date_time, gold_price)

        time.sleep(59.9)

driver.quit()
