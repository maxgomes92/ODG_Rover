#include "serialHandler.h"
#include "menu.h"

void setup() {}

void loop() {
  AndroidComm And(11, 10, 9600); // RX, TX, Baud
  UbuntuComm Ubu(9600); // Baud

  while(1) printMenu(And, Ubu);
}
