#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
from random import randint
import time

last_time = 0.0
twist_rate = 5.0
teleop=0

def callback(data):
    global last_time
    global twist_rate
    global teleop
    count=0
    
    if last_time == 0.0:
	last_time=time.time()
    else:
        current_time = time.time()
        twist_rate = 1.0/(current_time-last_time)
        last_time=current_time
	if twist_rate > 10:
            teleop = 1
        else:
	    teleop = 0


    rospy.loginfo(str(teleop))
    rospy.loginfo(str(twist_rate))

def time_out():
    global last_time
    global twist_rate
    global teleop
    if time.time()-last_time > 10.0:
        last_time = 0.0
        twist_rate = 5.0
        teleop=0   
   

def twist_sub():
    rospy.Subscriber('cmd_vel', Twist, callback)

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
	while spin_count != 0:
            rate.sleep()
	    if teleop == 1:
		time_out()
	    else:
                msg = Twist(null, angular)
        	pub.publish(msg)
		spin_count=spin_count-1
	while drive_count != 0:
            rate.sleep()
	    if teleop == 1:
		time_out()
	    else:
		msg = Twist(linear, null)
        	pub.publish(msg)
        	drive_count=drive_count-1

            


		

if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass
