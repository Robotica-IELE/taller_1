int ENA = 2;
int IN1 = 3;
int IN2 = 4;
int IN3 = 5;    // 
int IN4 = 6;    
int ENB = 7;  


//
String inputString = "";
int velMotor1 = 251;//izquierda
int velMotor2 = 253;//derecha
int velx;
bool stringComplete = false;
//

void setup()
{
  //
 Serial.begin(115200);
 inputString.reserve(200);
 //
 pinMode (ENA, OUTPUT);
 pinMode (ENB, OUTPUT); 
 pinMode (IN3, OUTPUT);
 pinMode (IN4, OUTPUT);
 pinMode (IN1, OUTPUT);
 pinMode (IN2, OUTPUT);
}

void loop()
{ 
  serialEvent(); 
  Leer();
  //Quieto();
  //Derecha();
  //Izquierda();
  //Atras();
  //Adelante();
  
  //analogWrite(ENA,105);
  //analogWrite(ENB,105);
  //delay(5000);
}

//Captura la velocidad
void readVelocidad()
{
  velx = Serial.readStringUntil("$").toInt();
  velMotor1 = 95.968*velx-142.1;
  velMotor2 = 96.706*velx-141.82;
}


//Comunicación con la raspberry
void Leer()
{
  if (stringComplete)
  {
    if (inputString.equals("$"))
    {
      readVelocidad();
    }
    if (inputString.equals("3"))
    {
      Izquierda();
      Serial.println("Izquierda");
    } 
    else if (inputString.equals("4"))
    {
      Derecha();
      Serial.println("Derecha");
    }
    else if (inputString.equals("1"))
    {
      Adelante();
      Serial.println("Adelante");
    }
    else if (inputString.equals("2"))
    {
      Atras();
      Serial.println("Atras");
    }
    else if (inputString.equals("0"))
    {
      Quieto();
      Serial.println("Quieto");
    }
    else 
    {
      Serial.println("Introdujo velocidades");
    }
    inputString = "";
    stringComplete = false;
  }
}

//

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

  analogWrite(ENA,velMotor1);
  analogWrite(ENB,velMotor2);
  //delay(500);
}

void Quieto() 
{
  //Para ir hacia adelante se usa [0110]
  digitalWrite (IN1, LOW);
  digitalWrite (IN2, LOW);
  
  digitalWrite (IN3, LOW);
  digitalWrite (IN4, LOW);

  analogWrite(ENA,velMotor1);
  analogWrite(ENB,velMotor2);
  //delay(500);
}

void Izquierda() 
{
  //Para ir hacia atras se usa [1001]
  digitalWrite (IN1, LOW);
  digitalWrite (IN2, LOW);
  
  digitalWrite (IN3, LOW);
  digitalWrite (IN4, HIGH);

  analogWrite(ENA,velMotor1);
  analogWrite(ENB,velMotor2);
  //delay(500);
}
void Atras() 
{
  //Para ir hacia la derecha se usa [1001]
  digitalWrite (IN1, HIGH);
  digitalWrite (IN2, LOW);
  
  digitalWrite (IN3, HIGH);
  digitalWrite (IN4, LOW);

  analogWrite(ENA,velMotor1);
  analogWrite(ENB,velMotor2);
  //delay(500);
}
void Adelante() 
{
  //Para ir hacia adelante se usa [1001]
  digitalWrite (IN1, LOW);
  digitalWrite (IN2, HIGH);
  
  digitalWrite (IN3, LOW);
  digitalWrite (IN4, HIGH);

  analogWrite(ENB,velMotor2);

  analogWrite(ENA,velMotor1);
  
  //delay(500);
}
