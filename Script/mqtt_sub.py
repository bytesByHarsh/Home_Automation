import paho.mqtt.client as paho 

MQTT_SERVER = "localhost"
MQTT_PATH = "#"
port=1883
client = []

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(MQTT_PATH)
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    #print("Num:",i)
    print(msg.topic+" "+str(msg.payload))



if __name__ == "__main__":
	client = paho.Client()
	client.on_connect = on_connect
	client.on_message = on_message
	client.connect(MQTT_SERVER, port, 60)
	client.loop_forever()
	#client.loop_start()
	print("END")