# Multi robot simulation

Trying out multi robot simulation

From the video: https://www.youtube.com/watch?v=mFTkN5v4Jzc   
Based on the question: https://answers.ros.org/question/41433/multiple-robots-simulation-and-navigation/   

## Current status

* Multi sim comes up with 2 robots
* Can keyboard teleop them individually 
* Localization works for multiple robots
* move_base seems to startup correctly
* **BUT** when giving goals, the robot moves haphazardly - **WHY??**

## TODOS

- [] Fix nav for one robot - google, verify all configs, compare vs standard TB3 sim, pull move_base source code and debug
- [] Simplify parameter setting per robot, make it somehow dynmically settable (needed for later)
- [] Test nav for 4 robots

## Installation

1. Clone this repo into a noetic workspace.  
2. Install deps from workspace directory (above src):  
`rosdep install --from-paths src --ignore-src -y`   
3. Install TB3 binaries:   
 `sudo apt install ros-noetic-turtlebot3*`
4. Build & source workspace.

## Bringup

### I. Multi robot sim with keyboard teleop

1. Start multi robot sim+rviz (terminal1):   
`roslaunch multi_robot main.launch nav:=false`   

NB: If you want the gazebo gui, set the param gui:=true above.    
ex: `roslaunch multi_robot main.launch nav:=false gui:=true`   

2. Start teleop for robot1 (terminal2):   
`roslaunch multi_robot keyboard_teleop.launch robot:=robot1`   

3. Start teleop for robot2 (terminal3):   
`roslaunch multi_robot keyboard_teleop.launch robot:=robot2`   

### II. Multi robot sim with navigation

1. Start multi robot sim+rviz+move_base (terminal1):   
`roslaunch multi_robot main.launch nav:=true` 

2. Start a goal publisher for the robot to command (terminal2). Only one at a time.   
`roscd multi_sim/scripts`    
`./robot1_goal.py`   

3. In rviz, select the "2D Nav Goal" button and then click and drag on the desired goal position. 
The above script will read this and invoke a move_base action with the same goal.
