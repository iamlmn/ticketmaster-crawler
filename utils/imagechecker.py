import cv2
import numpy as np
a = cv2.imread("sample1.png")
b = cv2.imread("sample2.png")
difference = cv2.subtract(a, b)    
result = not np.any(difference)
if result is True:
    print ("Pictures are the same")
else:
    cv2.imwrite("ed.jpg", difference )
    print ("Pictures are different, the difference is stored as ed.jpg")
