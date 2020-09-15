# Include Library
import paho.mqtt.client as paho  
import time
import random
import json
#MQTT Connection Information
MQTT_SERVER = "localhost"
MQTT_PATH = "#"
port=1883
client = []


#Default Connection Callback function
def on_connect(client, userdata, flags, rc):
    print("[INFO] Connected with result code "+str(rc))
    client.subscribe(MQTT_PATH)

#Default Connection Callback function after recieving message from server
def on_message(client, userdata, msg):
    #print("Num:",i)
    print("[DATA] " + msg.topic+" "+str(msg.payload))

# Send data contineously to MQTT Server
def send_data(client):
	print("[INFO] Press CRTL+C to stop the script...")
	try:
		while (1):
			temp = random.randint(20, 30)
			humidity = random.randint(10, 15)
			client.publish("house/temp",str(temp))
			client.publish("house/humidity",str(humidity))
			# To publish using JSON packet
			client.publish("house",str(json.dumps({"temp":str(temp),"humidity":str(humidity)}))) 
			time.sleep(2)
	except KeyboardInterrupt:
		print("[INFO] Dummy Sender Stopped..")
		#pass

# Main Function
if __name__ == "__main__":
	print("[INFO] Dummy Sender Init..")
	client = paho.Client()
	client.on_connect = on_connect
	client.on_message = on_message
	client.connect(MQTT_SERVER, port, 60)
	#client.loop_forever()	# Will loop forever
	client.loop_start()
	send_data(client)
	client.loop_stop() #stop the loop
	print("[INFO] END")