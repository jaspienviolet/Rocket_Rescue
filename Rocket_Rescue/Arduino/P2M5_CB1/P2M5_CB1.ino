/*

  SparkFun P2M4 Protype
  Xing Hao Huang - huang.xingh@northeastern.edu
  Testing a bunch of stuff
  Taken from Arduino IDE Sample - SparkFun Book SIK4.1 4A & 5A
  Descriptions: Press button, turns on and off LED, score on LCD increases, motor changes directions

*/

int dataIn;


#include <LiquidCrystal.h>

LiquidCrystal lcd(2, 9, 3, 4, 5, 6); // pins connected to LCD

//PIN VARIABLES
//the motor will be controlled by the motor A pins on the motor driver
const int AIN1 = 13;            // control pin 1 on the motor driver for the right motor
const int AIN2 = 12;            // control pin 2 on the motor driver for the right motor
const int PWMA = 11;            // speed control pin on the motor driver for the right motor

const int BIN1 = 8;             // control pin 1 on the motor driver for the right motor
const int BIN2 = 7;             // control pin 2 on the motor driver for the right motor
const int PWMB = 10;            // speed control pin on the motor driver for the right motor

//VARIABLES


void setup() 
{
  Serial.begin(9600);

  lcd.begin(16,2);              // initialize dimension of LCD
  lcd.clear();                  // clears the LCD
  lcd.noCursor();

  // pin modes
  pinMode(AIN1, OUTPUT);
  pinMode(AIN2, OUTPUT);
  pinMode(PWMA, OUTPUT);
  
  pinMode(BIN1, OUTPUT);
  pinMode(BIN2, OUTPUT);
  pinMode(PWMB, OUTPUT);

}

void loop() 
{
  lcd.setCursor(0,0);
  lcd.print("Score");  
  lcd.setCursor(0,1);
  lcd.print("          ");
  delay(1000);
  char rCode[32] = {'a'};

  while(1)
  {
    if (Serial.available())
    {
      char rCode = Serial.read();
      if (rCode == 'e')
      {
        lcd.setCursor(0,1);
        lcd.print("reset");
        delay(1000);
        lcd.clear();
        break;
      }
      else
      {
        dataIn = rCode - '0';
      }

      if (dataIn > 0)
      {
        spinMotor(dataIn);
        delay(3000);
        spinMotor(-dataIn);
        Serial.print('d');
        Serial.print('\n');
      }

    }
  }
}

/********************************************************************************/

void spinMotor(int time)            // function for driving the right motor
{
  int motorSpeed = 254;
  int i;
  int speed = motorSpeed;
  int score = 0;
  
  if (time > 0)                     // if the motor should drive forward (positive speed)
  {
    digitalWrite(AIN1, HIGH);             // set pin 1 to high
    digitalWrite(AIN2, LOW);              // set pin 2 to low
    digitalWrite(BIN1, HIGH);             // set pin 1 to high
    digitalWrite(BIN2, LOW);              // set pin 2 to low
  }
  else if (time < 0)                // if the motor should drive backward (negative speed)
  {
    digitalWrite(AIN1, LOW);              // set pin 1 to low
    digitalWrite(AIN2, HIGH);             // set pin 2 to high
    digitalWrite(BIN1, LOW);              // set pin 1 to low
    digitalWrite(BIN2, HIGH);             // set pin 2 to high
  }
  else                                    // if the motor should stop
  {
    digitalWrite(AIN1, LOW);              // set pin 1 to low
    digitalWrite(AIN2, LOW);              // set pin 2 to low
    digitalWrite(BIN1, LOW);              // set pin 1 to low
    digitalWrite(BIN2, LOW);              // set pin 2 to low
  }

  if (time > 0)
  {
    for (i = 0; i < time; i++)
    {
      lcd.setCursor(0,1);
      analogWrite(PWMA, motorSpeed);     // now that the motor direction is set, drive it at the entered speed
      analogWrite(PWMB, motorSpeed);
      lcd.print(score);
      score += 1;
      delay(500);
    }
    analogWrite(PWMA, motorSpeed); 
    analogWrite(PWMB, motorSpeed);
    lcd.setCursor(0,1);
    lcd.print(time);
    delay(500);
  }

  if (time < 0)
  {
    for (i = 0; i < abs(time); i++)
    {
      analogWrite(PWMA, motorSpeed);     // now that the motor direction is set, drive it at the entered speed
      analogWrite(PWMB, motorSpeed);
      delay(500);
    }
    analogWrite(PWMA, motorSpeed); 
    analogWrite(PWMB, motorSpeed);
    delay(500);
  }
  analogWrite(PWMA, 0);
  analogWrite(PWMB, 0);
}
