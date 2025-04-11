import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'she.jpg'))

### the idea is to convert bgr image to binary image
## Thresholding mostly used in image segmentation or detect object from a lots of noise

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
ret, thresh = cv2.threshold(img_gray, 110, 255, cv2.THRESH_BINARY) ###so 80 will be 0 or black and rest of it greater than 80 will be 255 or white

thresh = cv2.blur(thresh, (10, 10))

ret, thresh = cv2.threshold(thresh, 110, 255, cv2.THRESH_BINARY)

#### There is another threshold which is used for detecting shadow ocr. so the function called 
# cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C(we can use 2 different parameter here one gaus and mean), cv2.THRESH_BINARY, 21, 30) 



cv2.imshow('img', img)
cv2.imshow('img_gray', img_gray)
cv2.imshow('thresh', thresh)

cv2.imwrite('output/sketch.jpg', thresh)


cv2.waitKey(0)