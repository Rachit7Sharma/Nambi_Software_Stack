import cv2
from threading import Thread
from geometry_msgs.msg import PoseStamped
import numpy as np
import rospy
from geometry_msgs.msg import PoseStamped
from move_base_msgs.msg import MoveBaseActionGoal
import math


class ArrowDetector:
    def __init__(self):
        self.frame = None
        self.arrow_pose = None
        self.running = True
        self.detect_thread = Thread(target=self.detect_arrow)
        self.detect_thread.start()
        
    def detect_arrow(self):

        while self.running:
            if self.frame is not None:
                
                    # Perform arrow detection on the frame
					
                gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
                edges = cv2.Canny(gray, 50, 150, apertureSize = 3)
                lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)
                if lines is not None:
                    for line in lines:
                        x1, y1, x2, y2 = line[0]
                        # Draw arrow line on the frame
                        cv2.line(self.frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                        # Determine arrow direction and position
                        # Code to find the arrow direction and position
                        self.arrow_pose = PoseStamped()
                        self.arrow_pose.header.stamp = rospy.Time.now()
                        self.arrow_pose.header.frame_id = "base_link"
                        self.arrow_pose.pose.position.x = x1
                        self.arrow_pose.pose.position.y = y1
                        self.arrow_pose.pose.position.z = 0.0
                        self.arrow_pose.pose.orientation.x = 0.0
                        self.arrow_pose.pose.orientation.y = 0.0
                        self.arrow_pose.pose.orientation.z = 0.0
                        self.arrow_pose.pose.orientation.w = 1.0
                else:
                    self.arrow_pose = None

                cv2.imshow("Frame",self.frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                        break            # Show the frame
            


    def stop(self):
        self.running = False
        self.detect_thread.join()
        
    def set_frame(self, frame):
        self.frame = frame
        
    def get_arrow_pose(self):
        return self.arrow_pose

def detect_arrow_thread(cap):
    arrow_detector = ArrowDetector()
    while not rospy.is_shutdown():
        # Get the current frame from the video feed
        # Example using cv2.VideoCapture
        ret, frame = cap.read()

        arrow_detector.set_frame(frame)

        arrow_pose = arrow_detector.get_arrow_pose()
        if arrow_pose is not None:
            return arrow_pose

# Create the video capture object
cap = cv2.VideoCapture(0)
# ret, frame = cap.read()
# cv2.imshow('j',frame)


# Initialize a ROS node
rospy.init_node('arrow_detection')

# Create a publisher for the move_base_simple/goal topic
goal_pub = rospy.Publisher('move_base_simple/goal', MoveBaseActionGoal, queue_size=10)

# Create a publisher for the arrow_pose topic
arrow_pose_pub = rospy.Publisher('arrow_pose', PoseStamped, queue_size=10)

# Create a rate object to control the loop rate
rate = rospy.Rate(10)

while True:
    # Detect the arrow using the detect_arrow_thread function
    arrow_pose = detect_arrow_thread(cap)

    if arrow_pose is not None:
        # Publish the arrow pose on the arrow_pose topic
        arrow_pose_pub.publish(arrow_pose)

        # Create a move_base_simple goal message
        goal = MoveBaseActionGoal()
        goal.header.stamp = rospy.Time.now()
        goal.goal.target_pose.header.frame_id = "odom"
        goal.goal.target_pose.pose = arrow_pose.pose

        # Publish the goal on the move_base_simple/goal topic
        goal_pub.publish(goal)

    # Sleep for a short period of time
    rate.sleep()

