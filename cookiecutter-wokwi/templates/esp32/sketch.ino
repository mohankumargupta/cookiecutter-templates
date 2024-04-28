void setup() {
  pinMode(LED_BUILTIN, OUTPUT);

  // Wait for USB Serial to become available
  while (!Serial) delay(100);

  Serial.begin(115200);
  Serial.println("Hello, esp32 dev kit doit nodemcu!");
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
}
