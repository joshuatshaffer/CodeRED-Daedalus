#include <Stepper.h>
#include <Servo.h>

Stepper shoulder(4096, 5, 6, 1, 2);

void setup() {
  stepper.setSpeed(30);
}

void loop() {
    if (Serial.available()) {
    int command = Serial.read();
    int val = Serial.parseFloat();

    if (command == 's') {
      stepper.step(val - previous);
      previous = val;
    } else {
      Serial.print("The command \"");
      Serial.print(command);
      Serial.println("\" is not recognized");
    }
  }
}
