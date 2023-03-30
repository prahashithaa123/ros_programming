#!/usr/bin/python3

import rospy
from std_msgs.msg import String
rospy.init_node("sample_publisher")
pub = rospy.Publisher("sample_topic", String, queue_size = 10)
sentence = String()
sentence.data = "Hello"
loop_hz = rospy.Rate(10)

while not rospy.is_shutdown():
	pub.publish(sentence)
	rospy.loginfo(sentence.data)
	loop_hz.sleep()
