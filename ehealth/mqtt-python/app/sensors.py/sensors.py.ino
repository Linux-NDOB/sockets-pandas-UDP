#include <ArduinoJson.h>
// Para peso
#include "HX711.h"

#include <SharpIR.h>

#define ir A0
#define model 20150
// ir: the pin where your sensor is attached
// model: an int that determines your sensor:  1080 for GP2Y0A21Y
//                                            20150 for GP2Y0A02Y
//                                            (working distance range according to the datasheets)

SharpIR SharpIR(ir, model);


// Pin de datos y de reloj
byte pinData = 6 ;
byte pinClk = 7;

HX711 bascula;

// Parámetro para calibrar el peso y el sensor
float factor_calibracion = 20780.0; 

void setup() {
  //SERIAL COMMUNICATION SPEED
  Serial.begin(115200);
  // put your setup code here, to run once:
  // Iniciar sensor
  bascula.begin(pinData, pinClk);
 
  // Aplicar la calibración
  bascula.set_scale();
  
  // Iniciar la tara no tiene que haber nada sobre el peso
  bascula.tare();
 
  // Obtener una lectura de referencia
  long zero_factor = bascula.read_average();

}

void loop() { 

  unsigned long pepe1=millis();  // takes the time before the loop on the library begins

  int dis=SharpIR.distance();  // this returns the distance to the object you're measuring
  Serial.print(dis);
 
  // Aplicar calibración
  bascula.set_scale(factor_calibracion);
 
  float peso = bascula.get_units();
  Serial.print(peso);
  // JSON OBJECT
  DynamicJsonBuffer jBuffer;
  JsonArray& jsonData = jBuffer.createArray();

  //ADDING VARIABLES TO READ
  jsonData.add(peso);
  jsonData.add(dis);

  //PRINT DATA TO SERIAL PORT WITH 1SEG OF DELAY
  jsonData.printTo(Serial);
  Serial.println();
  delay(1000);
  // put your main code here, to run repeatedly:

}
