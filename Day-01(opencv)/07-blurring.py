import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'he.jpg'))

#neighbourhood
k_size = 7

### classical blur most commonly use
img_blur = cv2.blur(img, (k_size, k_size))

cv2.imshow('img', img)
cv2.imshow('img_blur', img_blur)
cv2.waitKey(0)