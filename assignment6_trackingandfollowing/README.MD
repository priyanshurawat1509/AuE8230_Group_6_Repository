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

<h4>3.1 - Tag Detection</h4>

The launch file `continous_detection.launch` provided in the package was used to detect the pose and id of the AprilTag.
The launch file is placed in the launch folder
For calling the image proc node, we had to use the interensic and extrensic calibration launch file along with camera bring up
The tag size and family was updated in the tags.ymal file which led to smooth detection of tags
Attached herewith is the rqt_graph of the Nodes acting to do so.

<b>The following command can be used to run the launch file - </b>

`roslaunch turtlebot3_autorace_camera raspberry_pi_camera_publish.launch`

`roslaunch turtlebot3_autorace_camera intrinsic_camera_calibration.launch mode:=action`

`roslaunch turtlebot3_autorace_camera extrinsic_camera_calibration.launch mode:=action`

`roslaunch assignment6_trackingandfollowing continous_detection.launch`

`rqt`

![continousdetection_rqt](https://user-images.githubusercontent.com/99144800/160041996-a32f8dc6-7774-4756-a2c2-32912068abb3.png)

<h4>3.2 - Tag Following</h4>
  
The output of the tag being detected can be seen in the rqt window

Once, the tag was detected the python file `april_tag_tracking.py` was used to take the output of tag detection and further process it for the bot to move and follow it.
 
 <b>The following command can be used to run the python script - </b>

`rosrun assignment6_trackingandfollowing april_tag_tracking.py`

https://user-images.githubusercontent.com/83747696/160017643-649b203a-664e-4dc3-aed8-ebd8de31c8a4.mp4

<h2>Citations :- </h2>

1. We strongly suggest you using a fast and reliable 5GHz network which we used during the development of this code as the amount of active nodes at one point will hamper the data transfer process leading to the images being recieved not in sync.
2. We used the following packages for the task:

https://github.com/AprilRobotics/apriltag_ros

https://github.com/opencv/opencv
