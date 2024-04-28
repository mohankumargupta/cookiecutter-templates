void setup() {
  pinMode(LED_BUILTIN, OUTPUT);

  // Wait for USB Serial to become available
  while (!Serial) delay(100);

  Serial.begin(115200);
  Serial.println("Hello, Wemos S2 mini!");
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
}
