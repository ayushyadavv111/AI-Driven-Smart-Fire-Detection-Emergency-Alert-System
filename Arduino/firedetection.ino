
#include <DHT.h>

#define DHTPIN 2
#define DHTTYPE DHT11

#define FLAME_SENSOR 3
#define SMOKE_SENSOR A0
#define BUZZER 8

DHT dht(DHTPIN, DHTTYPE);

float temperature;
int smokeValue;
int flameValue;

void setup() {

  Serial.begin(9600);

  pinMode(FLAME_SENSOR, INPUT);
  pinMode(BUZZER, OUTPUT);

  dht.begin();
}

void loop() {

  temperature = dht.readTemperature();
  smokeValue = analogRead(SMOKE_SENSOR);
  flameValue = digitalRead(FLAME_SENSOR);

  Serial.print("Temperature: ");
  Serial.println(temperature);

  Serial.print("Smoke Level: ");
  Serial.println(smokeValue);

  Serial.print("Flame Status: ");
  Serial.println(flameValue);

  if (temperature > 50 || smokeValue > 400 || flameValue == LOW) {

    Serial.println("🔥 FIRE RISK DETECTED");
    digitalWrite(BUZZER, HIGH);

  } else {

    Serial.println("SAFE");
    digitalWrite(BUZZER, LOW);

  }

  delay(2000);
}
