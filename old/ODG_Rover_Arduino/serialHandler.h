#ifndef SERIALHANDLER_H
#define SERIALHANDLER_H

#include "SoftwareSerial.h"

class AndroidComm {
  public:
    AndroidComm(int rx, int tx, int baud);
    ~AndroidComm();
  
  // Gets message from Android device and return it  
  String readString(); 
  void print(String msg);
  void println(String msg); 
  
  private:
    int _rx, _tx, _baud;
    SoftwareSerial BlueTooth;
};

class UbuntuComm {
  public:
    UbuntuComm(int baud);
    ~UbuntuComm();
   
    String readString(); // Gets message from Cpp code and return it
    void print(String msg);
  
  private:
    int _baud;
};

#endif // SERIALHANDLER_H
