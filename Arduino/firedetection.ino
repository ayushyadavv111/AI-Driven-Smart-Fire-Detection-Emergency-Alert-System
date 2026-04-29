#include <DHT.h>

#define DHTPIN 2
#define DHTTYPE DHT11

#define MQ2 A0
#define BUZZER 8

DHT dht(DHTPIN, DHTTYPE);

// Thresholds (adjust if needed)
float tempThreshold = 50.0;
int smokeThreshold = 280;

void setup() {
  Serial.begin(9600);
  pinMode(BUZZER, OUTPUT);
  dht.begin();
}

void loop() {
  float temperature = dht.readTemperature();
  int smokeValue = analogRead(MQ2);

  // Read data from Python (webcam)
  char data = '0';
  if (Serial.available()) {
    data = Serial.read();
  }

  // Debug output
  Serial.print("Temp: ");
  Serial.print(temperature);
  Serial.print(" | Smoke: ");
  Serial.print(smokeValue);
  Serial.print(" | Cam: ");
  Serial.println(data);

  // 🔥 FINAL DECISION
  if (temperature > tempThreshold || smokeValue > smokeThreshold || data == '1') {
    tone(BUZZER, 1000);   // ALERT
  } else {
    noTone(BUZZER);
  }

  delay(1);
}
