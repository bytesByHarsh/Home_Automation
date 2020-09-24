import paho.mqtt.client as paho 

class MQTTClient():

	def __init__(self,server,path,port):
		self.client = paho.Client()
		self.client.on_connect = self.on_connect
		self.client.on_message = self.on_message
		self.client.connect(server, port, 60)
		self.path = path
		self.client.loop_forever()

	def on_connect(self,client, userdata, flags, rc):
		print("Connected with result code "+str(rc))
		self.client.subscribe(self.path)
	def on_message(self,client, userdata, msg):
	    print(msg.topic+" "+str(msg.payload))


if __name__ == '__main__':
	
	client_new = MQTTClient(server="localhost",path="#",port=1883)
	