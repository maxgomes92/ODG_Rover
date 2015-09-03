///// ODG_Rover_Arduino //////

This code intermediate the communication between Ubuntu and Android and also actuate the DC Motors through the Motor Shield.

./ODG_Rover_Arduino.ino
	Main code. Creates objects, set up pins and runs the main loop.

./ActuateMotor.ino
	This code handle the motor actuation. It can be manually (fully controlled by RC) or automatic (Python calculate trajectory and
	send to Arduino / RC controlls speed).

./IOpins.h
	Stores all pins number.

./Motor.ino
	Stores the Motor class. It's meant to be created one for each motor.

./SoftwareSerial.cpp
	Library for serial communication. It was not importing properly, I had to move
it to the project folder.

./menu.ino
	This code handles the menu interaction. This commands are sent from the Android through bluetooth to the Arduino. It handle the actions by executing the task or/and by requesting it from the Ubuntu.

./serialHandler.ino
	This code stores the UbuntuCommunication and AndroidCommunication class. They deal with the information transmission. They have functions to write, read and set up.
