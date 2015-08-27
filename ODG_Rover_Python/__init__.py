import subprocess, time
import sys, inspect, os, signal

from ArduinoComm import *
from menu import *

def main():
	# Sets up communication with Arduino
	Ard = ArduinoComm("/dev/ttyACM0", 9600)
	
	# List to hold files name
	toStream = ['',''] # [0] baseline / [1] position	
	
	# Finds out its own path
	python_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
	root_path = ""
	root_path = python_path[:len(root_path)-17]	# Removing last folder's name
	
	# Receives Instruction from Arduino
	try:	
		while True:
			opt = Ard.read()
			# Processes instruction
			if opt != '':			
				# Opens Piksi Console - .../ODG_Rover/piksi_tools
				if opt[0] == "1":
					path = "xterm -e 'cd " + root_path + "/piksi_tools && python piksi_tools/console/console.py -p /dev/ttyUSB0'"
					console = subprocess.Popen([path], shell=True, stdin=None, 
					stderr=None, close_fds=True, preexec_fn=os.setsid)					
					print "Console opened."
				
				# Chooses CSV log files
				elif opt[0] == "2": 
					toStream = getFileName(Ard, root_path)					
					if toStream == "":
						print "No CSV files found."
					elif toStream[0] != [''] or toStream[1] != ['']:
						print toStream
						
				# Deletes all CSV files
				elif opt[0] == "3":
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
							streamFile(toStream, Ard, root_path)
							msg = Ard.read()
						print "Stream stop requested."
				
				# Saves the current spot to a file		
				elif opt[0] == "5":
					if toStream[0] == '' and toStream[1] == '':
						Ard.write("false")
					else:
						Ard.write("true")
						saveSpot(toStream, root_path)
				
				# Stops code. It will be reset by ./startup_code.py		
				elif opt[0] == "9":
					print "Closing console."
					os.killpg(console.pid, signal.SIGTERM)					
					sys.exit("--- Exiting program. ---")
						
				# Turns off Odroid
				elif opt[0] == "0":
					os.system("shutdown -h")
					print "System shutting down..."
				
				# Invalid input
				else: 
					print "Invalid input"
	except KeyboardInterrupt:
		sys.exit()
			
main()

	
	

