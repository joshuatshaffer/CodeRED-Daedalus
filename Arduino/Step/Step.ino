#include <Stepper.h>
#include <Servo.h>

Stepper shoulder(4096, 5, 6, 1, 2);
bool is_zeroed = false;
int calb_speed = 10,
    norm_speed = 30,
    calib_butt = 3;

void setup() {
  stepper.setSpeed(calb_speed);
  pinMode(calib_butt, INPUT);
}

void loop() {
  if (is_zeroed) {
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
  } else {
    stepper.step(10);
  
    if (digitalRead(calib_butt)) {
      stepper.setSpeed(norm_speed);
      is_zeroed = true;
    }
    delay (10);
  }
}

