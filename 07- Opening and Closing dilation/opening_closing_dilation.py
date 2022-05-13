import numpy as np
import cv2

theImage = cv2.imread("Noisy.png")

okernel = np.ones((5,5), dtype = "uint8")/9
opening = cv2.morphologyEx(theImage, cv2.MORPH_OPEN, okernel)

ckernel = np.ones((9,9), dtype = "uint8")/9
closing = cv2.morphologyEx(theImage, cv2.MORPH_CLOSE, ckernel)

CandO = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, ckernel)

cv2.imshow ("original Image" , theImage)
cv2.imshow("opening", opening)
cv2.imshow("closing", closing)
cv2.imshow("final Resualt", CandO)
cv2.waitKey(0)
cv2.destroyAllWindows()

