import json
import paho.mqtt.client as mqtt

# Load configuration
with open("mqtt_config.json") as f:
    config = json.load(f)

broker = config["broker"]
port = config["port"]
keepalive = config.get("keepalive", 60)
topic = config["topics"]["vehicle_parameters"]

# Callback when a message is received
def on_message(client, userdata, message):
    try:
        data = json.loads(message.payload.decode())
        print(f"Received message on {message.topic}: {json.dumps(data, indent=2)}")
    except json.JSONDecodeError:
        print(f"Received non-JSON message: {message.payload}")

# Create MQTT client
client = mqtt.Client()
client.on_message = on_message

# Connect and subscribe
client.connect(broker, port, keepalive)
client.subscribe(topic)
print(f"Subscribed to topic: {topic}")

# Keep listening
client.loop_forever()
