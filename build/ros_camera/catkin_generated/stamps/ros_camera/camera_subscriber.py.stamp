import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

import cv2

def callbackFunction(message):
	bridgeObject = CvBridge()
	rospy.loginfo('received a video message/frame')
	convertedFrameBackToCV=bridgeObject.imgmsg_to_cv2(message)
	cv2.imshow('camera',convertedFrameBackToCV)
	cv2.waitKey(1)

def listener():
	rospy.init_node('camera_sensor_subscriber', anonymous=True)
	rospy.Subscriber('video topic',Image,callbackFunction)
	rospy.spin()
	cv2.destroyAllWindows()

if __name__ == '__main__':
	listener()
