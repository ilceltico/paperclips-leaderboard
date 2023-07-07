from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

service = Service(executable_path="/usr/local/bin/chromedriver")
with webdriver.Chrome(service=service) as driver:
    driver.get('https://www.decisionproblem.com/paperclips/index2.html')

    while (True):
        time.sleep(2)
        el = driver.find_element(By.ID, "clips")
        print(el.text)
