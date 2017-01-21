#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3

def move():
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rospy.init_node('move', anonymous=True)
    rate = rospy.Rate(5) # 1hz
    while not rospy.is_shutdown():
        linear = Vector3(0.0, 0.0, 0.0)
	angular = Vector3(0.0, 0.0, 1.0)
	msg = Twist(linear, angular)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass
