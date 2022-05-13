import numpy as np
import cv2

theImage = cv2.imread("unsharpendSample.png")

kernel = np.array([[0, -1, 0],[-1, 5,-1],[0, -1, 0]])
image_sharp = cv2.filter2D(src=theImage, ddepth=-1, kernel=kernel)

cv2.imshow ("original Image" , theImage)
cv2.imshow("final", image_sharp)
cv2.waitKey(0)
cv2.destroyAllWindows()

