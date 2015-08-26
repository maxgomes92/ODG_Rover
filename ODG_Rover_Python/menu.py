import os
import subprocess
from ArduinoComm import *

def deleteCSV(Ard, root_path):
	i=0
	path = ""
	path = root_path + "/piksi_tools"
	for file in os.listdir(path):
		if file.endswith(".csv"):
			cmd = "xterm -e 'rm " + root_path + "/piksi_tools/" + file + "'"
			subprocess.call(cmd, shell=True)
			i+=1			
	print str(i) + " CSV files deleted."

def getFileName(Ard, root_path):
	files = []
	chosenFile = ['','']
	# Search files in piksi folder
	path = root_path + "/piksi_tools"
	for file in os.listdir(path):
		if file.endswith(".csv"):
			files.append(file)	
	
	if files == []:
		Ard.write("0")
		return ""
	
	# Sends number of files found
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

def getLastLine(filename, root_path):
	name = str(filename)
	n = len(name)
	path = root_path + "/piksi_tools/" + name[2:n-6]
	myfile = open(path, 'r')

	for line in myfile:
		last_line = line	
		
	return last_line
	
def streamFile(file_names, Ard, root_path):
	toPrint = ""
	
	if file_names[0] != ['']:
		# ---------- 'baseline' file
		msg = getLastLine(file_names[0], root_path);
		msg = msg[:len(msg)-1]
		msg = msg.split(',')
		
		# Vectors
		N = msg[1] # North
		E = msg[2] # East
		D = msg[3] # Down distance
		Dist = float(msg[4]) # Distance between Base and Rover
		nSat = msg[5] # N of satelites
		Flag = msg[6][3:4] # Mode (0 = float, 1 = fixed RTK)
		toPrint = "D:" + "%.4f" % Dist + " nS:" + nSat + " F:" + Flag
	
	if file_names[1] != ['']:
		if file_names[0] != ['']:
			toPrint = toPrint + "\n"
			
		# ---------- 'Position' file
		msg = getLastLine(file_names[1], root_path)
		msg = msg[:len(msg)-1]
		msg = msg.split(',')
		
		# Coordinates
		Lat = float(msg[1])
		Lon = float(msg[2])
		toPrint = toPrint + ("Lt:%.6f" % Lat + " Lg:%.6f" % Lon)
	
	Ard.write(toPrint)
	
def saveSpot(toStream, root_path):
	path = str(root_path + "/ODG_Rover_Python/log/baseline_spots.csv")
	baseline = open(path, "a")	
	toAppend = getLastLine(toStream[0], root_path)
	baseline.write(toAppend)	
	
	path = str(root_path + "/ODG_Rover_Python/log/potision_spots.csv")
	position = open(path, "a")
	toAppend = getLastLine(toStream[1], root_path)
	position.write(toAppend)
	
	
