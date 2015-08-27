#include "serialHandler.h"

AndroidComm::AndroidComm(int rx, int tx, int baud): 
BlueTooth(rx, tx) { 
  _rx = rx;
  _tx = tx;
  _baud = baud;

  BlueTooth.begin(baud);
  while(BlueTooth.available())  BlueTooth.read();  // empty RX buffer
}

AndroidComm::~AndroidComm() {}

String AndroidComm::readString() {
  if (BlueTooth.available()) {
    String btMSG = BlueTooth.readString();
    return btMSG;  
  }
  else return NULL;
}

void AndroidComm::println(String msg) {
  BlueTooth.println(msg); 
}

void AndroidComm::print(String msg) {
  BlueTooth.print(msg); 
}

// ------------------------------------------------

UbuntuComm::UbuntuComm(int baud) {
  _baud = baud;

  Serial.begin(baud);  
}

UbuntuComm::~UbuntuComm() {}

String UbuntuComm::readString() {
  if(Serial.available()>0) {
    String PythonMSG = Serial.readStringUntil(']');

    return PythonMSG;
  } 
  else return NULL;    
}

void UbuntuComm::print(String msg) {
  // Char to indicate when the Ubuntu has to consider
  // the message. Because it also gets the message that
  // goes to the Android
  String foo = "]"; 
  foo.concat(msg);
  Serial.println(foo);
}


