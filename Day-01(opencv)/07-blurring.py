import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'he.jpg'))

#neighbourhood
k_size = 7

### classical blur most commonly use
img_blur = cv2.blur(img, (k_size, k_size))

##gaussian blur
img_gaussian_blur = cv2.GaussianBlur(img, (k_size, k_size), 3)

###median blur
img_median_blur = cv2.medianBlur(img, k_size)


cv2.imshow('img', img)
cv2.imshow('img_blur', img_blur)
cv2.imshow('img_gaussian_blur', img_gaussian_blur)
cv2.imshow('img_median_blur', img_median_blur)

cv2.imwrite('output/blur-gaussian-myy.jpg', img_gaussian_blur)

cv2.waitKey(0)