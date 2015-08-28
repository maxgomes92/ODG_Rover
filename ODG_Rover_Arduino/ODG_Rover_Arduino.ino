#include "serialHandler.h"
#include "menu.h"
#include "Motor.h"
#include "RC_Receiver.h"
#include "IOpins.h"

// INFORMATION FLUX
// Odroid <USB> Arduino <BLUETOOTH> Android

void setup() {
  pinMode(RC_Motor, INPUT);
  pinMode(RC_Steer, INPUT); 
}

void loop() {
  int CH[2]; // Int to receive RC signals
  
  // Object for Android communication
  AndroidComm And(TX, RX, Baud_And); // TX, RX, Baud

  // Object for Odroid/Ubuntu communication
  UbuntuComm Ubu(Baud_Ubu); // Baud
  
  // Instanciating motors
  Motor M1(M1_inA, M1_inB, M1_PWM); // inA, inB, PWM
  Motor M2(M1_inA, M1_inB, M1_PWM);
  Motor M3(M1_inA, M1_inB, M1_PWM);
  Motor M4(M1_inA, M1_inB, M1_PWM);

  // Prints menu to Android
  printMenu(And, Ubu);
  
  while(1) {
    // Receives serial data from Android
    menuEngine(And,Ubu);
    
    //Receives driving commands from RC
    RC_Receiver(CH); // CH[0] for Steering / CH[1] for Motors
    ActuateRobot(CH, M1, M2, M3, M4);
  }
}
