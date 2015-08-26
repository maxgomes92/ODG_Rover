import subprocess, time
import sys, inspect, os

from ArduinoComm import *
from menu import *

def main():
	Ard = ArduinoComm("/dev/ttyACM0", 9600)
	toStream = ['',''] # [0] baseline / [1] position
	
	# Finds out its own path
	python_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) # script directory
	root_path = ""
	root_path = python_path[:len(root_path)-17]		
	
	# Receives Instruction from Arduino
	try:	
		while True:
			opt = Ard.read()
			
			# Converting to Integer
			if opt != '':
				
				# Open Console - /home/odroid/Desktop/GitHub/piksi_tools
				if opt[0] == "1":
					path = "xterm -e 'cd " + root_path + "/piksi_tools && python piksi_tools/console/console.py -p /dev/ttyUSB0'"
					subprocess.Popen([path], shell=True, stdin=None, 
					stdout=True, stderr=None, close_fds=True)
					print "Console opened."
				
				# Chooses CSV files
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
					if toStream[0] == [''] and toStream[1] == ['']: 
						Ard.write("false")
					else:
						Ard.write("true")
						msg = ''
						print "Starting to stream..."
						while "stop" not in msg:
							streamFile(toStream, Ard, root_path)
							msg = Ard.read()
						print "Stream stop requested."
				
				# Stop code in order to reset it by .sh file		
				elif opt[0] == "9":
					sys.exit("Exiting program...")
						
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

	
	

