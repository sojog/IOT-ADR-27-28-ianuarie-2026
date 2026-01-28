
## CITIRE DE LA BROKER
import random
import time
import paho.mqtt.client as mqtt


### BROKER -> Structura RADIO
MQTT_BROKER = "broker.hivemq.com"

### TOPIC -> Frecventa Radio
TOPIC = "temperaturi_python" # este schimbabil

## PORT -> Specific MQTT
PORT = 1883

QOS_FARA_GARANTIE = 0
QOS_CEL_PUTIN_O_DATA = 1
QOS_FIX_O_DATA = 2

client_abonat_id = "ABONAT_IOT_321"

client = mqtt.Client(client_id=client_abonat_id)

def connect_callback(client, userdata, connect_flags, reason_code):
    if reason_code == 0:
        print("Dispozitivul s-a conectat cu success")
        client.subscribe(TOPIC)
    else:
        print(f"Conexiunea a esuat: {reason_code}")

def message_callback(client, userdata, message):
    print("Se apeleaza de fiecare data cand primesc un mesaj")

    print(f"Topicul mesajului: {message.topic}")

    payload_mesaj = message.payload.decode()

    print(f"Mesajul trimis: {payload_mesaj}")


client.on_connect = connect_callback

client.on_message = message_callback

try:
    client.connect(MQTT_BROKER,PORT, 60)
    client.loop_forever()
except Exception as e:
    print(f"A aparut o eroare {e}")