//Author: Dillon Hicks
#include <Servo.h>

Servo myservo;  
int button = 2;
bool rev = false;
int pos = 0;    // variable to store the servo position

void setup() {
  myservo.attach(7);  // attaches the servo on pin 9 to the servo object
  pinMode(button, INPUT);
}

void loop() {
    //if the button is high
    if(digitalRead(button) == HIGH){
      //Change servo position based on current position
      if(pos == 180){
        pos = 0;}
      else if(pos == 0){
        pos = 180;}
      //Move the servo to the current position
      myservo.write(pos);
      //Wait .2 Seconds to give the servo time to move
      delay(200);                     
    }
}
