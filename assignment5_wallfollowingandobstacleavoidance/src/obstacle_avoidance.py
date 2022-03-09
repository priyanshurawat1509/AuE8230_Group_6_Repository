#!/usr/bin/env python3
#Python code for obstacle avoidance

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def wallfollow(data):
    print('Range at 20 degress: {}'.format(data.ranges[20]))
    print('Range at 55 degress: {}'.format(data.ranges[55]))
    print('Range at 90 degress: {}'.format(data.ranges[90]))
    print('Range at 270 degress: {}'.format(data.ranges[270]))
    print('Range at 305 degress: {}'.format(data.ranges[305]))
    print('Range at 340 degress: {}'.format(data.ranges[340]))
    
    thresh = 0.4
        
    if data.ranges[20]>thresh and data.ranges[340]>thresh and data.ranges[0]>thresh:
       move.linear.x = 0.5
       move.angular.z = 0
    elif data.ranges[20]>thresh and data.ranges[55]>thresh and data.ranges[90]>thresh:
       move.linear.x = 0.0
       move.angular.z = 0.155
       if data.ranges[0]>thresh and data.ranges[20]>thresh and data.ranges[340]>thresh:
          move.linear.x = 0.5
          move.angular.z = 0.0
    elif data.ranges[270]>thresh and data.ranges[305]>thresh and data.ranges[340]>thresh:
       move.linear.x = 0.0
       move.angular.z = 0.85
       if data.ranges[0]>thresh and data.ranges[20]>thresh and data.ranges[340]>thresh:
          move.linear.x = 0.5
          move.angular.z = 0.0
    else:
       move.linear.x = 0.0
       move.angular.z = 0.5
    
    pub.publish(move)
   
move = Twist()
rospy.init_node('wall_following')
pub = rospy.Publisher("/cmd_vel",Twist, queue_size=10)

sub = rospy.Subscriber("/scan",LaserScan, wallfollow)

rospy.spin() 
