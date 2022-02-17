#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def circle(radius):
    rospy.init_node('turtlebot3', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(5)
    vel = Twist()
    while not rospy.is_shutdown():
        vel.linear.x = 0.1
        vel.linear.y = 0
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = 0.5
        rospy.loginfo("Radius = %f", radius)
        pub.publish(vel)
        rate.sleep()
 
if __name__ == '__main__':
    try:
        circle(2)
    except rospy.ROSInterruptException:
        pass
        
