/*

  SparkFun P2M4 Protype
  Xing Hao Huang - huang.xingh@northeastern.edu
  Testing a bunch of stuff
  Taken from Arduino IDE Sample - SparkFun Book SIK4.1 4A & 5A
  Descriptions: Press button, turns on and off LED, score on LCD increases, motor changes directions

*/

const int buttonLaunch = 11;              
const int buttonReset = 12;              

const int button1 = 2;            // button pin
const int button2 = 3;            // button pin
const int button3 = 4;            // button pin
const int button4 = 5;            // button pin
const int button5 = 6;            // button pin
const int button6 = 7;            // button pin
const int button7 = 8;            // button pin
const int button8 = 9;            // button pin
const int button9 = 10;           // button pin
//VARIABLES

void setup() 
{
  Serial.begin(9600);
  // pin modes
  pinMode(button1, INPUT_PULLUP);
  pinMode(button2, INPUT_PULLUP);
  pinMode(button3, INPUT_PULLUP);
  pinMode(button4, INPUT_PULLUP);
  pinMode(button5, INPUT_PULLUP);
  pinMode(button6, INPUT_PULLUP);
  pinMode(button7, INPUT_PULLUP);
  pinMode(button8, INPUT_PULLUP);
  pinMode(button9, INPUT_PULLUP);

  pinMode(buttonLaunch, INPUT_PULLUP);
  pinMode(buttonReset, INPUT_PULLUP);

}

void loop() 
{
  
  bool bS = 0;
  int row1 = 0;
  int row2 = 0;
  int row3 = 0;
  int info = 0;
  int s1 = 0;
  int s2 = 0;
  int s3 = 0;
  bool b1, b2, b3, b4, b5, b6, b7, b8, b9, bR, bL;
  char rCode[32] = {'a'};

  while (info < 3)
  {
    if (row1 == 0)
    {

      b1 = digitalRead(button1);
      b2 = digitalRead(button2);
      b3 = digitalRead(button3);

      if (b1 == LOW) 
      {
        row1 = 1;
        s1 = 1;
      }
      else if (b2 == LOW)
      {
        row1 = 2;
        s1 = 2;
      }
      else if (b3 == LOW)
      {
        row1 = 3;
        s1 = 3;
      }
    }
    if (row2 == 0)
    {
      b4 = digitalRead(button4);
      b5 = digitalRead(button5);
      b6 = digitalRead(button6);

      if (b4 == LOW)
      {
        row2 = 4;
        s2 = 4;
      }
      else if (b5 == LOW)
      {
        row2 = 5;
        s2 = 5;
      }
      else if (b6 == LOW)
      {
        row2 = 6;
        s2 = 6;
      }
    }
    if (row3 == 0)
    {
      b7 = digitalRead(button7);
      b8 = digitalRead(button8);
      b9 = digitalRead(button9);

      if (b7 == LOW)
      {
        row3 = 7;
        s3 = 7;
      }
      else if (b8 == LOW)
      {
        row3 = 8;
        s3 = 8;
      }
      else if (b9 == LOW)
      {
        row3 = 9;
        s3 = 9;
      }
    }

    if (s1 != 0)
    {
      Serial.print('s'); // Component Grid 1 Sound
      Serial.print(',');
      Serial.print(s1);
      Serial.print('\n');
      s1 = 0;
      info += 1;
      delay(500);
    }

    if (s2 != 0)
    {
      Serial.print('s'); // Component Grid 1 Sound
      Serial.print(",");
      Serial.print(s2);
      Serial.print('\n');
      s2 = 0;
      info += 1;
      delay(500);
    }

    if (s3 != 0)
    {
      Serial.print('s'); // Component Grid 1 Sound
      Serial.print(',');
      Serial.print(s3);
      Serial.print('\n');
      s3 = 0;
      info += 1;
      delay(500);
    }
  }

    Serial.print("c"); // Component Grid 1 Check
    Serial.print(",");
    Serial.print(row1);
    Serial.print(',');
    Serial.print(row2);
    Serial.print(',');
    Serial.print(row3);
    Serial.print('\n');

    delay(500);
  
  while (info == 3)
  {
    char rCode = Serial.read();

    bL = digitalRead(buttonLaunch);
    bR = digitalRead(buttonReset);
   

    if (bL == LOW)
    {
      Serial.print('L');
      Serial.print('\n');
      delay(500);
    }
    if (bR == LOW)
    {
      Serial.print('r');
      Serial.print('\n');
      delay(500);
    }

    b1 = digitalRead(button1);
    b2 = digitalRead(button2);
    b3 = digitalRead(button3);
    b4 = digitalRead(button4);
    b5 = digitalRead(button5);
    b6 = digitalRead(button6);
    b7 = digitalRead(button7);
    b8 = digitalRead(button8);
    b9 = digitalRead(button9);

    b1 = !b1;
    b2 = !b2;
    b3 = !b3;
    b4 = !b4;
    b5 = !b5;
    b6 = !b6;
    b7 = !b7;
    b8 = !b8;
    b9 = !b9;       

    bS = b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8 + b9;

    if (Serial.available())
    {
      if ((rCode == 'r') & (bS == 0))
      {
        Serial.print('g'); // Component Grid 1 Good
        Serial.print('\n');
        break;
      }
      if ((rCode == 'r') & (bS != 0))
      {
        Serial.print('b'); // Component Grid 1 Bad
        Serial.print('\n');
        delay(2000);
      }
    }
  }

}

/********************************************************************************/






