**PACKAGE CONTENTS**

This assignment contains the files for the following tasks - 

1. Obstacle Avoidance- 

In this part of the assignment a python code 'obstacle_avoidance.py' is implemented to avoid obstacles in the path of the turtlebot3 using /scan data from the liDAR. The aforementioned code file is written by seperating the scan data into different sectors. The launch file executes both the python script and required gazebo environment containing obstacles.

To execute the launch file use -

"roslaunch assignment5_wallfollowingandobstacleavoidance obstacle_avoidance.launch"

2. Wall Following - 

In this part of the assignment a python code 'wall_following.py' is implemented to follow the path enclosed within the side walls by extracting /scan data from the turtlebot3 liDAR. A P-Controller is used to control the motion of the robot by taking /scan data as input from the left and right sides of the turtlebot3. A Kp value of 0.69 is used with conjuction to a linear velocity of .45. The launch file executes both the python script and required gazebo environment.

To execute the launch file use -

"roslaunch assignment5_wallfollowingandobstacleavoidance wall_following.launch"
