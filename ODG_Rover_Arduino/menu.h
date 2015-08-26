#ifndef MENU_H
#define MENU_H

#include <ctype.h>
#include "serialHandler.h"

// Prints menu to Android
void printMenu(AndroidComm& And, UbuntuComm& Ubu);

// Gets menu option from Android
void menuEngine(AndroidComm& And, UbuntuComm& Ubu);

void clearBuffer(UbuntuComm& Ubu);

int getChosenFile(String files[2], AndroidComm& And, UbuntuComm& Ubu);

#endif // MENU_H
