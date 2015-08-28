#ifndef MOTOR_H
#define MOTOR_H

// Motors disposition
//
// M2 --- M1
//    ---
// M4 --- M3

class Motor {
  public:
    // Constructor sets pins
    Motor(int inA, int inB, int pwmPin);
    ~Motor();
    
    void setPWM(int pwm);
    void Forward(int pwm);
    void Backward(int pwm);
    int getPWM();
  private:
    int inA_, inB_, pwmPin_, pwm_;
};

#endif // MOTOR_H
