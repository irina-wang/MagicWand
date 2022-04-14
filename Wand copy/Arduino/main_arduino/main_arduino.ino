#include <FastLED.h>

#define LED_PIN     6
#define NUM_LEDS    30

CRGB leds[NUM_LEDS];

/*
int red_light_pin = 47;
int green_light_pin = 48;
int blue_light_pin = 49;
*/
// serial communication
//String incoming; // for incoming serial data
char incomingByte;
char byte_mode;

void setup() {
  // put your setup code here, to run once:
  /*
  pinMode(red_light_pin, OUTPUT);
  pinMode(green_light_pin, OUTPUT);
  pinMode(blue_light_pin, OUTPUT);
  */
  
  FastLED.addLeds<NEOPIXEL, LED_PIN>(leds, NUM_LEDS);
//  led_off();
  fill_rainbow();
  FastLED.show();
  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps

}

void loop() {
//  Serial.print("incomingByte = ");
//  Serial.println(incomingByte);
  if (Serial.available() > 0) {
    incomingByte = Serial.read();
//    Serial.print("incomingByte = ");
//    Serial.println(incomingByte);
//    Serial.print("incomingByte == '1' = ");
//    Serial.println(incomingByte == '1');

    if (incomingByte == '0' || incomingByte == '6') {
      led_off();
      byte_mode = incomingByte;
    } else if (incomingByte == '1') {
       fill_red();
      byte_mode = incomingByte;
    } else if (incomingByte == '2') {
      fill_green();
      byte_mode = incomingByte;
    } else if (incomingByte == '3') {
      fill_blue();
      byte_mode = incomingByte;
    } else if (incomingByte == '4') {
      fill_purple();
    }else if (incomingByte == '5') {
      fill_orange();
    } if (incomingByte == 'x' ||
          incomingByte == 'q' ||   // q = red + green     = 1 + 2 
          incomingByte == 'w' ||   // w = red + blue      = 1 + 3 
          incomingByte == 'e' ||   // e = green + blue    = 2 + 3 
          incomingByte == 'r' ||   // r = red + purple    = 1 + 4
          incomingByte == 't' ||   // t = green + purple  = 2 + 4
          incomingByte == 'y' ||   // y = blue + purple   = 3 + 4
          incomingByte == 'a' ||   // a = red + green + blue    = 1 + 2 + 3 
          incomingByte == 's' ||   // s = red + green + purple  = 1 + 2 + 4 
          incomingByte == 'd' ||   // d = red + blue + purple   = 1 + 3 + 4 
          incomingByte == 'f' ||   // f = green + blue + purple = 2 + 3 + 4 
          incomingByte == 'z') {   // z = red + blue + green + purple = 1 + 2 + 3 + 4
      byte_mode = incomingByte;
    }
    /*
    if (incomingByte == '6'){
      fill_solid(leds, NUM_LEDS, CRGB::Purple);
//        set_all_color(CRGB::Purple); 
        RGB_color(0,255,255); // Cyan
    } else if (incomingByte == '1') {
        set_all_color(CRGB::Red); 
        RGB_color(0,255,0); // Green
    } else if (incomingByte == '2') {
        set_all_color(CRGB::Orange); 
        RGB_color(0,0,255); // Blue
    } else if (incomingByte == '0') {
        set_all_color(CRGB::Yellow); 
        RGB_color(255,255,0); // Yellow
    } else if (incomingByte == '4') {
        set_all_color(CRGB::Green); 
        RGB_color(255,0,255); // Magenta
    } else if (incomingByte == '5') {
        set_all_color(CRGB::Blue); 
        RGB_color(255,0,0); // Red   
    } else {
      RGB_color(255,255,255); // White
    } 
    */
    /*
    if (incomingByte == '6'){
        RGB_color(0,255,255); // Cyan
    } else if (incomingByte == '1') {
        RGB_color(0,255,0); // Green
    } else if (incomingByte == '2') {
        RGB_color(0,0,255); // Blue
    } else if (incomingByte == '0') {
        RGB_color(255,255,0); // Yellow
    } else if (incomingByte == '4') {
        RGB_color(255,0,255); // Magenta
    } else if (incomingByte == '5') {
        RGB_color(255,0,0); // Red   
    } else {
      RGB_color(255,255,255); // White
    } */
    

  } 


  
  if (byte_mode == 'x') { // 1 + 2 = red + green
      fill_rainbow();
  } else if (byte_mode == 'q') { // 1 + 2 = red + green
      int rand_n = random(2);
//      Serial.println(rand_n);
      if (rand_n == 0) {
        fill_red();
      } else {
        fill_green();
      }
    } else if (byte_mode == 'w') { // 1 + 3 = red + blue
      int rand_n = random(2);
//      Serial.println(rand_n);
      if (rand_n == 0) {
        fill_red();
      } else {
        fill_blue();
      }
    } else if (byte_mode == 'e') { // 2 + 3 = green + blue
      int rand_n = random(2);
//      Serial.println(rand_n);
      if (rand_n == 0) {
        fill_blue();
      } else {
        fill_green();
      }
    } else if (byte_mode == 'r') { // 1 + 4 = red + purple
      int rand_n = random(2);
//      Serial.println(rand_n);
      if (rand_n == 0) {
        fill_red();
      } else {
        fill_purple();
      }
    } else if (byte_mode == 't') { // 2 + 4 = green + purple
      int rand_n = random(2);
//      Serial.println(rand_n);
      if (rand_n == 0) {
        fill_purple();
      } else {
        fill_green();
      }
    } else if (byte_mode == 'y') { // 3 + 4 = blue + purple
      int rand_n = random(2);
//      Serial.println(rand_n);
      if (rand_n == 0) {
        fill_blue();
      } else {
        fill_purple();
      }
    } else if (byte_mode == 'a') { // 1 + 2 + 3 = red + green + blue
      int rand_n = random(3);
//      Serial.println(rand_n);
      if (rand_n == 0) {
        fill_red();
      } else if (rand_n == 1) {
        fill_green();
      } else {
        fill_blue();
      }
    } else if (byte_mode == 's') { // 1 + 2 + 4 = red + green + purple
      int rand_n = random(3);
//      Serial.println(rand_n);
      if (rand_n == 0) {
        fill_red();
      } else if (rand_n == 1) {
        fill_green();
      } else {
        fill_purple();
      }
    } else if (byte_mode == 'd') { // 1 + 3 + 4 = red + blue + purple
      int rand_n = random(3);
//      Serial.println(rand_n);
      if (rand_n == 0) {
        fill_red();
      } else if (rand_n == 1) {
        fill_purple();
      } else {
        fill_blue();
      }
    } else if (byte_mode == 'f') { // 2 + 3 + 4 = blue + green + purple
      int rand_n = random(3);
//      Serial.println(rand_n);
      if (rand_n == 0) {
        fill_purple();
      } else if (rand_n == 1) {
        fill_green();
      } else {
        fill_blue();
      }
    } else if (byte_mode == 'z') { // 1 + 2 + 3 + 4 = red + blue + green + purple
      int rand_n = random(4);
//      Serial.println(rand_n);
      if (rand_n == 0) {
        fill_red();
      } else if (rand_n == 1) {
        fill_green();
      } else if (rand_n == 2) {
        fill_blue();
      } else {
        fill_purple();
      }
    }
    FastLED.show();
//  delay(250);

}

