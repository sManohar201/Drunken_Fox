#!/usr/bin/env python
# James Radwill
# Sabari Palaniappan
# Deep Doshi
# January 20, 2017
# Created for EE5900: Introduction to Robotics

#This script provides the control for the jackal simulation to perform a random walk.
#That is rotate a random angle, and drive a random distance. The procedure will interupt
#in the presence of a teleoperation node and resume after 10 seconds of inactivity.

import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
from random import randint
import time

last_time = 0.0		#last time cmd_vel recieved
twist_rate = 5.0	#rate at which cmd_vel is being recieved
teleop=0	#teleoperation flag

# when a cmd-vel message is recieved this function determines the rate at which
# it is being published and from that it determines whether a teleop node is running
def callback(data):
    global last_time
    global twist_rate
    global teleop
    count=0
    #in the case of the first message, set the last time variable
    if last_time == 0.0:
	last_time=time.time()
    #otherwise determine the rate and subsequently determine if a teleop node is running
    else:
        current_time = time.time()
        twist_rate = 1.0/(current_time-last_time)
        last_time=current_time
	if twist_rate > 10:
            teleop = 1
        else:
	    teleop = 0

#this function is called when the teleop flag is set. In the case that the teleop node has been 
#inactive for 10 seconds, it will reset the global variables.
def time_out():
    global last_time
    global twist_rate
    global teleop
    if time.time()-last_time > 10.0:
        last_time = 0.0
        twist_rate = 5.0
        teleop=0   
   
#Creates a subscriber
def twist_sub():
    rospy.Subscriber('cmd_vel', Twist, callback)

#This function defines the random walk and publishes the twist messages.
def move():
    global last_time
    global twist_rate
    global teleop
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    rospy.init_node('move', anonymous=True)
    rate = rospy.Rate(5) # 1hz
    twist_sub()
    while not rospy.is_shutdown():
	null = Vector3(0.0, 0.0, 0.0)
        linear = Vector3(1.0, 0.0, 0.0)
	angular = Vector3(0.0, 0.0, 1.0)
	spin_count = randint(1,20)
	drive_count = randint(1,20)
	#spin a random angle
	while spin_count != 0:
            rate.sleep()
	    if teleop == 1:#If teleop is on call time_out
		time_out()
	    else:
                msg = Twist(null, angular)
        	pub.publish(msg)
		spin_count=spin_count-1
	#drive a random distance
	while drive_count != 0:
            rate.sleep()
	    if teleop == 1:	#If teleop is on call time_out
		time_out()
	    else:
		msg = Twist(linear, null)
        	pub.publish(msg)
        	drive_count=drive_count-1

#Main
if __name__ == '__main__':
    try:
        move()	#call move
    except rospy.ROSInterruptException:
        pass
