import json
import time
import random
import paho.mqtt.client as mqtt

BROKER_HOST = "localhost"
BROKER_PORT = 1883
DEVICE_ID = "device-001"
TOPIC = f"sensors/{DEVICE_ID}/telemetry"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)   
client.connect(BROKER_HOST, BROKER_PORT, 60)

while True:
    payload = {
        "device_id": DEVICE_ID,
        "timestamp": int(time.time()),
        "temperature": round(random.uniform(20, 30), 2),
        "humidity": round(random.uniform(40, 70), 2)
    }

    client.publish(TOPIC, json.dumps(payload))
    print("Message envoyé :", payload)

    time.sleep(5)