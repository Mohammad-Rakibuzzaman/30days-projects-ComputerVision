
import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'whiteboard.png'))

print(img.shape)

### line (last argument is thickness) x and y each time start to end point
cv2.line(img, (100, 150), (300, 450), (0, 255, 0), 3)

### rectangle

cv2.rectangle(img, (200, 250), (350, 350), (0, 0, 225), -1)


### circle

## measuring shape is (671, 1000, 3) meaning that y cordinate or height and x cordinate or width
### so below (275) is vertical or x axis and (300) is horizontal or y axis  

cv2.circle(img, (275, 300), 95, (255, 0, 0), 3) ##BGR
cv2.circle(img, (800, 200), 95, (255, 0, 0), 3) 


### text

cv2.putText(img, 'Hey You bro !!!!', (300, 550), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 7)


cv2.imshow('img', img)
cv2.waitKey(0)