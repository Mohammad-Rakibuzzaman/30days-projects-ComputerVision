
import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'GjbRnviasAAmda9.jpg'))


cv2.imshow('img', img)
cv2.waitKey(0)
