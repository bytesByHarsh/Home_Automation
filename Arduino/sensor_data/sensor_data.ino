// Include Libraries
#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <DHT.h>

// Connect to the WiFi
const char* ssid = "HarshMittal";          // Wifi Name                 
const char* password = "1234567890";       // Wifi password

const char* mqtt_server = "192.168.0.33";   // MQTT server IP address

WiFiClient espClient;
PubSubClient client(espClient);

// DHT Sensor information
#define DHTPIN D3
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

// Declare variables
unsigned long lastSend;


// Reconect to wifi
void reconnect(){
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    if (client.connect("NodeMCU1")){
      Serial.println("Connected");
      client.subscribe("house/#");
    }
    else{
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}
void setup() {
  
  Serial.begin(9600);
  Serial.println("Booting Up the NodeMCU...");
  client.setServer(mqtt_server, 1883); // MQTT Server port

  client.setCallback(callback); // Calback function for MQTT Messages

  dht.begin();

}

void loop() {
  
  // Check Connection first
  if (!client.connected()) {
    reconnect();  
  }

  if ( millis() - lastSend > 1000 ){ // Update and send only after 1 seconds
    
    getAndSendSensorData();
    lastSend = millis();
  }

  client.loop();
}

void getAndSendSensorData(){
  Serial.println("Collecting sensor data.....");
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  if (isnan(h) || isnan(t)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  Serial.print("Humidity: ");
  Serial.print(h);
  Serial.print(" %\t");
  Serial.print(" %\t Temperature: ");
  Serial.print(t);
  Serial.print(" *C ");

  String temperature = String(t);
  String humidity = String(h);


  // Prepare a JSON payload string
  String payload = "{";
  payload += "\"temp\":"; payload += temperature; payload += ",";
  payload += "\"humidity\":"; payload += humidity;
  payload += "}";

  // Send payload
  char attributes[100];
  char temp[10],hum[10];
  payload.toCharArray( attributes, 100 );
  temperature.toCharArray(temp,10);
  humidity.toCharArray(hum,10);
  client.publish( "house", attributes );
  client.publish( "house/temp", temp );
  client.publish( "house/humidity", hum );
  Serial.println( attributes );
}

// For Recieved Message
void callback(char* topic, byte* payload, unsigned int length){
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
}
