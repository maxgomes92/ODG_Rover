///// ODG_Rover_Python //////
	This software is integrated with the Arduino. It receives commands coming 
	from it and executes tasks, such as, running Piksi console and streamming a file.

./startup_code.py
	This code file is meant to be called everytime the Ubuntu starts up. becase
	 if you have no monitor connected to the Odroid, the code is already running 
	 ready to get commands coming from the Arduino. It calls the ./__init__.py in a loop so if it breaks, it will be called again.

./__init__.py
	 This code gets command from Arduino and interprets them by executing the 
	 task or by calling the responsible function.

./menu.py
	This file stores most of the functions called by ./__init__.py. More detailed 
	information about each function can be found in the file.

./ArduinoComm.py
	This code stores the class for the serial communication with the Arduino. 
	It has a function to set it up, to read from and to write to.

./settings.py
	This code stores the Arduino and Piksi USB path as well as their baud rate.

./AutoRobot.py
	This code has the functions for the Robot auto mobility. It works by comparing 
	the angle the Robot went to the angle it should have gone. Then it attempts to 
	correct this difference by rotating itself. The first angle is calculated by 
	relating the current position to the previous position and the second by relation 
	the destination to the previous position as well.


