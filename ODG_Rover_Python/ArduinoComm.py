import serial, sys

class ArduinoComm:
	# Sets up serial communication with Arduino
	# If the communication can't be stabilished, the program is aborted.
	def __init__(self, serialpath, baud):
		self.port = serialpath
		self.baud = baud
		
		try:
			self.ard = serial.Serial (
				port = serialpath,
				baudrate = baud,
				parity = serial.PARITY_NONE,
				stopbits = serial.STOPBITS_ONE,
				bytesize = serial.EIGHTBITS,
				timeout=0.1
				)
		except serial.serialutil.SerialException:
			print "Could not stabilish Arduino communication! Aborting..."
			sys.exit()
		
		while self.ard.readline() != "": continue # Empty buffer	
		print "Connected to ", self.ard.name
	
	# Reads serial buffer and returns the String
	# It will return "" if no information on buffer or if it doesn't
	# contain the char "]".
	def read(self):
		msg = self.ard.readline()

		if msg != "":
			# Char to indicate the information was sent to Ubuntu, not to Android
			if msg[0] == "]":
				return msg[1:]
		
		return ""
	
	# Writes to Arduino	
	def write(self, msg):
		# Char to indicate that message comes from Ubuntu ']'
		msg += ']'
		self.ard.write(msg)	 		
			
		
