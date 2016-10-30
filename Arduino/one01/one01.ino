//UNO1 Left above sticker 1D111
#include <Servo.h>

Servo shoulder;  // create servo object to control a servo
Servo torso;


void setup()
{
  Serial.begin(9600);
  
  torso.attach(5);  // attaches the servo on pin 9 to the servo object
  shoulder.attach(4);

}

void loop()
{
  if (Serial.available())
  {
    int command = Serial.read();
    int val = Serial.parseFloat();

    if (command == 't') {
      torso.write(val); 
    }
    else if (command == 's') {
      shoulder.write(val); 
    }    
     else {
      Serial.print("The command \"");
      Serial.print(command);
      Serial.println("\" is not recognized");
    }
  }
 
}


