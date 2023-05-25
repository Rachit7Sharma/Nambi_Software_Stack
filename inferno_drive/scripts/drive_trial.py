#!/usr/bin/env python
import rospy
from drive.msg import Drive
from sensor_msgs.msg import Joy
import sys
import math


class Manual:
	def __init__(self):
		rospy.init_node("Velocity")
		self.pub = rospy.Publisher("cmd_vel",Drive,queue_size=1)
		#self.pub = rospy.Publisher('robotic_arm', Pwm,queue_size=1)  

		self.rate = rospy
		rospy.Subscriber("joy", Joy, self.joyCallback)
		self.cmd_vel = Drive()

	def main(self):
		r = rospy.Rate(4)
		while not rospy.is_shutdown():
			self.pub.publish(self.cmd_vel)
			print(self.cmd_vel)
			print('\n ------- \n')
			r.sleep()

	""" def inverseKinematics(self):
		length1 = 34
		length2 = 38

		rad_angle2 = math.acos(((x**2)+ (y**2) - (length1**2) - (length2**2)) / (2*length1*length2))
		rad_angle1= math.atan(y / x) - math.atan((length2*(math.sin(rad_angle2))) / (length1+ length2*(math.cos(rad_angle2))))

		self.cmd_vel.shoulder_angle= (rad_angle1*180)/math.pi
		self.cmd_vel.elbow_angle= (rad_angle2*180)/math.pi	
 """
	""" def ForwardKinematics(self):
		length1 = 34
		length2 = 38

		rad_angle1 = (self.cmd_vel.shoulder_angle*math.pi)/180
		rad_angle2 = (self.cmd_vel.elbow_angle*math.pi)/180
		x = length1 * math.cos(rad_angle1) +length2 * math.cos(rad_angle1 + rad_angle2)
		y = length1 * math.sin(rad_angle1) +length2 * math.sin (rad_angle1 + rad_angle2)
       """

	def joyCallback(self, msg):

		#rt/bt
		# if(abs(msg.axes[2]) > 0):
		# 	self.cmd_vel.base = 200 - (200.0*msg.axes[2])
		# else:
		# 	self.cmd_vel.base = 0
		
		# if(abs(msg.axes[5]) > 0):
		# 	self.cmd_vel.base = - int(200 - (200.0*msg.axes[5]))
		# else:
		# 	self.cmd_vel.base = 0	

		


		global x
		x = 38
		global y 
		y = 34

		self.cmd_vel.Tower = 1
		# left side axis up/down for elbow
		if(abs(msg.axes[1]) > 0.2):
			self.cmd_vel.left1 = int(255.0*msg.axes[1])
		        self.cmd_vel.left2 = int(255.0*msg.axes[1])
                        self.cmd_vel.right1 = int(255.0*msg.axes[1])
		        self.cmd_vel.right2 = int(255.0*msg.axes[1])
		elif(abs(msg.axes[1]) < 0.2):
			self.cmd_vel.left1 = int(255.0*msg.axes[1])
		        self.cmd_vel.left2 = int(255.0*msg.axes[1])
                        self.cmd_vel.right1 = int(255.0*msg.axes[1])
		        self.cmd_vel.right2 = int(255.0*msg.axes[1])
		
		else:
			self.cmd_vel.left1 = 0
		        self.cmd_vel.left2 = 0
                        self.cmd_vel.right1 = 0
		        self.cmd_vel.right2 = 0

				

        # left side axis left/right for shoulder
		if(abs(msg.axes[3]) > 0.2):
			self.cmd_vel.left1 = -int(255.0*msg.axes[3])
		        self.cmd_vel.left2 = -int(255.0*msg.axes[3])
                        self.cmd_vel.right1 = int(255.0*msg.axes[3])
		        self.cmd_vel.right2 = int(255.0*msg.axes[3])
		
		elif(abs(msg.axes[3]) < 0.2):
			self.cmd_vel.left1 = -int(255.0*msg.axes[3])
		        self.cmd_vel.left2 = -int(255.0*msg.axes[3])
                        self.cmd_vel.right1 = int(255.0*msg.axes[3])
		        self.cmd_vel.right2 = int(255.0*msg.axes[3])
		
		else:
			self.cmd_vel.left1 = 0
		        self.cmd_vel.left2 = 0
                        self.cmd_vel.right1 = 0
		        self.cmd_vel.right2 = 0

	


	   	#right side axis left/right for yaw
#		if(abs(msg.axes[4]) > 0.2):
#			self.cmd_vel.yaw = int(255.0*msg.axes[4])
		
#		elif(abs(msg.axes[4]) < 0.2):
#			self.cmd_vel.yaw = int(255.0*msg.axes[4])
		
#		else:
#			self.cmd_vel.yaw = 0

		#right side axis up/down for pitch
#		if(abs(msg.axes[3]) > 0.2):
#			self.cmd_vel.base = int(255.0*msg.axes[3])
		
#		elif(abs(msg.axes[3]) < 0.2):
#			self.cmd_vel.base = int(255.0*msg.axes[3])
		
#		else:
#			self.cmd_vel.base = 0

		# lb/rb buttons for roll
#		self.cmd_vel.pitch = -100*(msg.buttons[1]-msg.buttons[2])

		# lb/rb buttons for base
#		self.cmd_vel.gripper = 250*(msg.buttons[4]-msg.buttons[5])

#		self.cmd_vel.roll = -250*(msg.buttons[3]-msg.buttons[0])
	

'''
        # Computing angle 2 Elbow up/down 
		numerator = ((length1 + length2)**2) - ((x**2) + (y**2))
		denominator = ((x**2) + (y**2)) - ((length1 - length2)**2)
		angle2UP = math.degrees(math.atan(math.sqrt(numerator/denominator)))
		angle2DOWN = angle2UP * -1
		#self.cmd_vel.shoulder_angle
        #self.cmd_vel.elbow_angle
        # Angle 1 Elbow up
		numerator = (length2 * math.sin(math.radians(angle2UP)))
		denominator = ((length1 + length2) * math.cos(math.radians(angle2UP)))
		angle1UP = math.degrees(math.atan2(numerator, denominator))
        # Angle 1 Elbow down
		numerator = (length2 * math.sin(math.radians(angle2DOWN)))
		denominator = ((length1 + length2) * math.cos(math.radians(angle2DOWN)))
		angle1DOWN = math.degrees(math.atan2(numerator, denominator))
		print("Angle 1 Elbow up: " + str(angle1UP))
		print("Angle 1 Elbow down: " + str(angle1DOWN))
		print("Angle 2 Elbow up: " + str(angle2UP))
		print("Angle 2 Elbow down: " + str(angle2DOWN))		
'''    
			
if __name__ == '__main__':
	x = Manual()
	x.main()
	rospy.spin()

