__author__ = 'Hank'


import numpy as np
import cv2

img = np.zeros((512, 512, 3), np.uint8)


#image x-y
# 0-0     5-0     10-0


# 0-5     5-5     10-5


# 0-10    5-10    10-10

#image, point1, point2, BGR (are you fucking kidding me?), thickness pixel
cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

#image, top left, bottom right, color, thickness pixel
cv2.rectangle(img, (100, 100), (200, 500), (0, 100, 0), 5)


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()