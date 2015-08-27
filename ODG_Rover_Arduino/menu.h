#ifndef MENU_H
#define MENU_H

#include <ctype.h>
#include "serialHandler.h"

// Prints menu to Android and calls menuEngine()
void printMenu(AndroidComm& And, UbuntuComm& Ubu);

// Gets input from Android and treats it.
// If required, it dealls with the Odroid.
void menuEngine(AndroidComm& And, UbuntuComm& Ubu);

// Clear any data in the buffer between the Odroid(Ubuntu) and the Arduino
void clearBuffer(UbuntuComm& Ubu);

// Gets the chosen CSV log file, returns zero if, for any reason,
// no valid file is chosen. Returns 1 if it succeed.
int getChosenFile(String files[2], AndroidComm& And, UbuntuComm& Ubu);

#endif // MENU_H
