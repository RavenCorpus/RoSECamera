#!/usr/bin/env python

# need usb_cam package
# need ros-*version*-perception

#--------Run Camera Instructions------------
#1. roscore (tab 1)
#2. source ~/ros_camera/devel/setup.bash (tab2)
#3. rosrun ros_camera camera_publisher.py (tab2)
#4. source ~/ros_camera/devel/setup.bash (tab3)
#5. rosrun ros_camera camera_publisher.py (tab3)

# enable ros python
import rospy
# get msgs as image
from sensor_msgs.msg import Image
# bridge opencv images and ros messages
from cv_bridge import CvBridge
import cv2


def talker():
	#initialize node with name
    rospy.init_node('camera_sensor_publisher', anonymous=True)
	#create topic publisher
    publisher = rospy.Publisher('video_topic', Image, queue_size=60)
	#update rate
    rate = rospy.Rate(30)

	#create camera object
    videoCaptureObject = cv2.VideoCapture(0)
    bridgeObject = CvBridge()

    while not rospy.is_shutdown():
	#read camera
        returnValue, capturedFrame = videoCaptureObject.read()
        if returnValue == True:
		#confirm image
            rospy.loginfo('Video frame captured and published')
            imageToTransmit = bridgeObject.cv2_to_imgmsg(capturedFrame)
            publisher.publish(imageToTransmit)
        rate.sleep()

#retry camera until exception
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

