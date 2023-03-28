int IN1 = 1;
int IN2 = 2;
int IN3 = 3;    // Input3 conectada al pin 5
int IN4 = 4;    // Input4 conectada al pin 4 
int ENB = 6;    // ENB conectada al pin 3 de Arduino
int ENA = 5;

//
String inputString = "";
int velMotors = 0;
bool stringComplete = false;
//

void setup()
{
  //
 Serial.begin(115200);}
 inputString.reserve(200);
 //
 pinMode (ENA, OUTPUT);
 pinMode (ENB, OUTPUT); 
 pinMode (IN3, OUTPUT);
 pinMode (IN4, OUTPUT);
 pinMode (IN1, OUTPUT);
 pinMode (IN2, OUTPUT);
}
flag = true
void loop()
{ 
  serialEvent(); 
  if (flag == true)
  {
    velMotors = vel();
  }
  flag = false
  Leer();
  //analogWrite(ENA,105);
  // analogWrite(ENB,105);
  //delay(2000);
  //analogWrite(ENA,255);
  //analogWrite(ENB,255);
  //delay(2000);
  // Apagamos el motor y esperamos 5 seg
  analogWrite(ENA,0);
  analogWrite(ENB,0);
  delay(100);
}

//Comunicación con la raspberry
void Leer()
{
  if (stringComplete)
  {
    if (inputString.equals("Izquierda"))
    {
      Izquierda();
      Serial.println("Izquierda");
    } 
    else if (inputString.equals("Derecha"))
    {
      Derecha();
      Serial.println("Derecha");
    }
    else if (inputString.equals("Adelante"))
    {
      Adelante();
      Serial.println("Adelante");
    }
    else if (inputString.equals("Atras"))
    {
      Atras();
      Serial.println("Atras");
    }
    else 
    {
      vel();
      Serial.println("Introdujo velocidades");
    }
    inputString = "";
    stringComplete = false;
  }
}

//
int vel()
{
  vel = (int)inputString // inString.toInt()
  return 404.1*vel-57.5;
}
void serialEvent() {
  
  while (Serial.available()) {//Mientras tengamos caracteres disponibles en el buffer
    char inChar = (char)Serial.read();//Leemos el siguiente caracter
    if (inChar == '\n') {//Si el caracter recibido corresponde a un salto de línea
      stringComplete = true;//Levantamos la bandera 
    }
    else{//Si el caracter recibido no corresponde a un salto de línea
      inputString += inChar;//Agregamos el caracter a la cadena 
    }
  }
}
//

void Derecha() 
{
  //Para ir hacia adelante se usa [0110]
  digitalWrite (IN1, LOW);
  digitalWrite (IN2, HIGH);
  
  digitalWrite (IN3, LOW);
  digitalWrite (IN4, LOW);

  analogWrite(ENA,velMotors);
  analogWrite(ENB,velMotors);
  delay(500);
}

void Quieto() 
{
  //Para ir hacia adelante se usa [0110]
  digitalWrite (IN1, LOW);
  digitalWrite (IN2, LOW);
  
  digitalWrite (IN3, LOW);
  digitalWrite (IN4, LOW);

  analogWrite(ENA,velMotors);
  analogWrite(ENB,velMotors);
  delay(500);
}

void Izquierda() 
{
  //Para ir hacia atras se usa [1001]
  digitalWrite (IN1, LOW);
  digitalWrite (IN2, LOW);
  
  digitalWrite (IN3, LOW);
  digitalWrite (IN4, HIGH);

  analogWrite(ENA,80);
  analogWrite(ENB,80);
  delay(2000);
}
void Atras() 
{
  //Para ir hacia la derecha se usa [1001]
  digitalWrite (IN1, HIGH);
  digitalWrite (IN2, LOW);
  
  digitalWrite (IN3, HIGH);
  digitalWrite (IN4, LOW);

  analogWrite(ENA,velMotors);
  analogWrite(ENB,velMotors);
  delay(2000);
}
void Adelante() 
{
     //Para ir hacia adelante se usa [1001]
  digitalWrite (IN1, LOW);
  digitalWrite (IN2, HIGH);
  
  digitalWrite (IN3, LOW);
  digitalWrite (IN4, HIGH);

  analogWrite(ENA,velMotors);
  analogWrite(ENB,velMotors);
  delay(2000);
}
