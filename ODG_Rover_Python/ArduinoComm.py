import serial

class ArduinoComm:
	# Sets up serial communication with Arduino
	def __init__(self, serialpath, baud):
		self.port = serialpath
		self.baud = baud
		
		self.ard = serial.Serial (
			port = serialpath,
			baudrate = baud,
			parity = serial.PARITY_NONE,
			stopbits = serial.STOPBITS_ONE,
			bytesize = serial.EIGHTBITS,
			timeout=0.3
			)
		
		while self.ard.readline() != "": continue	
		print "Connected to ", self.ard.name
	
	# Reads serial buffer and returns the String 	
	def read(self):
		msg = self.ard.readline()

		if msg != "":
			if msg[0] == "]":
				return msg[1:]
		
		return ""
	
	# Writes to Arduino	
	def write(self, msg):
		# Char to indicate that message comes from Ubuntu ']'
		msg += ']'
		self.ard.write(msg)	 		
			
		
