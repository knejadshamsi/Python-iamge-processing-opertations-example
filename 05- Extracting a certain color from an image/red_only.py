import numpy as np
import cv2

theImage = cv2.imread("golden-gate.png")
grayImage = cv2.cvtColor(theImage, cv2.COLOR_BGR2GRAY)

lower = np.array([20, 0, 15])
upper = np.array([60, 80, 270])
theRedmask = cv2.inRange(theImage, lower, upper)
others_mask = cv2.bitwise_not(theRedmask)

Red = cv2.bitwise_or(theImage,theImage,mask= theRedmask)
Gray = cv2.bitwise_or(grayImage,grayImage,mask= others_mask)
Gray = np.stack((Gray,)*3, axis=-1)

final = Red+Gray

cv2.imshow ("the filter" , theRedmask)
cv2.imshow ("original Image" , theImage)
cv2.imshow('final', final)

cv2.waitKey(0)
cv2.destroyAllWindows()

