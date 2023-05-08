#define Trig 11 //Use one trigger and 3 echos to be able to simultaenously trigger
#define Echo1 10
#define Buzzer 6
#define Motor 3 

void setup()
{ 
  pinMode(Trig, OUTPUT);
  pinMode(Echo1, INPUT);
  pinMode(Buzzer, OUTPUT);
  pinMode(Motor, OUTPUT);
}

void loop()
{ 
  float dist1, timetaken1; 
  digitalWrite(Trig, LOW); 
  delayMicroseconds(20); 
  digitalWrite(Trig, HIGH);
  delayMicroseconds(10); 
  digitalWrite(Trig, LOW);
  timetaken1 = (float) pulseIn(Echo1, HIGH);
  dist1 = ((timetaken1/2)*340)/10000;//By the formula- distance=(time/2)*speed of sound
  Serial.begin(9600);
  Serial.print("Distance: ");
  Serial.print(dist1);
  Serial.println("cm");
  if (dist1< 150) //If distance is less than 100, motor is activated
  {
    if (dist1 < 30){
      analogWrite(Buzzer, 255/5);
      analogWrite(Motor, 255);
    }
    else{
    //analogWrite(Buzzer, 255*(1 - (dist1-10)/90)/10); // turn on motor on full power (range is 0 - 255)
      analogWrite(Buzzer, (255/5)*pow(M_E, (-1)*(dist1-30)/40));
      analogWrite(Motor, (255/5)*pow(M_E, (-1)*(dist1-30)/80));
    }
  }
  else{
    analogWrite(Motor, 0);
    analogWrite(Buzzer, 0);
  }
  delay(100);
}
//add a transistor parallel to the motor, use the diagram on the document Kate made. 
//edit distance variable to get linear distance to the person
//in future edit the code so different motors vibrate at different strength, each motor corresponds with a sensor.
