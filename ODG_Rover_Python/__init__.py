import time
import os

from ArduinoComm import *
from menu import *

def main():
	Ard = ArduinoComm("/dev/ttyACM0", 9600)
	toStream = ['',''] # [0] baseline / [1] position
	
	# Receiving Instruction
	while True:
		opt = Ard.read()
		
		# Converting to Integer
		if opt != '':
			
			# Open Console
			if opt[0] == "1":
				os.system("python /home/odroid/Desktop/GitHub/piksi_tools/piksi_tools/console/console.py -p /dev/ttyUSB0")
			
			# Choose CSV files
			if opt[0] == "2": 
				toStream = getFileName(Ard)
				if toStream[0] != [''] or toStream[1] != ['']:
					print toStream
			
			# Stream CSV files
			elif opt[0] == "3":
				if toStream[0] == [''] and toStream[1] == ['']: 
					Ard.write("false")
				else:
					Ard.write("true")
					msg = ''
					print "Starting to stream..."
					while "stop" not in msg:
						streamFile(toStream, Ard)
						msg = Ard.read()
					print "Stream stop requested."
			
			# Invalid input
			else: 
				print "Invalid input"						
	
main()

	
	

