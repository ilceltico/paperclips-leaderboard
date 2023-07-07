
# python3.6

import random
import logging
import time

from paho.mqtt import client as mqtt_client

FIRST_RECONNECT_DELAY = 1
RECONNECT_RATE = 2
MAX_RECONNECT_COUNT = 120
MAX_RECONNECT_DELAY = 600

broker = 'localhost'
port = 1883
topic = "python/mqtt"
# Generate a Client ID with the subscribe prefix.
# client_id = f'subscribe-{random.randint(0, 100)}'
client_id = f'subscribe-{1}'
# username = 'emqx'
# password = 'public'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            subscribe(client)
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)



    # def on_disconnect(client, userdata, rc):
    #     logging.info("Disconnected with result code: %s", rc)
    #     reconnect_count, reconnect_delay = 0, FIRST_RECONNECT_DELAY
    #     while reconnect_count < MAX_RECONNECT_COUNT:
    #         logging.info("Reconnecting in %d seconds...", reconnect_delay)
    #         time.sleep(reconnect_delay)

    #         try:
    #             client.reconnect()
    #             logging.info("Reconnected successfully!")
    #             return
    #         except Exception as err:
    #             logging.error("%s. Reconnect failed. Retrying...", err)

    #         reconnect_delay *= RECONNECT_RATE
    #         reconnect_delay = min(reconnect_delay, MAX_RECONNECT_DELAY)
    #         reconnect_count += 1
    #     logging.info("Reconnect failed after %s attempts. Exiting...", reconnect_count)

    client = mqtt_client.Client(client_id, clean_session=False)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    # client.on_disconnect = on_disconnect
    return client






def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    client.loop_forever()


if __name__ == '__main__':
    run()
