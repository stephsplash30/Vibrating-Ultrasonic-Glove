#define Trig 11 //Use one trigger and 3 echos to be able to simultaenously trigger
#define Echo1 10

void setup()
{ 
  pinMode(Trig, OUTPUT);
  pinMode(Echo1, INPUT);
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
  delay(500);
}
//add a transistor parallel to the motor, use the diagram on the document Kate made. 
//edit distance variable to get linear distance to the person
//in future edit the code so different motors vibrate at different strength, each motor corresponds with a sensor.
