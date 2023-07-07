
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# service = Service(executable_path="/usr/local/bin/chromedriver")
# service = Service(executable_path="/usr/bin/safaridriver")
with webdriver.Chrome() as driver:
# with webdriver.Safari(service=service) as driver:
    driver.get('file:///Users/stella/repos/leaderboard/leaderboard.html')
    # driver.get('https://gogos.me/leaderboard/')
    # driver.get('http://watir.com/examples/shadow_dom.html')
    time.sleep(5)


    editButton = driver.find_element(By.CLASS_NAME, "edit")
    editButton.click()

    textArea = driver.find_element(By.ID, "tarea")
    textArea.send_keys("a,a,2\nb,b,4")

    editPopup = driver.find_element(By.CLASS_NAME, "edit-popup")
    okButton = editPopup.find_element(By.CLASS_NAME, "ok")
    okButton.click()

    time.sleep(2)

    editButton = driver.find_element(By.CLASS_NAME, "edit")
    editButton.click()

    textArea = driver.find_element(By.ID, "tarea")
    textArea.clear()
    textArea.send_keys("a,a,6\nb,b,4")

    editPopup = driver.find_element(By.CLASS_NAME, "edit-popup")
    okButton = editPopup.find_element(By.CLASS_NAME, "ok")
    okButton.click()

    # input_shadow = driver.execute_script('''return document.querySelector("textarea#tarea").shadowRoot''')

    # shadow_host = driver.find_element(By.CSS_SELECTOR, '#shadow_host')
    # shadow_root = shadow_host.shadow_root
    # shadow_content = shadow_root.find_element(By.CSS_SELECTOR, '#shadow_content')
    # div_text = inputShadow.find_element_by_tag_name("div").text
    # el.shadow_r
    import pdb
    pdb.set_trace()
    # el.click