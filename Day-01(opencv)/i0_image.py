import os
import cv2

#read image
image_path = os.path.join('.', 'data', 'GjbRnviasAAmda9.jpg')
img = cv2.imread(image_path)

#write image

cv2.imwrite(os.path.join('.', 'output', 'GjbRnviasAAmda9_out.jpg'), img)


#visualizes image
cv2.imshow('image', img)

cv2.waitKey(0)