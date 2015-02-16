__author__ = 'Hank'


import numpy as np
import cv2

img = cv2.imread('OriginalPic.png')


checkx = 740
checky = 540
#cv2.line(img, (0, 0), (checkx, checky), (255, 0, 0), 2)
#cv2.imshow('test', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

px = img[checkx, checky]
print px


hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


#the following array is not simply B G R
#works different in HSV
#look http://docs.opencv.org/trunk/doc/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html#converting-colorspaces
#>>> green = np.uint8([[[0,255,0 ]]])
#>>> hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
#>>> print hsv_green
#[[[60 255 255]]]
#then use [x-10, 100, 100] and [x+10, 255, 255]


lower_Green = np.array([50, 100, 100])
upper_Green = np.array([70, 255, 255])

mask = cv2.inRange(hsv, lower_Green, upper_Green)

res = cv2.bitwise_and(img, img, mask= mask)

cv2.imshow('pic', img)

cv2.imshow('mask', mask)
cv2.imshow('result', res)

cv2.waitKey(0)
cv2.destroyAllWindows()


#cv2.imwrite('OriginalPic.png', img)
#cv2.imwrite('FilteredPic.png', res)