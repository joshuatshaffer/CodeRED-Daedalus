//ard 101
#include <Servo.h>

 // create servo object to control a servo
Servo yz;
Servo elbow;


void setup()
{
  Serial.begin(9600);
  
    // attaches the servo on pin 9 to the servo object
  yz.attach(3);
  elbow.attach(9);
}

void loop()
{
  if (Serial.available()) {
    int command = Serial.read();
    int val = Serial.parseFloat();

    if (command == 'y') {
      yz.write(val); 
    } else if (command == 'e') {
      elbow.write(val);
    } 
     else {
      Serial.print("The command \"");
      Serial.print(command);
      Serial.println("\" is not recognized");
    }
    } 
 
}

