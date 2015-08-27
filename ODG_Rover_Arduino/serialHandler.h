#ifndef SERIALHANDLER_H
#define SERIALHANDLER_H

#include "SoftwareSerial.h"

class AndroidComm {
  public:
    AndroidComm(int rx, int tx, int baud);
    ~AndroidComm();
  
  // Gets message from Android device and return it  
  String readString(); 
  
  // Prints string to Android without \n
  void print(String msg);
  
  // Prints string to Android with \n
  void println(String msg); 
  
  private:
    int _rx, _tx, _baud;
    SoftwareSerial BlueTooth;
};

class UbuntuComm {
  public:
    UbuntuComm(int baud);
    ~UbuntuComm();
   
    // Gets message from Odroid(Ubuntu) and return it
    String readString(); 
    
    // Prints message through serial to Odroid
    void print(String msg);
  
  private:
    int _baud; // baud rate
};

#endif // SERIALHANDLER_H
