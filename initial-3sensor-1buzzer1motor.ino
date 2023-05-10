#define Trig 11 //Use one trigger and 3 echos to be able to simultaenously trigger
#define Echo1 10
#define Echo2 9
#define Echo3 5
#define Buzzer 6
#define Motor 3 

void setup()
{ 
  pinMode(Trig, OUTPUT);
  pinMode(Echo1, INPUT);
  pinMode(Echo2, INPUT);
  pinMode(Echo3, INPUT);
  pinMode(Buzzer, OUTPUT);
  pinMode(Motor, OUTPUT);
}

void loop()
{ 
  float dist1, dist2, dist3, dist; 
  float timetaken[3];
  int echo[3]={Echo1,Echo2,Echo3};
  for(int i = 0; i<3; i++){
    digitalWrite(Trig, LOW); 
    delayMicroseconds(10); 
    digitalWrite(Trig, HIGH);
    delayMicroseconds(5); 
    digitalWrite(Trig, LOW);
    timetaken[i] = (float) pulseIn(echo[i], HIGH);
    //delayMicroseconds(5); 
  }
  dist1 = ((timetaken[0]/2)*340)/10000;//By the formula- distance=(time/2)*speed of sound
  dist2 = ((timetaken[1]/2)*340)/10000;//By the formula- distance=(time/2)*speed of sound
  dist3 = ((timetaken[2]/2)*340)/10000;//By the formula- distance=(time/2)*speed of sound
  
  dist = minimum(dist1, dist2, dist3);

  Serial.begin(9600);
  //Serial.print("Distance: ");
  //Serial.println(dist);
  Serial.println(time());
  //Serial.println("cm");

  
  if (dist< 200) //If distance is less than 100, motor is activated
  {
    if (dist < 30){
      analogWrite(Buzzer, 255/2);
      analogWrite(Motor, 255);
    }
    else{
    //analogWrite(Buzzer, 255*(1 - (dist1-10)/90)/10); // turn on motor on full power (range is 0 - 255)
      analogWrite(Buzzer, (255/2)*pow(M_E, (-1)*(dist1-30)/80));
      analogWrite(Motor, (255)*pow(M_E, (-1)*(dist1-30)/40));
    }
  }
  else{
    analogWrite(Motor, 0);
    analogWrite(Buzzer, 0);
  }
  //delayMicroseconds(5); 
}

float minimum(float a, float b, float c){ float min;
  min=a;
  if(b<min&&b>0){
    min=b;
  }
  if(c<min&&c>0){
    min=c;
  }
  return min;
}
//add a transistor parallel to the motor, use the diagram on the document Kate made. 
//edit distance variable to get linear distance to the person
//in future edit the code so different motors vibrate at different strength, each motor corresponds with a sensor.
