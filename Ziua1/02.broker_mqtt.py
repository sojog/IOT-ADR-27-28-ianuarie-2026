import random
import time
import paho.mqtt.client as mqtt

## SCRIERE CATRE BROKER


### BROKER -> Structura RADIO
MQTT_BROKER = "broker.hivemq.com"

### TOPIC -> Frecventa Radio
TOPIC = "temperaturi_python" # este schimbabil

## PORT -> Specific MQTT
PORT = 1883

QOS_FARA_GARANTIE = 0
QOS_CEL_PUTIN_O_DATA = 1
QOS_FIX_O_DATA = 2

client_id = "PUBLISHER_IOT_23"

MIN_TEMP = 1
MAX_TEMP = 40

client = mqtt.Client(client_id=client_id)

def connect_callback(client, userdata, connect_flags, reason_code):
    if reason_code == 0:
        print("Dispozitivul s-a conectat cu success")
    else:
        print(f"Conexiunea a esuat: {reason_code}")

client.on_connect = connect_callback

client.connect(MQTT_BROKER,PORT, 60)
client.loop_start()


while True:
    temperatura = random.randint(MIN_TEMP, MAX_TEMP)
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    payload = f'''{{
        "timestamp" : "{timestamp}",
        "temperatura" : {temperatura}
    }}'''
    print(payload)

    client.publish(TOPIC, payload, QOS_FARA_GARANTIE)

    time.sleep(5)