#include "RC_Receiver.h"

void RC_Receiver(int * ch) {
  ch[0] = pulseIn(RC_Steer, HIGH, 25000);
  ch[1] = pulseIn(RC_Motor, HIGH, 25000);
}

