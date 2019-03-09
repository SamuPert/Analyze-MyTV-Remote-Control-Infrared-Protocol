int pinInfraredSensor = A0;
int sensorValue;

void setup() {
  pinMode(pinInfraredSensor, INPUT);
  Serial.begin(2000000);
}

void loop() {
  
  sensorValue = analogRead(pinInfraredSensor);
  Serial.println(sensorValue);
  
}
