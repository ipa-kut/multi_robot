#!/usr/bin/env python3
# license removed for brevity

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseFeedback
from geometry_msgs.msg import PoseStamped

client = actionlib.SimpleActionClient('robot1/move_base',MoveBaseAction)

def feedback(msg):
    #print("Got feedback", msg)
    pass

def callback(msg:PoseStamped):
    print("Got goal from rviz")
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = msg.header.frame_id
    goal.target_pose.header.stamp = msg.header.stamp
    goal.target_pose.pose.position.x = msg.pose.position.x
    goal.target_pose.pose.position.y = msg.pose.position.y
    # goal.target_pose.pose.position.x = 0.5
    # goal.target_pose.pose.position.y = 0.5
    goal.target_pose.pose.orientation.x = msg.pose.orientation.x
    goal.target_pose.pose.orientation.y = msg.pose.orientation.y
    goal.target_pose.pose.orientation.z = msg.pose.orientation.z
    goal.target_pose.pose.orientation.w = msg.pose.orientation.w
    
    global client
    client.send_goal(goal, feedback_cb=feedback)
    wait = client.wait_for_result()

    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result()


def movebase_client():
    global client
    client.wait_for_server()
    rospy.Subscriber("/move_base_simple/goal", PoseStamped, callback)
    print("Wait for goal from rviz")
    rospy.spin()

if __name__ == '__main__':
    try:
        rospy.init_node('movebase_client_py')
        result = movebase_client()
        if result:
            rospy.loginfo("Goal execution done!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
