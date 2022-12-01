void Adelante();
void Atras();
void alto();
void gira_derecha();
void gira_izquierda();
void parametros(String funcion, String velocidad, String tiempo);
//void div_char(char data);
const int pin1 = 3;
const int pin2 = 2;
const int pin3 = 4;
const int pin4 = 5;
const int pinControlizq = 9;
const int pinControlder = 10;
int potenciaizq = 255;
int potenciader = 255;
int tiempo;
int cont = 0;
char data;
String funcion;
String velocidad;
String tiempoS;
void setup() {
  // put your setup code here, to run once:
  pinMode(pinControlizq,OUTPUT);
  pinMode(pinControlder,OUTPUT);
  pinMode(pin1, OUTPUT);
  pinMode(pin2, OUTPUT); 
  pinMode(pin3, OUTPUT); 
  pinMode(pin4, OUTPUT); 
  analogWrite(pinControlizq,potenciaizq);
  analogWrite(pinControlder,potenciader);
  Serial.begin(9600);}

void loop() {
  // put your main code here, to run repeatedly:
  while(Serial.available()){
    data = Serial.read();
    if(data == 44){
      cont++;
    }
    if(cont == 0){
      funcion+=data;
    }
    if(cont == 1 && data!=44){
      velocidad+=data;
    }
    if(cont == 2 && data!=44){
      tiempoS+=data;
    }
    if(cont == 3){
      parametros(funcion,velocidad,tiempoS);
    }
  }
}

void Adelante(){
  digitalWrite(pin1,HIGH);
  digitalWrite(pin2,LOW);
  digitalWrite(pin3,HIGH);
  digitalWrite(pin4,LOW);
}

void alto(){
  digitalWrite(pin1,LOW);
  digitalWrite(pin2,LOW);
  digitalWrite(pin3,LOW);
  digitalWrite(pin4,LOW);
}
void Atras(){
  digitalWrite(pin1,LOW);
  digitalWrite(pin2,HIGH);
  digitalWrite(pin3,LOW);
  digitalWrite(pin4,HIGH);
}
void gira_derecha(){
  digitalWrite(pin1,HIGH);
  digitalWrite(pin2,LOW);
  digitalWrite(pin3,LOW);
  digitalWrite(pin4,HIGH);
}
void gira_izquierda(){
  digitalWrite(pin1,LOW);
  digitalWrite(pin2,HIGH);
  digitalWrite(pin3,HIGH);
  digitalWrite(pin4,LOW);
}

void parametros(String f, String v, String t){
  cont = 0;
  potenciaizq = v.toInt();
  potenciader = v.toInt();
  analogWrite(pinControlizq,potenciaizq);
  analogWrite(pinControlder,potenciader);
  if(f=="adelante"){
      Adelante();
      delay(t.toInt());
      alto();
  }
  if(f=="atras"){
      Atras();
      //delay(t.toInt());
      //alto();
  }
  if(f=="izquierda"){
      gira_derecha();
      delay(t.toInt());
      alto();
  }
  if(f=="derecha"){
      gira_izquierda();
      delay(t.toInt());
      alto();
  }
  if(f=="alto"){
    alto();
  }
  Serial.println("Termine");
  funcion="";
  velocidad="";
  tiempoS="";
  
}
