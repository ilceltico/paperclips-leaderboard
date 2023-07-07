
import time

from paho.mqtt import client as mqtt_client

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


JS_ADD_TEXT_TO_INPUT = """
  var elm = arguments[0], txt = arguments[1];
  elm.value += txt;
  elm.dispatchEvent(new Event('change'));
  """

FIRST_RECONNECT_DELAY = 1
RECONNECT_RATE = 2
MAX_RECONNECT_COUNT = 120
MAX_RECONNECT_DELAY = 600

broker = 'localhost'
port = 1883
topic = "paperclips"
client_id = f'subscribe-{1}'
# username = 'emqx'
# password = 'public'

data = {}


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            subscribe(client)
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)


    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client



def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        text = msg.payload.decode()
        print(f"Received `{text}` from `{msg.topic}` topic")

        fields = text.split(",")
        # print(fields)
        name = fields[0]
        count = fields[1]
        data[name] = count
        # print(name)
        # print(count)

    client.subscribe(topic)
    client.on_message = on_message


def run():
    with webdriver.Chrome() as driver:
        driver.get(f'file://{os.getcwd()}/leaderboard/leaderboard.html')
        time.sleep(2)

        client = connect_mqtt()
        client.loop_start()

        while True:
            time.sleep(5)
            editButton = driver.find_element(By.CLASS_NAME, "edit")
            editButton.click()

            textArea = driver.find_element(By.ID, "tarea")
            textArea.clear()

            sortedData = sorted(data.items(), key=lambda x: -float(x[1]) )
            print(sortedData)

            text = ""
            i = 1
            for item in sortedData:
                key = item[0]
                value = item[1]

                rank = str(i)
                if rank == "1":
                    rank = "🥇"
                elif rank == "2":
                    rank = "🥈"
                elif rank == "3":
                    rank = "🥉"

                text += f"{rank},{key},{value}\n"
                
                i += 1


            # textArea.send_keys(text)
            driver.execute_script(JS_ADD_TEXT_TO_INPUT, textArea, text)

            editPopup = driver.find_element(By.CLASS_NAME, "edit-popup")
            okButton = editPopup.find_element(By.CLASS_NAME, "ok")
            okButton.click()



if __name__ == '__main__':
    run()
