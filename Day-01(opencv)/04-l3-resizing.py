#resizing 

import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'GjbRnviasAAmda9.jpg'))

resized_img = cv2.resize(img, (368, 368)) #in this case width and height

print(img.shape) ### in this case print height then width'
print(resized_img.shape)

cv2.imshow('img', img)
cv2.imshow('resized_img', resized_img)
cv2.waitKey(0)

 





 