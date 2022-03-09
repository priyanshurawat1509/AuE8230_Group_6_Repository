#!/usr/bin/env python3
	
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
	
def PID(error, Kp=0.69): #defing a function for P-Controller
    return Kp*error 
    	
def wallfollow(data): #defining a wall following function
    lidar_scan = list(data.ranges[0:359]) # Storing LiDAR data 
    scan = []
    for i in range(len(lidar_scan)):
        if lidar_scan[i]<3:
            scan.append(lidar_scan[i]) #Taking only values less than '3'  

    right = scan[-90:-16]
    right = sum(right)/len(right) #average distance of obstacles on the right 
    left = scan[16:90]
    left = sum(left)/len(left) #average distance of obstacles on the left 
    
    linear_vel = 0.45 
    angular_vel = 0 
 
    error = left-right #estimating the error for P-Controller
    
    move.linear.x = linear_vel #linear velocity
    move.angular.z = angular_vel + PID(error) #angular velocity
    print("Angular Velocity is %s" % move.angular.z)

rospy.init_node('wall_follower')
move = Twist()
pub = rospy.Publisher("/cmd_vel",Twist, queue_size=10)
sub = rospy.Subscriber("/scan",LaserScan, wallfollow)
while not rospy.is_shutdown():
    pub.publish(move)
    pass
rospy.spin()
