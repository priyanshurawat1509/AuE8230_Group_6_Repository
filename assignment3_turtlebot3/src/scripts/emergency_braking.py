#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

def callback(msg):

    global velocity_publisher, vel_msg
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    rate = rospy.Rate(10)

    speed = 0.2

    while not rospy.is_shutdown():

        vel_msg.linear.x = speed
        velocity_publisher.publish(vel_msg)
        range = msg.ranges 
        
        
        if range[0] < 2:
            stop()
        print(range)
        move()

        

def stop():
    vel_msg.linear.x= 0
    velocity_publisher.publish(vel_msg)

def main():
    rospy.init_node('emergency_brake', anonymous=True)
    laser_subscriber = rospy.Subscriber('/scan', LaserScan, callback)
    rospy.spin()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException: 
        pass
