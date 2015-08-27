#include "serialHandler.h"
#include "menu.h"

// INFORMATION FLUX
// Odroid <USB> Arduino <BLUETOOTH> Android

void setup() {}

void loop() {
  AndroidComm And(11, 10, 9600); // RX, TX, Baud
  UbuntuComm Ubu(9600); // Baud

  printMenu(And, Ubu);
  
  while(1) {
    menuEngine(And,Ubu);
  }
}
