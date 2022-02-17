#!/usr/bin/env python
from xml.etree.ElementTree import PI
import rospy
from geometry_msgs.msg import Twist

def move():
    # Starts a new node
    rospy.init_node('turtlebot3', anonymous=True)
    velocity_publisher = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    print("Let's move your robot")

    speed = 0.3
    distance = 0.4
    angular_speed = 0.3

    PI = 3.1415926535897
    angle = (90*2*PI)/360

    while not rospy.is_shutdown():

        n = 4

        while n != 0:

            t1 = rospy.Time.now().to_sec()
            current_distance = 0

            while current_distance < distance and n > 0:

                vel_msg.linear.x = speed
                vel_msg.angular.z = 0
                velocity_publisher.publish(vel_msg)
                t3=rospy.Time.now().to_sec()
                current_distance= speed*(t3-t1)

            t2 = rospy.Time.now().to_sec()
            current_angle = 0

            while current_angle < angle and n > 0:
                           
                vel_msg.linear.x = 0
                vel_msg.angular.z = abs(angular_speed)
                velocity_publisher.publish(vel_msg)
                t4 = rospy.Time.now().to_sec()
                current_angle = angular_speed*(t4-t2)
            
            n = n - 1

        #After the loop, stops the robot
        vel_msg.linear = 0
        vel_msg.angular = 0
        #Force the robot to stop
        velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass
