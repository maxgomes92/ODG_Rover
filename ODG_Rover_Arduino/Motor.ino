Motor::Motor(int inA, int inB, int pwmPin) {
  inA_ = inA;
  inB_ = inB;
  pwmPin_ = pwmPin;
  pwm_ = 0;
  
  pinMode(inA_, OUTPUT);
  pinMode(inB_, OUTPUT);
  pinMode(pwmPin_, OUTPUT);
  
  digitalWrite(inA_, HIGH);
  digitalWrite(inB_, LOW);
};

Motor::~Motor(){};

void Motor::setPWM(int pwm) {
  this->pwm_ = pwm;
  analogWrite(pwmPin_, pwm); 
}

void Motor::Forward(int pwm) {
  digitalWrite(inA_, HIGH);
  digitalWrite(inB_, LOW);   
  
  this->pwm_ = pwm;
  setPWM(pwm);
}

void Motor::Backward(int pwm) {
  digitalWrite(inA_, LOW);
  digitalWrite(inB_, HIGH);
  
  this->pwm_ = pwm;
  setPWM(pwm);
}

int Motor::getPWM() {
  return this->pwm_;
}