void led_off() {
  FastLED.clear();
  Serial.println("Led off");
}

void fill_red() {
  fill_solid(leds, NUM_LEDS, CRGB::Red);
  Serial.println("Red");
}

void fill_green() {
  fill_solid(leds, NUM_LEDS, CRGB::Green);  
  Serial.println("Green");
}

void fill_blue() {
  fill_solid(leds, NUM_LEDS, CRGB::Blue);  
  Serial.println("Blue");
}

void fill_purple() {
  fill_solid(leds, NUM_LEDS, CRGB::Purple);  
  Serial.println("Purple");
}

void fill_orange(){
  fill_solid(leds, NUM_LEDS, CRGB::Orange);  
  Serial.println("Orange");
}

void fill_yellow() {
  fill_solid(leds, NUM_LEDS, CRGB::Yellow);  
  Serial.println("Yellow");
}

void fill_rainbow() {
  for (int i=0; i<NUM_LEDS; i++){
    if (i%6 == 0) {
      leds[i] = CRGB::Red;
    } else if (i%6 == 1) {
      leds[i] = CRGB::Orange;
    } else if (i%6 == 2) {
      leds[i] = CRGB::Yellow;
    } else if (i%6 == 3) {
      leds[i] = CRGB::Green;
    } else if (i%6 == 4) {
      leds[i] = CRGB::Blue;
    } else {
      leds[i] = CRGB::Purple;
    }
  }
//  leds[NUM_LEDS]
}
/*
  RGB_color(255, 0, 0); // Red
  RGB_color(0, 255, 0); // Green
  RGB_color(0, 0, 255); // Blue
  RGB_color(255, 255, 125); // Raspberry
  RGB_color(0, 255, 255); // Cyan
  RGB_color(255, 0, 255); // Magenta
  RGB_color(255, 255, 0); // Yellow


void RGB_color(int red_light_value, int green_light_value, int blue_light_value)
{
  analogWrite(red_light_pin, red_light_value);
  analogWrite(green_light_pin, green_light_value);
  analogWrite(blue_light_pin, blue_light_value);
}
*/
