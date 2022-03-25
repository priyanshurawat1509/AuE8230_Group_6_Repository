<h1>Assignment 6: Line Following and Apriltag Tracking</h1>

This Readme file contains information about this package and the demo videos for each tasks.

<h2>Outcomes:</h2>

1.  Manipulating image data for tracking a point.
2.  Implementing path tracking controllers in Python

<h2>Contents:</h2>

This package consists of scripts and launch files to achieve the following tasks:

- Turtlebot following lane in simulation (gazebo)
- Turtlebot following lane in real world
- Turtlebot burger following the april tag (ID=0)

<h3>Part 1: Track Following in Simulation</h3>

The python file `sim_follow_line.py` for this task is stored in the `scripts` folder and was used to run turtlebot track following in gazebo. The `sim_follow_line.launch` file launches both the python script and gazebo world. For the simulation environment, the turtlebot follows a <I>'Yellow'</I> track. 

The following command can be used to run the launch file - 

`roslaunch assignment6_trackingandfollowing sim_follow_line.launch`

<h4>OUTPUT:</h4>

https://user-images.githubusercontent.com/83747696/160032070-63933c6f-f533-4bed-b579-e2e7e482b3ea.mp4

<h3>Part 2: Track Following in Real-World</h3>

The python file `sim2real_follow_line.py` for this task is stored in the `scripts` folder. This task deals with running turtlebot track following in real-world. For the real-world environment the turtlebot follows a <I>'White'</I> track. Appropriate values of Kp, and HSV values were define to achieve the desired outcome.

The following command can be used to run the python script - 

`rosrun assignment6_trackingandfollowing sim2real_follow_line.py`

https://user-images.githubusercontent.com/83747696/160025485-8e8ba8ee-4311-4e67-94f9-943dd7926964.mp4

<h3>Part 3: April Tag Following</h3>

https://user-images.githubusercontent.com/83747696/160017643-649b203a-664e-4dc3-aed8-ebd8de31c8a4.mp4
