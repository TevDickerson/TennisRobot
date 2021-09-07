import cv2
import numpy as np
import csv


def empty(a):
    pass


mask_Data_File = open('TestFile.csv', 'r')
csvreader = csv.reader(mask_Data_File)
savedValueList = []
for values in csvreader:
    savedValueList = values

mask_Data_File.close()


# VideoSettings___________________________________________
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # pixel quality 480p
cap.set(4, 480)  # pixel quality 480p
cap.set(10, 50)  # brightness
# _________________________________________________________

cv2.namedWindow("TrackedBars")
cv2.resizeWindow("TrackedBars", 640, 240)
cv2.createTrackbar("Hue Min", "TrackedBars", int(savedValueList[0]), 179, empty)
cv2.createTrackbar("Hue Max", "TrackedBars", int(savedValueList[1]), 179, empty)
cv2.createTrackbar("Sat Min", "TrackedBars", int(savedValueList[2]), 255, empty)
cv2.createTrackbar("Sat Max", "TrackedBars", int(savedValueList[3]), 255, empty)
cv2.createTrackbar("Val Min", "TrackedBars", int(savedValueList[4]), 255, empty)
cv2.createTrackbar("Val Max", "TrackedBars", int(savedValueList[5]), 255, empty)

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)

    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow("HSV", imgHSV)

    h_min = cv2.getTrackbarPos("Hue Min", "TrackedBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackedBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackedBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackedBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackedBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackedBars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)

    cv2.imshow("Mask", mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        mask_Data_File = open('TestFile.csv', 'w')
        csvwriter = csv.writer(mask_Data_File)
        csvwriter.writerow([h_min, h_max, s_min, s_max, v_min, v_max])
        mask_Data_File.close()
        break
