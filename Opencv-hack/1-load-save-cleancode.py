import cv2
import numpy as np
from matplotlib import pyplot as plt


# Let's see what version we're running
print(cv2.__version__)

image = cv2.imread('./images/GjbRnviasAAmda9.jpg')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# plt.imshow(image)

# plt.show()

# example of neat and organized code
def imshow(title = "", image = None):
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('myexbeb')
    plt.show()

# imshow("Display my first image", image)

#to save the last image
cv2.imwrite('output/output.jpg', image)
cv2.imwrite('output/output.png', image)

print(image.shape) #height, width and depth which is  (736, 736, 3)
print(image.shape[0])

print("Height of my image is: {} pixels".format(int(image.shape[0])))
print("Width of my image is: {} pixels".format(int(image.shape[1]))) 
print("Depth of my image is: {} pixels".format(int(image.shape[2])))



