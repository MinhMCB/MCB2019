#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include "DHT.h"
#include <ArduinoJson.h>


// Pin
#define DHTPIN D4
// Su dung cam bien DHT11 
#define DHTTYPE DHT11
// Thiet lap DHT
DHT dht(DHTPIN, DHTTYPE);


// Cập nhật thông tin
// Thông tin về wifi

#define ssid "TLGT"
#define password "9876543210"



// Thông tin về MQTT Broker
#define mqtt_server "192.168.1.9" // Thay bằng thông tin của bạn
#define mqtt_topic_pub "test"   //Giữ nguyên nếu bạn tạo topic tên là demo
#define mqtt_topic_sub "demo"
#define mqtt_user "ntm"    //Giữ nguyên nếu bạn tạo user là esp8266 và pass là 123456
#define mqtt_pwd "minh6464"

const uint16_t mqtt_port = 1883; //Port của CloudMQTT

WiFiClient espClient;
PubSubClient client(espClient);

long lastMsg = 0;
char msg[50];
int value = 0;
int count=1;

void setup() {
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, mqtt_port); 
  client.setCallback(callback);

  // Khoi tao DHT 
  dht.begin();
}
// Hàm kết nối wifi
void setup_wifi() {
  delay(10);
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}
// Hàm call back để nhận dữ liệu
void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();
}
// Hàm reconnect thực hiện kết nối lại khi mất kết nối với MQTT Broker
void reconnect() {
  // Chờ tới khi kết nối
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Thực hiện kết nối với mqtt user và pass
    if (client.connect("ESP8266Client",mqtt_user, mqtt_pwd)) {
      Serial.println("connected");
      // Khi kết nối sẽ publish thông báo
      client.publish(mqtt_topic_pub, "ESP_reconnected");
      // ... và nhận lại thông tin này
      client.subscribe(mqtt_topic_sub);
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Đợi 5s
      delay(5000);
    }
  }
}
void loop() {
  // Kiểm tra kết nối
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
  // Sau mỗi 2s sẽ thực hiện publish dòng hello world lên MQTT broker
  long now = millis();
  if (now - lastMsg > 400) {
    lastMsg = now;
    
    // Doc do am
    float h = dht.readHumidity();
    // Doc nhiet do o do C
    float t = dht.readTemperature();
    
    if (count==6){
      count=1;
    }
    //@@@@@@@@@@@@@@@@@@@@@@@@@
    DynamicJsonBuffer jBuffer;
    JsonObject& root = jBuffer.createObject();

    root["SensorID"] = count;
    root["Temperature"] = t;
    root["Humidity"] = h;

 
  
    //@@@@@@@@@@@@@@@@
    
    char JSONmessageBuffer[100];
    root.printTo(JSONmessageBuffer, sizeof(JSONmessageBuffer));
    
    snprintf (msg,100, JSONmessageBuffer);
    Serial.print("Publish message: ");
    Serial.println(msg);
    client.publish(mqtt_topic_pub, msg);
    count++;
  }
}
