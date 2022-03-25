<h1>ASSIGNMENT 6: TRACKING & FOLLOWING</h1>

This Readme file contains information about this package and the demo videos for each tasks.

<h2>OUTCOMES</h2>

1.  Manipulating image data for tracking a point.
2.  Implementing path tracking controllers in Python

<h2>CONTENTS</h2>

This package consists of scripts and launch files to achieve the following tasks:

- Turtlebot following lane in simulation (gazebo)
- Turtlebot following lane in real world
- Turtlebot burger following the april tag (ID=0)

<h3>PART 1: LINE FOLLOWING IN SIMULATION</h3>

The python file `sim_follow_line.py` for this task is stored in the `scripts` folder and was used to run turtlebot track following in gazebo. The `sim_follow_line.launch` file launches both the python script and gazebo world. For the simulation environment, the turtlebot follows a <I>'Yellow'</I> track. 

<b>The following command can be used to run the launch file - </b>

`roslaunch assignment6_trackingandfollowing sim_follow_line.launch`

<h4>OUTPUT</h4>

https://user-images.githubusercontent.com/83747696/160032070-63933c6f-f533-4bed-b579-e2e7e482b3ea.mp4

<h3>PART 2: LINE FOLLOWING IN REAL-WORLD</h3>

The python file `sim2real_follow_line.py` for this task is stored in the `scripts` folder. This task deals with running turtlebot track following in real-world. For the real-world environment the turtlebot follows a <I>'White'</I> track. Appropriate values of Kp, and HSV values were define to achieve the desired outcome.

<b>The following command can be used to run the python script - </b>

`rosrun assignment6_trackingandfollowing sim2real_follow_line.py`

<h4>OUTPUT</h4>

https://user-images.githubusercontent.com/83747696/160025485-8e8ba8ee-4311-4e67-94f9-943dd7926964.mp4

<h3>PART 3: APRIL TAG TRACKING</h3>

https://user-images.githubusercontent.com/83747696/160017643-649b203a-664e-4dc3-aed8-ebd8de31c8a4.mp4
