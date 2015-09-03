import os
import subprocess
from ArduinoComm import *

# Deletes all CSV log files in piksi_tools folder
def deleteCSV(Ard, root_path):
	i=0
	path = ""
	path = root_path + "/piksi_tools" # define path
	for file in os.listdir(path): # find all files
		if file.endswith(".csv"): # check if it's a .CSV
			cmd = "xterm -e 'rm " + root_path + "/piksi_tools/" + file + "'" # Run terminal cmd to delete
			subprocess.call(cmd, shell=True)
			i+=1			
	print str(i) + " CSV files deleted."

# Gets CSV log files name and sends to Arduino
# If none is found, it returns "" and sends "0" to Arduino.
# If files are found, it sends the names to the Arduino.
# Then it gets the chosen one, sent by Arduino.
# Returns the chosen file's name 
def getFileName(Ard, root_path):
	files = []
	chosenFile = ['','']
	
	# Search files in piksi folder
	path = root_path + "/piksi_tools"
	for file in os.listdir(path):
		if file.endswith(".csv"):
			files.append(file)	
	
	# If none is found
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

# It gets the last line from the CSV log files
def getLastLine(filename, root_path):
	name = str(filename)
	n = len(name)
	path = root_path + "/piksi_tools/" + name[2:n-6]
	myfile = open(path, 'r')

	for line in myfile:
		last_line = line	
		
	return last_line

# It creates a string containing some specific information from the CSV log files
# Sends it to the Arduino afterwards
def streamFile(Ard, RobotCoord, file_names):
	toPrint = ""
	
	if file_names[0] != ['']:
		toPrint = "N:%.2f " % RobotCoord['N'] + "E:%.2f" % RobotCoord['E'] + " nS:%i" % RobotCoord['nSat'] + " F:%i" % RobotCoord['Flag']
	
	if file_names[1] != ['']:
		if file_names[0] != ['']:
			toPrint = toPrint + "\n"

		toPrint = toPrint + ("Lt:%.6f" % RobotCoord['Lat'] + " Lg:%.6f" % RobotCoord['Lon'])
	
	Ard.write(toPrint)

# It saves the current Rover spot in a file
# Information is extracted from the CSV log files
# It stores to the spotsSaved dictionary as well	
def saveSpot(toStream, root_path, spotsSaved):
	path = str(root_path + "/ODG_Rover_Python/log/baseline_spots.csv")
	baseline = open(path, "a")	
	msg = getLastLine(toStream[0], root_path)
	baseline.write(msg)	
	
	msg = msg[:len(msg)-1]
	msg = msg.split(',')
	spotsSaved['N'] = float(msg[1])
	spotsSaved['E'] = float(msg[2])
	
	path = str(root_path + "/ODG_Rover_Python/log/potision_spots.csv")
	position = open(path, "a")
	toAppend = getLastLine(toStream[1], root_path)
	position.write(toAppend)

# It updates the RobotCoord dictionary, which contains
# information from the last line of the CSV log files	
def updateRobotCoord(RobotCoord, file_names, root_path):
	if file_names[0] != ['']:
		# ---------- 'baseline' file
		msg = getLastLine(file_names[0], root_path);
		msg = msg[:len(msg)-1]
		msg = msg.split(',')
		
		# Distances between base and rover
		RobotCoord['N']= float(msg[1]) # North
		RobotCoord['E'] = float(msg[2]) # East
		RobotCoord['D'] = float(msg[3]) # Down distance
		RobotCoord['Dist'] = float(msg[4]) # Distance
		RobotCoord['nSat'] = int(msg[5]) # N of satelites
		RobotCoord['Flag'] = int(msg[6][3:4]) # Mode (0 = float, 1 = fixed RTK)	

	if file_names[1] != ['']:
			
		# ---------- 'Position' file
		msg = getLastLine(file_names[1], root_path)
		msg = msg[:len(msg)-1]
		msg = msg.split(',')
		
		# Coordinates
		RobotCoord['Lat'] = float(msg[1])
		RobotCoord['Lon'] = float(msg[2])
	
	
	
		
