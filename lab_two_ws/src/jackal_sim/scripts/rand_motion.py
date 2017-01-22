#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
from random import randint

def move():
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rospy.init_node('move', anonymous=True)
    rate = rospy.Rate(5) # 1hz
    while not rospy.is_shutdown():
	null = Vector3(0.0, 0.0, 0.0)
        linear = Vector3(1.0, 0.0, 0.0)
	angular = Vector3(0.0, 0.0, 1.0)
	spin_count = randint(1,10)
	drive_count = randint(1,10)
	while spin_count != 0:
		msg = Twist(null, angular)
        	pub.publish(msg)
        	rate.sleep()
		spin_count=spin_count-1
	while drive_count != 0:
		msg = Twist(linear, null)
        	pub.publish(msg)
        	rate.sleep()
		drive_count=drive_count-1
		

if __name__ == '__main__':

    try:
        move()
    except rospy.ROSInterruptException:
        pass
