#include <Arduino.h>

#ifndef LED_BUILTIN
#define LED_BUILTIN 2
#endif

bool ledOn = false;

void setup() {
  Serial.begin(115200);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  ledOn = !ledOn;
  digitalWrite(LED_BUILTIN, ledOn);  // на C6 DevKit это RGB-светодиод на GPIO8
  Serial.println(ledOn ? "blink: on" : "blink: off");
  delay(500);
}
