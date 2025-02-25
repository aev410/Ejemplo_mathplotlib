#include <Arduino.h>

int xyzPins[] = {A1, A2, 10};
void setup() {
     Serial.begin(9600);
     pinMode(xyzPins[2], INPUT_PULLUP);
}

void loop() {
     int xVal = analogRead(xyzPins[0]);
     int yVal = analogRead(xyzPins[1]);
     int zVal = digitalRead(xyzPins[2]);
     Serial.print("X,Y,Z: ");
     Serial.print(xVal);
     Serial.print(",\t");
     Serial.print(yVal);
     Serial.print(",\t");
     Serial.println(zVal);
     delay(500);
}