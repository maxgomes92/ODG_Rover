#ifndef ACTUATEMOTOR_H
#define ACTUATEMOTOR_H


// Based on signal received from RC
#define maxFw 1700
#define minFw 1350
#define maxBw 1300
#define minBw 950

#define maxTnRight 1660
#define minTnRight 1320
#define maxTnLeft 1260
#define minTnLeft 920


// Receives RC signals and interprets them
void ActuateRobot(int RC_Signal[], Motor M1, Motor M2, Motor M3, Motor M4);

#endif // ACTUATEMOTOR_H
