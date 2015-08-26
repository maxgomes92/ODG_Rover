/////// INSTRUCTIONS TO GET && RUN THE SOFTWARE ////////

// ------------------ GENERAL
This software was developed to integrate the Odroid with the Arduino.
Both will be placed in the Rover Robot.
Since there will be no way to have a monitor hocked up to it, the Arduino
communicates with the Android.
The Android runs a apk from the Google Play Store named Bluetooth Terminal (v1.2).
It can be found at: https://goo.gl/8Gk4KA
Through the Android you can interact and command the Odroid by sending
commands to the Arduino, who will interpret it and send the necessary
information to the Odroid.
	
// ------------------ TO GET
1-Clone the projects:
	Clone this project in any folder.
		$ git clone http://github.com/maxgomes92/ODG_Rover
	
	Clone this project in .../ODG_Rover/
		$ git clone https://github.com/swift-nav/piksi_tools.git
	
	Folders structure:
		.../ODG_Rover/ODG_Rover_Arduino
		.../ODG_Rover/ODG_Rover_Python
		.../ODG_Rover/piksi_tools	

// ------------------ TO RUN
2-ODG_Rover_Arduino (.../ODG_Rover/ODG_Rover_Arduino/)
	Just turn on the Arduino.
	To edit the code using the Arduino IDE, open the 
	file ODG_Rover_Arduino.ino 
	
3-ODG_Rover_Python (be at .../ODG_Rover/ODG_Rover_Python)
	To run the code:
		$ python __init__.py
	
	To run the code in a loop that calls it back
	if __init__.py stops running:
		python startup_code.py
	This file was set as a start up application.
	The intention is to have it running in case of
	no monitor is present.
	To stop the code from running in the background:
		$ killall python
		
// ------------------ USAGE
The Arduino must be connected to the Odroid USB port.
Everytime you start the Python code, the Arduino will reset.
The system runs normally whether the Android is connected to the 
Bluetooth device or not.

-> Step-by-Step

- Plug the Arduino to the Odroid USB;
- Turn on the Odroid;
- Connect the Android to the Bluetooth (if it's the first time, you will
- have to pair it first, password is 1234 or 0000);
- Log into the Odroid (if the code is still set to run automatically
  you won't need to do the next stetp);
- Go the .../ODG_Rover/ODG_Rover_Python, open the terminal and type in:
	python startup_code.py

If everything is OK, you will receive this on your Android app:

--> Piksi Integration Software
1. Run Console
2. Choose CSV to read
3. Delete all CSV files
4. Start Streamming
5. Save a spot
9. Reset Python Code
0. Shut down ODROID

Whenever you type in "menu" you will get this on your Android app.

You command by typing in the option number.
Functions:
1- Runs the Piksi console on Odroid.
2- To choose the CSV log files you want to save.
3- Deletes all CSV log files placed at .../ODG_Rover/piksi_console/*.csv
4. Starts streamming the CSV log files chosen in option 3.
5. Saves the current log data from the CSV log files chosen in option 3.
9. Resets the Python code. You will receive the menu again after reseting it.
0. Shuts down the ODROID (requires SUDO).

If you want to test in, after running the console, goes to Settings and 
enable the simulation mode by switching it to True.
For more info: http://docs.swiftnav.com/wiki/Piksi_User_Getting_Started_Guide
