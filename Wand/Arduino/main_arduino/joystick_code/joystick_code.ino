//https://create.arduino.cc/projecthub/MinukaThesathYapa/arduino-thumb-joystick-to-processing-92c182

int xValue = 0 ;
int yValue = 0 ; 
int bValue = 0 ;


const int redX = 512;
const int redY = 1023;
const int greenX = 1023;
const int greenY = 0;
const int blueX = 0;
const int blueY = 0;

void setup()	
{	
	Serial.begin(9600) ;
	pinMode(8,INPUT); 
	digitalWrite(8,HIGH);	
}	

void loop()	
{	
	int xValue = analogRead(A0);	
	int yValue = analogRead(A1);	
	bValue = digitalRead(8);	
	Serial.print(xValue,DEC);
	Serial.print(",");
	Serial.print(yValue,DEC);
//	Serial.print(",");
//	Serial.print(!bValue);
	Serial.print("\n");
//	delay(10);	


  // Flip orientation (if needed)
  int xAxis = map(xValue, 0, 1023, 0, 1023);
  int yAxis = map(yValue, 0, 1023, 1023, 0);

  int distanceRed = sqrt(pow(abs(redX - xAxis), 2) +  pow(abs(redY - yAxis), 2));
  int distanceGreen = sqrt(pow(abs(greenX - xAxis), 2) +  pow(abs(greenY - yAxis), 2));
  int distanceBlue = sqrt(pow(abs(blueX - xAxis), 2) +  pow(abs(blueY - yAxis), 2));

  int brightRed = 255 - constrain(map(distanceRed, 0, 1023, 0, 255), 0, 255);
  int brightGreen = 255 - constrain(map(distanceGreen, 0, 1023, 0, 255), 0, 255);
  int brightBlue = 255 - constrain(map(distanceBlue, 0, 1023, 0, 255), 0, 255);

//  Serial.print("KEY: ");
//  Serial.print(digitalRead(PUSHBUTTON_PIN));
  Serial.print(", X: ");
  Serial.print(xAxis);
  Serial.print(", Y: ");
  Serial.print(yAxis);
  Serial.print(", R: ");
  Serial.print(brightRed);
  Serial.print(", G: ");
  Serial.print(brightGreen);
  Serial.print(", B: ");
  Serial.print(brightBlue);
  Serial.println("\n");

  delay(100);

//  if (digitalRead(PUSHBUTTON_PIN) == 0) {
//      brightRed = 255;
//      brightGreen = 255;
//      brightBlue = 255;
}
