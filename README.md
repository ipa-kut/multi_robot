Trying out multi robot simulations

From the video: https://www.youtube.com/watch?v=mFTkN5v4Jzc   
Based on the question: https://answers.ros.org/question/41433/multiple-robots-simulation-and-navigation/   

But it seems like turtlebot3_gazebo alread has a launch/multi_robot.launch example as well -> check this out as well

Succesfully spawning and visualising two turtlebots now.   
Next get navigation working for both by refering the two resources above.

**!!WARNING!!**   
Currently publishing stupid static tf between the two robots in `robots.launch` just to make visualization nicer. For full navi, this needs to be removed.