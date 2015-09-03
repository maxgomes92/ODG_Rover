import subprocess, time
import sys, inspect, os, signal, serial

from ArduinoComm import *
from menu import *
from settings import *
from AutoRobot import *

def main():
	# When false, means robot will be fully controlled by RC
	AutoDrive = False
	
	# To save spots (they will be used to tell the Robot which place to go autonomouslly)
	spotsSaved = {}
	
	# Sets up communication with Arduino
	Ard = ArduinoComm(USB_Arduino, Baud_Arduino)
	
	# List to hold files name
	toStream = ['',''] # [0] baseline / [1] position	
	
	# Finds out its own path
	python_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
	root_path = ""
	root_path = python_path[:len(root_path)-17]	# Removing last folder's name
	
	# Initiating dicionary to store Robot coordinates
	RobotCoord = {'N':0, 'E':0, 'D':0, 'Dist':0, 'nSat':0, 'Flag':0, 'Lat':0, 'Lon':0}
	oldRobotCoord = {'N':0, 'E':0}
		
	# Receives Instruction from Arduino
	try:	
		while True:
			# Attempts to receive instruction from Arduino
			opt = Ard.read()
			
			# Processes instruction
			if opt != '':			
				# Opens Piksi Console - .../ODG_Rover/piksi_tools
				if opt[0] == "1":
					try:
						piksi = serial.Serial(port = USB_Piksi)	# Testing if piksi is connected to correct USB port
						piksi.close()
						path = "xterm -e 'cd " + root_path + "/piksi_tools && python piksi_tools/console/console.py -p " + USB_Piksi + "'"
						console = subprocess.Popen([path], shell=True, stdin=None, 
						stderr=None, close_fds=True, preexec_fn=os.setsid)					
						print "Console opened."	
						Ard.write("true")					
					except serial.serialutil.SerialException:
						Ard.write("false")
						print "Piksi on wrong USB port!"
				
				# Chooses CSV log files
				elif opt[0] == "2": 
					toStream = getFileName(Ard, root_path)					
					if toStream == "":
						print "No CSV files found."
					elif toStream[0] != [''] or toStream[1] != ['']:
						print toStream
						
				# Deletes all CSV files
				elif opt[0] == "3":
					toStream = ['','']
					deleteCSV(Ard, root_path)
				
				# Streams CSV files
				elif opt[0] == "4":
					if toStream[0] == '' and toStream[1] == '': 
						Ard.write("false")
					else:
						Ard.write("true")
						msg = ''
						print "Starting to stream..."
						while "stop" not in msg:
							updateRobotCoord(RobotCoord, toStream, root_path)
							streamFile(Ard, RobotCoord, toStream)
							msg = Ard.read()
							time.sleep(0.5)
						print "Stream stop requested."
				
				# Saves the current spot to a file		
				elif opt[0] == "5":
					if toStream[0] == '' and toStream[1] == '':
						Ard.write("false")
					else:
						Ard.write("true")
						saveSpot(toStream, root_path, spotsSaved)
				
				# Deletes files used to save spots		
				elif opt[0] == "6":
					i=0
					path = str(root_path + "/ODG_Rover_Python/log/")
					for file in os.listdir(path):
						cmd = "xterm -e 'rm " + path + file + "'"
						subprocess.call(cmd, shell=True)
						i+=1
					if i > 0:
						Ard.write("true")
					else:
						Ard.write("false")	
				
				# Start autonomous mobility
				# CSV files must have been selected before (Option 2)			
				# There must be at least 1 spot saved (Option 5)
				elif opt[0] == "7":
					if spotsSaved == {}:
						Ard.write("false") 
					else:
						if AutoDrive:
							AutoDrive = False
						else:
							Ard.write("true")
							AutoDrive = True					
																	
				# Stops code. It will be reset if you called ./startup_code.py		
				elif opt[0] == "9":
					print "Closing console."
					os.killpg(console.pid, signal.SIGTERM)					
					sys.exit("--- Exiting program. ---")
						
				# Turns off Odroid
				# Must run code as root!
				elif opt[0] == "0":
					os.system("shutdown -h")
					print "System shutting down..."
				
				# Invalid input
				else: 
					print "Invalid input"
			
			# Updates RobotCoord dictionary	
			if toStream[0] != '' or toStream[1] != '':	
				updateRobotCoord(RobotCoord, toStream, root_path)			
			
			# Autonomous mobility
			if AutoDrive:
				AutoRobot(RobotCoord, oldRobotCoord, spotsSaved, Ard)				
			
	except KeyboardInterrupt: # In case you CTRL+C on terminal
		sys.exit()
			
main()

	
	

