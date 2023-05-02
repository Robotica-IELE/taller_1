#include <Servo.h>  // librería para poder controlar el servo


Servo servoMotorTronco;
////
Servo servoMotor1;
Servo servoMotor2;
///
Servo servoMotorCodo;
Servo servoMotorMuneca;
Servo servoMotorGarra;

bool stringComplete = false;
String inputString = "";

void setup(){ 
  Serial.begin(115200);
  // Asociamos el servo a la patilla 2 del Arduino

  servoMotorTronco.attach(8);
  servoMotor1.attach(9);
  servoMotor2.attach(10);
  servoMotorCodo.attach(11);
  servoMotorMuneca.attach(12);
  servoMotorGarra.attach(13);


  servoMotorTronco.write(0); // Inicializamos al ángulo 0 el servomotor
  servoMotor1.write(0); // Inicializamos al ángulo 0 el servomotor
  servoMotor2.write(0); // Inicializamos al ángulo 0 el servomotor
  servoMotorCodo.write(0); // Inicializamos al ángulo 0 el servomotor
  servoMotorMuneca.write(0); // Inicializamos al ángulo 0 el servomotor
  servoMotorGarra.write(0); // Inicializamos al ángulo 0 el servomotor

}

void loop(){

//   //giro de 0 a 180º
  for (int i = 225; i <270; i++){
    servoMotorTronco.write(i);
    Serial.print("Angulo:  ");
    Serial.println(i);
    ///////////////////////////
//    servoMotorTronco.write(i);
//    Serial.print("Angulo:  ");
//    Serial.println(i);
    delay(20);
  }
 // giro de 180 a 0º
  for (int i = 269; i > 225; i--){
    servoMotorTronco.write(i);
    Serial.print("Angulo:  ");
    Serial.println(i);
    delay(20);
    //////////////////
//    servoMotorTronco.write(i);
//    Serial.print("Angulo:  ");
//    Serial.println(i);
  }

}
