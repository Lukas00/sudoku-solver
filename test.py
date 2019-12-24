import numpy as np
import cv2

img = cv2.imread('profile.png', 0)

cv2.imshow("Test", img)
k = cv2.waitKey(0) & 0xFF
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('test.png',img)
    cv2.destroyAllWindows()