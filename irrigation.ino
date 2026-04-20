#include <ESP8266WiFi.h>
#include <FirebaseESP8266.h>

#define WIFI_SSID "YOUR_WIFI"
#define WIFI_PASSWORD "YOUR_PASSWORD"

#define FIREBASE_HOST "YOUR_PROJECT.firebaseio.com"
#define FIREBASE_AUTH "YOUR_SECRET"

#define sensorPin A0
#define relayPin D1

FirebaseData firebaseData;

void setup() {
  Serial.begin(9600);
  pinMode(relayPin, OUTPUT);

  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }

  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
}

void loop() {
  int moisture = analogRead(sensorPin);

  Firebase.setInt(firebaseData, "/moisture", moisture);

  if (Firebase.getString(firebaseData, "/pump")) {
    String state = firebaseData.stringData();

    if (state == "ON") digitalWrite(relayPin, LOW);
    else digitalWrite(relayPin, HIGH);
  }

  delay(2000);
}