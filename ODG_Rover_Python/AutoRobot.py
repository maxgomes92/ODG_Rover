import time, math

def AutoRobot(RobotCoord, oldRobotCoord, spotsSaved, Ard):
	N_to_Dest = abs(RobotCoord['N'] - spotsSaved['N']) > 0.5
	E_to_Dest = abs(RobotCoord['E'] - spotsSaved['E']) > 0.5
	
	# Moved enough?
	N_to_old = abs(RobotCoord['N'] - oldRobotCoord['N']) > 0.1
	E_to_old = abs(RobotCoord['E'] - oldRobotCoord['E']) > 0.1
	
	if (N_to_Dest or E_to_Dest): # Check if it's on the right spot
		if(N_to_old or E_to_old): # Check if robot has moved enough
			# Going right direction?
			print "Checking right direction"
			
			# Global coordinates (x,y)
			dest = [spotsSaved['E'],spotsSaved['N']] # destination
			old = [oldRobotCoord['E'],oldRobotCoord['N']] # previous
			cur = [RobotCoord['E'],RobotCoord['N']] # current
			
			# Local coordinates (x,y)
			cur_local = [cur[0]-old[0],cur[1]-old[1]]
			dest_local = [dest[0]-old[0],dest[1]-old[1]]
			
			print cur_local
			print dest_local
			
			# Gets angle
			cur_angle = calcAngle(cur_local)
			dest_angle = calcAngle(dest_local)
			
			print cur_angle # added
			print dest_angle # added
			
			# Right direction? Acceptable error +-5 degrees
			if dest_angle > cur_angle + 5:
				a = cur_angle + (360 - dest_angle)
				b = dest_angle - cur_angle
				if a < b: 
					Ard.write("rr")
					print "RR" # added
				else: 
					Ard.write("rl")
					print "RL" # added	
				time.sleep(0.5) 								
			elif cur_angle > dest_angle + 5:
				a = dest_angle + (360 - cur_angle)
				b = cur_angle - dest_angle
				if a > b: 
					Ard.write("rr")
					print "RR" # added
				else: 
					Ard.write("rl")
					print "RL" # added
				time.sleep(0.5) # sometime to the robot to rotate 			
			else:
				print "On right track!" # added
							
			# Saving current position before updating
			oldRobotCoord['N'] = RobotCoord['N']
			oldRobotCoord['E'] = RobotCoord['E']	
									
			Ard.write("fw")		
	else:						
		print "On right spot!!" # added
		
def calcAngle(coord):
	# 1st quadrant
	if coord[0] > 0 and coord[1] >= 0:
		if coord[1] == 0: return 0
		angle = math.degrees(math.atan(abs(coord[1]/coord[0])))
		return angle
	# 2nd quadrant
	elif coord[0] < 0 and coord[1] >= 0:
		if coord[1] == 0: return 180
		angle = 90 + math.degrees(math.atan(abs(coord[0]/coord[1])))
		return angle
	# 3rd quadrant
	elif coord[0] <= 0 and coord[1] < 0:
		if coord[0] == 0: return 270
		angle = 180 + math.degrees(math.atan(abs(coord[1]/coord[0])))
		return angle
	# 4th quadrant	
	elif coord[0] > 0 and coord[1] <= 0:
		if coord[1] == 0: return 0
		angle = 270 + math.degrees(math.atan(abs(coord[0]/coord[1])))
		return angle
