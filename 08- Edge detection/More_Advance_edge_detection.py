import cv2
import numpy as np

theImage = cv2.imread("cameraman.png")
edge = cv2.Canny(theImage, 120, 150)
edge2 = cv2.Canny(theImage, 120, 350)
edge3 = cv2.Canny(theImage, 10, 150)

cv2.imshow("original Image", theImage)
cv2.imshow("edge", edge)
cv2.imshow("edge2", edge2)
cv2.imshow("edge3", edge3)

cv2.waitKey(0)
cv2.destroyAllWindows()
