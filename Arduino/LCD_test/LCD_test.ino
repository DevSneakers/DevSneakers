#include <LiquidCrystal_I2C.h>
#include <Wire.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

int dis = 5;

void setup() {
lcd.init();
}

void loop() {
lcd.backlight();
lcd.setCursor(0,0);
lcd.print("welcom to home");
lcd.setCursor(0,1);
lcd.print("thank you");
}
