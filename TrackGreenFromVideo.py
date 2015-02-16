__author__ = 'Hank'

import numpy as np
import cv2
import cv2.cv as cv

lower_Green = np.array([50, 100, 100])
upper_Green = np.array([70, 255, 255])

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_Green, upper_Green)

    res = cv2.bitwise_and(frame, frame, mask= mask)

    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)

    blobs = cv2.HoughCircles(gray, cv.CV_HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
    blobs = np.uint16(np.around(blobs))

    for i in blobs[0, :]:
        #outer circle
        #cv2.circle(res, (i[0], i[1]), i[2], (0, 0, 255), 2)

        #centre of circle
        cv2.circle(res,(i[0],i[1]),2,(0,0,255),3)
        cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)


    #cv2.imshow('pic', img)

    #cv2.imshow('mask', mask)
    cv2.imshow('Video Feed', frame)
    cv2.imshow('result', res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#release the capture when finished
cap.release()
cv2.destroyAllWindows()