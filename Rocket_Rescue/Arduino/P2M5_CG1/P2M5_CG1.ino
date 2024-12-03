/*

  Final Code for P2M7 -- File Name not renamed from prior file
  Xing Hao Huang - huang.xingh@northeastern.edu
  Component Grid 1
  Descriptions: Read changes in limit switches / buttons, sends code through Serial
  Change for b1 through b9, change all digitalRead == HIGH to change to detect lifting up pieces instead of pressing down siwtches

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
    if (row1 == 0) // detects changes to first row, only activates if no changes have occurred
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
    if (row2 == 0) // detects changes to second row, only activates if no changes have occurred
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
    if (row3 == 0) // detects changes to third row, only activates if no changes have occurred
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
      Serial.print('s'); // Component Grid 1 Sound for first row
      Serial.print(',');
      Serial.print(s1);
      Serial.print('\n');
      s1 = 0;
      info += 1;
      delay(500);
    }

    if (s2 != 0)
    {
      Serial.print('s'); // Component Grid 1 Sound for second row
      Serial.print(",");
      Serial.print(s2);
      Serial.print('\n');
      s2 = 0;
      info += 1;
      delay(500);
    }

    if (s3 != 0)
    {
      Serial.print('s'); // Component Grid 1 Sound for third row
      Serial.print(',');
      Serial.print(s3);
      Serial.print('\n');
      s3 = 0;
      info += 1;
      delay(500);
    }
  }

    Serial.print("c"); // Component Grid 1 Check
    Serial.print(","); // sends selected component choices through Serial
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
   

    if (bL == LOW) // if launch button is pressed, tell Serial
    {
      Serial.print('L');
      Serial.print('\n');
      delay(500);
    }
    if (bR == LOW) // if reset button is pressed, tell Serial
    {
      Serial.print('r');
      Serial.print('\n');
      delay(500);
    }

    // checks if components are in correct position to reset
    b1 = digitalRead(button1);
    b2 = digitalRead(button2);
    b3 = digitalRead(button3);
    b4 = digitalRead(button4);
    b5 = digitalRead(button5);
    b6 = digitalRead(button6);
    b7 = digitalRead(button7);
    b8 = digitalRead(button8);
    b9 = digitalRead(button9);

    // comment out if buttons are meant to be in HIGH for reset
    b1 = !b1;
    b2 = !b2;
    b3 = !b3;
    b4 = !b4;
    b5 = !b5;
    b6 = !b6;
    b7 = !b7;
    b8 = !b8;
    b9 = !b9; 
    // comment out if buttons are meant to be in HIGH for reset

    bS = b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8 + b9;

    if (Serial.available())
    {
      if ((rCode == 'r') & (bS == 0)) // if components are in right position, allow for reset
      {
        Serial.print('g'); // Component Grid 1 Good
        Serial.print('\n');
        break;
      }
      if ((rCode == 'r') & (bS != 0)) // if components are in right position, do not allow for reset
      {
        Serial.print('b'); // Component Grid 1 Bad
        Serial.print('\n');
        delay(2000);
      }
    }
  }
}
