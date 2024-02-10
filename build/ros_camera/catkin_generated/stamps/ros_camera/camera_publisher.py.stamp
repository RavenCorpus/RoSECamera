import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

rospy.init_node('camera_sensor_publisher', anonymous=True)
publisher=rospy.Publisher('video topic',Image,queue_size=60)
rate = rospy.Rate(30)

videoCaptureObject = cv2.VideoCapture(0)
bridgeObject=CvBridge()

def talker():
	while not rospy.is_shutdown():
		returnValue, capturedFrame = videoCaptureObject.read()
		if returnValue == True:
			rospy.loginfo('Video frame captured an published')
			imageToTransmit=bridgeObject.cv2 to imgmsg(capturedFrame)
			publisher.publish(imageToTransmit)
		rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
