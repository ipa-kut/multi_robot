# Multi robot simulation

Trying out multi robot simulation

From the video: https://www.youtube.com/watch?v=mFTkN5v4Jzc   
Based on the question: https://answers.ros.org/question/41433/multiple-robots-simulation-and-navigation/   

But it seems like turtlebot3_gazebo alread has a launch/multi_robot.launch example as well -> check this out as well

Succesfully spawning and visualising two turtlebots now.   
Next get navigation working for both by refering the two resources above.

**!!WARNING!!**   
Currently publishing stupid static tf between the two robots in `robots.launch` just to make visualization nicer. For full navi, this needs to be replaced with dynamic tf to world, which would come from localization.

## Installation

1. Clone this repo into a noetic workspace.  
2. Install deps from workspace directory (above src):  
`rosdep install --from-paths src --ignore-src -y`   
3. Build workspace.

## Bringup

### Multi robot sim witk keyboard teleop

1. Start multi robot sim+rviz (terminal1):   
`roslaunch multi_robot main.launch`   

2. Start teleop for robot1 (terminal2):   
`roslaunch multi_robot keyboard_teleop.launch robot:=robot1`   

3. Start teleop for robot2 (terminal3):   
`roslaunch multi_robot keyboard_teleop.launch robot:=robot2`   
