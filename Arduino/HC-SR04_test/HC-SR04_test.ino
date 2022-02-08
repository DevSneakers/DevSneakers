#include <LiquidCrystal_I2C.h>
#include <Wire.h>
#include <NewPing.h>

// RGB LED
int redled = 2;
int greenled = 3;
int blueled = 4;

// 초음파 센서
int trigPin = 6;                          // 초음파 발신
int echoPin = 7;                          // 초음파 수신

// 능동부저
int speaker = 8;

// LCD
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  Serial.begin(9600);                     // serial bitrate
  pinMode(echoPin, INPUT);
  pinMode(trigPin, OUTPUT);

  pinMode(redled, OUTPUT);
  pinMode(greenled, OUTPUT);
  pinMode(blueled, OUTPUT);

  pinMode(speaker, OUTPUT);

  lcd.init();
}

void loop() {
  lcd.backlight();
  long dur, dis;
  digitalWrite(trigPin, HIGH);
  delay(10);
  digitalWrite(trigPin, LOW);

  dur = pulseIn(echoPin, HIGH);         // echoPin이 HIGH를 Hold한 시간
  dis = ((float)(340*dur)/10000)/2;


  Serial.print("Duration : ");
  Serial.println(dur);
  Serial.print("Distance : ");
  Serial.print(dis);
  Serial.println("cm\n");
  delay(100);

  if(dis <= 10){
    setColor(255, 0 , 0);
    digitalWrite(speaker, HIGH);
  }
  else if(dis <= 30){
    setColor(0, 255, 0);
    digitalWrite(speaker, HIGH);
    delay(100);
    digitalWrite(speaker, LOW);
  }
  else{
    setColor(0, 0, 255);
  }

  lcd.setCursor(0,0);
  lcd.print("Distance");
  lcd.setCursor(0,1);
  lcd.print("-> ");
  lcd.print(dis);
  lcd.print(" CM ");
}

void setColor(int red, int green, int blue) {
  analogWrite(redled, red);
  analogWrite(greenled, green);
  analogWrite(blueled, blue);
}
