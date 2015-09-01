#include "ActuateMotor.h"
#include "Motor.h"

#define debug 0

void ActuateRobot(int RC_Signal[], Motor M1, Motor M2, Motor M3, Motor M4) {
  int pwm=0;
  int pwmSteerWheel=0;
  
  int toSteer = RC_Signal[0];
  int toSpeedUP = RC_Signal[1];
  
  //Serial.print(toSteer);
  //Serial.print(" ");
  //Serial.println(toSpeedUP);
  
  // For going forward and turning right
  if(toSpeedUP > minFw && toSpeedUP <= maxFw && toSteer > minTnRight && toSteer <= maxTnRight) {
    pwmSteerWheel = map(toSpeedUP, minFw, maxFw, 0, 100) + 
                    map(toSteer, minTnRight, maxTnRight, 40, 155);
    pwm = map(toSpeedUP, minFw, maxFw, 0, 100);
    
    M1.Forward(pwm);
    M2.Forward(pwmSteerWheel);
    M3.Forward(pwm);
    M4.Forward(pwmSteerWheel);    
    
    
    if(debug) Serial.println("Forward and Turning right.");    
  }
  // For going foward and turning left
  else if(toSpeedUP > minFw && toSpeedUP <= maxFw && toSteer < maxTnLeft && toSteer >= minTnLeft) {
    pwmSteerWheel = map(toSpeedUP, minFw, maxFw, 0, 100) + 
                    map(toSteer, maxTnLeft, minTnLeft, 40, 155);
    pwm = map(toSpeedUP, minFw, maxFw, 0, 100);
    
    M1.Forward(pwmSteerWheel);
    M2.Forward(pwm);
    M3.Forward(pwmSteerWheel);
    M4.Forward(pwm);    
    
    if(debug) Serial.println("Forward and turning left.");
  }

// ------------
  // For going backward and turning right
  else if(toSpeedUP > minBw && toSpeedUP <= maxBw && toSteer > minTnRight && toSteer <= maxTnRight) {
    pwmSteerWheel = map(toSpeedUP, maxBw, minBw, 0, 100) + 
                    map(toSteer, minTnRight, maxTnRight, 40, 155);
    pwm = map(toSpeedUP, maxBw, minBw, 0, 100);
    
    M1.Backward(pwm);
    M2.Backward(pwmSteerWheel);
    M3.Backward(pwm);
    M4.Backward(pwmSteerWheel);    
    
    
    if(debug) Serial.println("Backward and Turning right.");    
  }
  // For going backward and turning left
  else if(toSpeedUP > minBw && toSpeedUP <= maxBw && toSteer < maxTnLeft && toSteer >= minTnLeft) {
    pwmSteerWheel = map(toSpeedUP, maxBw, minBw, 0, 100) + 
                    map(toSteer, maxTnLeft, minTnLeft, 40, 155);
    pwm = map(toSpeedUP, maxBw, minBw, 0, 100);
    
    M1.Backward(pwmSteerWheel);
    M2.Backward(pwm);
    M3.Backward(pwmSteerWheel);
    M4.Backward(pwm);    
    
    if(debug) Serial.println("Backward and turning left.");
  }

// -----------
  
  // For going forward
  else if(toSpeedUP > minFw && toSpeedUP < maxFw) {
    pwm = map(toSpeedUP, minFw, maxFw, 40, 255);
    M1.Forward(pwm);
    M2.Forward(pwm);
    M3.Forward(pwm);
    M4.Forward(pwm);   
  
    if(debug) Serial.println("Forward.");    
  }
  // For going backward
  else if(toSpeedUP < maxBw && toSpeedUP > minBw) {
    pwm = map(toSpeedUP, maxBw, minBw, 40, 255);   
    M1.Backward(pwm);
    M2.Backward(pwm);
    M3.Backward(pwm);
    M4.Backward(pwm);
    
    if(debug) Serial.println("Backward.");     
  }  
  
  // For turning right
  else if(toSteer > minTnRight && toSteer <= maxTnRight) {
    pwm = map(toSteer, minTnRight, maxTnRight, 0, 200);   
    M1.Backward(pwm);
    M3.Backward(pwm);
    M2.Forward(pwm);
    M4.Forward(pwm);
    
    if(debug) Serial.println("Turn right.");     
  } 
  // For turning left
  else if(toSteer < maxTnLeft && toSteer >= minTnLeft) {
    pwm = map(toSteer, maxTnLeft, minTnLeft, 0, 200);   
    M2.Backward(pwm);
    M4.Backward(pwm);
    M1.Forward(pwm);
    M3.Forward(pwm);
    
    if(debug) Serial.println("Turn left.");      
  }   
  
  else {
    M1.setPWM(0);
    M2.setPWM(0);
    M3.setPWM(0);
    M4.setPWM(0);  
  }
  
  //Serial.print(pwm);
  //Serial.print(" ");
  //Serial.println(pwmSteerWheel);
}

void AutoRobot(int RC_Signal[], Motor M1, Motor M2, Motor M3, Motor M4, AndroidComm& And, UbuntuComm& Ubu) {
  String msg = Ubu.readString();
  
  int pwm=0;
  int toSteer = RC_Signal[1];
  int toSpeedUP = RC_Signal[1];  
  
  if(toSpeedUP > 800 || toSpeedUP < 1800) {
  } else if(msg == "fw") {
    pwm = map(toSpeedUP, minFw, maxFw, 20, 200);
    M1.Forward(pwm);
    M2.Forward(pwm);
    M3.Forward(pwm);
    M4.Forward(pwm); 
    //And.println("Forward.");
  } else if(msg == "bw") {
    pwm = map(toSpeedUP, maxBw, minBw, 20, 200);   
    M1.Backward(pwm);
    M2.Backward(pwm);
    M3.Backward(pwm);
    M4.Backward(pwm);    
  } else if(msg == "tr") {
    pwm = map(toSteer, minTnRight, maxTnRight, 0, 200);   
    M1.Backward(pwm);
    M3.Backward(pwm);
    M2.Forward(pwm);
    M4.Forward(pwm);    
    //And.println("Turn right.");
  } else if(msg == "tl") {
    pwm = map(toSteer, maxTnLeft, minTnLeft, 0, 200);   
    M2.Backward(pwm);
    M4.Backward(pwm);
    M1.Forward(pwm);
    M3.Forward(pwm);    
  }
}
