import os
from ArduinoComm import *

def getFileName(Ard):
	files = []
	chosenFile = ['','']
	# Search files in piksi folder
	for file in os.listdir("/home/odroid/Desktop/GitHub/piksi_tools"):
		if file.endswith(".csv"):
			files.append(file)
			print file
	
	# Converts to string
	Ard.write(str(len(files)))
	
	# Sends files name to Arduino
	for fileName in files:
		Ard.write(fileName)
	
	# Get the chosen ones from Arduino	
	for x in range(0, 2):
		msg = ""
		while msg == "":
			msg = Ard.read()
		
		if msg[0] == "0":
			chosenFile[x] = [''] 
		else:
			chosenFile[x] = [msg]
			
	return chosenFile

def getLastLine(filename):
	name = str(filename)
	n = len(name)
	path = "/home/odroid/Desktop/GitHub/piksi_tools/" + name[2:n-6]
	myfile = open(path, 'r')

	for line in myfile:
		last_line = line	
		
	return last_line
	
def streamFile(file_names, Ard):
	toPrint = ""
	
	if file_names[0] != ['']:
		# ---------- 'baseline' file
		msg = getLastLine(file_names[0]);
		msg = msg[:len(msg)-1]
		msg = msg.split(',')
		
		# Vectors
		N = msg[1] # North
		E = msg[2] # East
		D = msg[3] # Down distance
		Dist = float(msg[4]) # Distance between Base and Rover
		nSat = msg[5] # N of satelites
		Flag = msg[6][3:4] # Mode (0 = float, 1 = fixed RTK)
		toPrint = "D:" + "%.2f" % Dist + " nS:" + nSat + " F:" + Flag
	
	if file_names[1] != ['']:
		if file_names[0] != ['']:
			toPrint = toPrint + "\n"
			
		# ---------- 'Position' file
		msg = getLastLine(file_names[1])
		msg = msg[:len(msg)-1]
		msg = msg.split(',')
		
		# Coordinates
		Lat = float(msg[1])
		Lon = float(msg[2])
		toPrint = toPrint + ("Lt:%.3f" % Lat + " Lg:%.3f" % Lon)
	
	Ard.write(toPrint)
