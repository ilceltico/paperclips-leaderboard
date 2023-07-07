# python 3.6

import random
import time
import logging

from paho.mqtt import client as mqtt_client

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


broker = 'localhost'
port = 1883
topic = "paperclips"
client_id = ""
user=""
# username = 'emqx'
# password = 'public'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client, driver):
    while True:
        time.sleep(2)
        clips = int(driver.find_element(By.ID, "clips").text.replace(',', ''))
        msg = f"{user},{clips}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")


def run():
    print("Type your username: ")
    global user
    global client_id
    user = input()
    client_id = f'publish-{user}'

    client = connect_mqtt()

    options = webdriver.ChromeOptions()
    options.add_argument(f"user-data-dir={os.path.join(os.getcwd(),user)}")
    with webdriver.Chrome(options=options) as driver:
        driver.get('https://www.decisionproblem.com/paperclips/index2.html')
        time.sleep(5)

        client.loop_start()
        publish(client, driver)
        client.loop_stop()


if __name__ == '__main__':
    run()
