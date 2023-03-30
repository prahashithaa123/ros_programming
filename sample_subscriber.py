#!/usr/bin/python3

import rospy
from std_msgs.msg import String

def callback_function(msg):
	rospy.loginfo(msg.data + "From Subscriber")
	
rospy.init_node("sample_subscriber")
sub = rospy.Subscriber("sample_topic", String, callback_function, queue_size=10)
rospy.spin()
