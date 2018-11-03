#include <SimpleDHT.h>

//Author: Dillon Hicks
//This code needs the SimpleDHT library, so make sure to install it in Tools > Manage Libraries
int pinDHT11 = 7 ;
SimpleDHT11 dht11(pinDHT11);

void setup() {
  Serial.begin(9600);
}

void loop() {
    // start working...
    // read without samples.
    byte temperature = 0;
    byte humidity = 0;
    int err = SimpleDHTErrSuccess;
    if ((err = dht11.read(&temperature, &humidity, NULL)) != SimpleDHTErrSuccess) {
      Serial.print("Read DHT11 failed, err="); Serial.println(err);delay(1000);
      return;
   }
  
   Serial.print("Readings: ");
   Serial.print((int)temperature); Serial.print(" *C, "); 
   Serial.print((int)humidity); Serial.println(" H");
  
   delay(1500);

}
