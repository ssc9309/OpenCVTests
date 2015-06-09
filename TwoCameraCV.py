__author__ = 'Hank'


import numpy as np
import cv2

#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)

while(True):
    #capture frame by frame
    ret, frame = cap.read()
    ret, frame2 = cap2.read()

    #grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #faces = face_cascade.detectMultiScale(grayFrame, 1.3, 5)
    #for (x, y, w, h) in faces:
    #    cv2.rectangle(frame, (x, y,), (x+w, y+h), (255, 0, 0), 2)
        #roi_gray = gray[y:y+h, x:x+w]
        #roi_color = img[y:y+h, x:x+w]
        #eyes = eye_cascade.detectMultiScale(roi_gray)
        #for (ex,ey,ew,eh) in eyes:
        #    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    #this will update the same window with the newest frame
    cv2.imshow('Cam 1', frame)
    cv2.imshow('Cam 2', frame2)


    #if q is pressed, quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#release the capture when finished
cap.release()
cv2.destroyAllWindows()



