void setup() {
  pinMode(LED_BUILTIN, OUTPUT);

  // Wait for USB Serial to become available
  while (!Serial) delay(100);

  Serial.begin(115200);
  Serial.println("Hello, esp32s devkit doit nodemcu!");
  // https://www.buildlog.net/blog/wp-content/uploads/2018/04/nodemcu_32s_pinout.png
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
}
