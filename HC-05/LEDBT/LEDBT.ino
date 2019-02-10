#include <SoftwareSerial.h>
SoftwareSerial BTSerial(10, 11); // RX | TX
void setup()
{
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  BTSerial.begin(9600);  // HC-05 default speed in Standard mode
}
void loop()
{
  // Keep reading from HC-05 and send to Arduino Serial Monitor
  if (BTSerial.available()){ // Check if the Serial is reading properly
    char c = BTSerial.read();
    if(c == '1'){ //If 1 is detected in Putty
      digitalWrite(LED_BUILTIN, HIGH); //Set the LED to High
      BTSerial.println("LED On!"); //Write this to the HC-05’s serial
    }
    if(c == '0'){ //If 0 is detected in Putty
      digitalWrite(LED_BUILTIN, LOW);
      BTSerial.println("LED Off!"); 
    }
  }
}
