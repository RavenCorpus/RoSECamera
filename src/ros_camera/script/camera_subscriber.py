#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def callbackFunction(message):
	#bridge camera info
	bridgeObject = CvBridge()
	#confirm image reception
	rospy.loginfo('received a video message/frame')
	convertedFrameBackToCV=bridgeObject.imgmsg_to_cv2(message)
	#display frame
	cv2.imshow('camera',convertedFrameBackToCV)
	cv2.waitKey(1)

def listener():
	#create subscriber topic
	rospy.init_node('camera_sensor_subscriber', anonymous=True)
	rospy.Subscriber('video_topic',Image,callbackFunction)
	rospy.spin()
	cv2.destroyAllWindows()

if __name__ == '__main__':
	listener()
