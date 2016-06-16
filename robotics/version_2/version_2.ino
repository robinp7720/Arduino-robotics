/* Include the software serial port library */
#include <SoftwareSerial.h>
/* to communicate with the Bluetooth module's TXD pin */
#define BT_SERIAL_TX 12
/* to communicate with the Bluetooth module's RXD pin */
#define BT_SERIAL_RX 13
/* Initialise the software serial port */
SoftwareSerial BluetoothSerial(BT_SERIAL_TX, BT_SERIAL_RX);

//Motor A enable = pin 2
int M_A_E = 3;
//Motor A IN1    = pin 2
int M_A_IN1 = 6;
//Motor A IN2    = pin 3
int M_A_IN2 = 5;

//Motor B enable = pin 4
int M_B_E = 11;
//Motor B IN3    = pin 5
int M_B_IN3 = 9;
//Motor B IN4    = pin 6
int M_B_IN4 = 10;

int steer = 0;
int motor_speed = 0;

void setup() {
  pinMode(M_A_E, OUTPUT);
  pinMode(M_A_IN1, OUTPUT);
  pinMode(M_A_IN2, OUTPUT);
  pinMode(M_B_E, OUTPUT);
  pinMode(M_B_IN3, OUTPUT);
  pinMode(M_B_IN4, OUTPUT);

  Serial.begin(9600); // Initialise BlueTooth

  Serial.print("Starting ...");
}

void brake(char motor) {
  if (motor == 'A') {
    digitalWrite(M_A_IN1, LOW);
    digitalWrite(M_A_IN2, LOW);
  }
  if (motor == 'B') {
    digitalWrite(M_B_IN3, LOW);
    digitalWrite(M_B_IN4, LOW);
  }
}

void forward(char motor) {
  if (motor == 'A') {
    digitalWrite(M_A_IN1, HIGH);
    digitalWrite(M_A_IN2, LOW);
  }
  if (motor == 'B') {
    digitalWrite(M_B_IN3, HIGH);
    digitalWrite(M_B_IN4, LOW);
  }
}

void backward(char motor) {
  if (motor == 'A') {
    digitalWrite(M_A_IN1, LOW);
    digitalWrite(M_A_IN2, HIGH);
  }
  if (motor == 'B') {
    digitalWrite(M_B_IN3, LOW);
    digitalWrite(M_B_IN4, HIGH);
  }
}

void loop() {
  while (Serial.available() == 0);

  int val = Serial.parseInt(); //read int or parseFloat for ..float...

  if (val > 0) {
      Serial.println(val);

      // say what you got:
      Serial.print("I got: ");
      Serial.println(val);

      if (val < 1000) {
        motor_speed = val;
      }
      if (val >= 1000) {
        steer = val - 2000;
      }

      forward('A');
      forward('B');

      analogWrite(M_A_E, motor_speed+steer);
      analogWrite(M_B_E, motor_speed-steer);
    }
}
