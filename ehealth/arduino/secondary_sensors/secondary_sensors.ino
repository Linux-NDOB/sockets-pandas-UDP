// import ArduinoJson
#include <ArduinoJson.h>

// Para altura
int trig = 8;
int echo = 9;

float duration;
int distance;
int Length;
int door_Height =200;

// Para peso
#include "HX711.h"


// Pin de datos y de reloj
byte pinData = 6 ;
byte pinClk = 7;

HX711 bascula;

// Parámetro para calibrar el peso y el sensor
float factor_calibracion = 20780.0; 

void setup() {
  // Para peso
  Serial.begin (9600);
  
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);

 
  Serial.println("Quita cualquier peso de la bascula");
  Serial.println("Una vez empiece a mostrar informacion de medidas, coloca un peso conocido encima de la bascula");
  Serial.println("Presiona + o - para el factor de calibracion");
 
  // Iniciar sensor
  bascula.begin(pinData, pinClk);
 
  // Aplicar la calibración
  bascula.set_scale();
  
  // Iniciar la tara no tiene que haber nada sobre el peso
  bascula.tare();
 
  // Obtener una lectura de referencia
  long zero_factor = bascula.read_average();
  
  // Mostrar la primera desviación
  Serial.print("Zero factor: ");
  Serial.println(zero_factor);

}

void loop() {
  // Para peso:
  
  // Aplicar calibración
  bascula.set_scale(factor_calibracion);
 
  // Para altura

  digitalWrite(trig, LOW);        
  delayMicroseconds(2);              
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);           
  digitalWrite(trig, LOW);
  duration = pulseIn(echo, HIGH);
  distance = (duration/2) / 29.1;
  Length =  door_Height - distance;
  //Para IMC

  float peso = bascula.get_units();
  float altura_m = Length/100;
  float altura = pow(altura_m,2);
  float imc = peso/altura_m;
  
  DynamicJsonBuffer jBuffer; 
  JsonObject& data = jBuffer.createObject();
  data["Height"] = altura_m;
  data["Weight"] = peso;
  data["IMC"] = imc;
  data.prettyPrintTo(Serial);      
  
}
  

 
