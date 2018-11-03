#include <SimpleDHT.h>

//Author: Dillon Hicks
//This code needs the SimpleDHT library, so make sure to install it in Tools > Manage Libraries

//In this case the DHT11 DATA pin is connected to Pin 7
int pinDHT11 = 7 ;

SimpleDHT11 dht11(pinDHT11);

void setup() {
  Serial.begin(9600);
}

void loop() {
    
    byte temperature = 0;
    byte humidity = 0;
    
    //Check for errors in sensor
    int err = SimpleDHTErrSuccess;
    if ((err = dht11.read(&temperature, &humidity, NULL)) != SimpleDHTErrSuccess) {
      Serial.print("Read DHT11 failed, err="); Serial.println(err);delay(1000);
      return;
    }
    
    //Print Readouts
    Serial.print("Readings: ");
    Serial.print((int)temperature); Serial.print(" *C, "); 
    Serial.print((int)humidity); Serial.println(" H");
    //DHT11 can only ready at 1Hz, so set a delay as necessary 
    delay(1500);

}
