#!/usr/bin/env python3

import rospy
import cv2


def startvideo():
    rospy.init_node('videoer', anonymous=True)
    cap = cv2.VideoCapture(0)
    cv2.namedWindow("TrackedBars")
    cv2.resizeWindow("TrackedBars", 640, 240)
    #cap.set(3, 640)
    #cap.set(4, 480)
    #cap.set(10, 50)

    while not rospy.is_shutdown():
        success, img = cap.read()
        cv2.imshow("Video", img)
        cv2.imshow("Video2", img)
        print("Working")


if __name__ == '__main__':
    try:
        startvideo()
    except rospy.ROSInterruptException:
        pass
