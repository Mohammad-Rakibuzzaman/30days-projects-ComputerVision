# import os
#
# import cv2
#
# img = cv2.imread(os.path.join('.', 'data', 'GjbRnviasAAmda9.jpg'))
#
# print(img.shape)
#
# cropped_img = img[250:520, 160:520] #height then width
#
# cv2.imshow('img', img)
# cv2.imshow('cropped_img', cropped_img)
# cv2.waitKey(0)
#
import os
import cv2

# Mouse callback function to display coordinates
def show_coordinates(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        # Make a copy of the original image to prevent drawing artifacts
        display_img = img.copy()
        # Get pixel value at (x, y)
        b, g, r = display_img[y, x]
        # Text to display
        text = f'X: {x}, Y: {y}, BGR: ({b}, {g}, {r})'
        # Draw text on the image
        cv2.putText(display_img, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (150, 185, 130), 2, cv2.LINE_AA)
        # Show the updated image
        cv2.imshow('img', display_img)

# Load the image
img = cv2.imread(os.path.join('.', 'data', 'GjbRnviasAAmda9.jpg'))

# Check if the image loaded correctly
if img is None:
    raise FileNotFoundError("Image not found")

print(img.shape)

# Crop the image
cropped_img = img[250:520, 160:520] # height then width

# Display the original and cropped images
cv2.imshow('img', img)
cv2.imshow('cropped_img', cropped_img)

# Set mouse callback to display coordinates
cv2.setMouseCallback('img', show_coordinates)

cv2.waitKey(0)
cv2.destroyAllWindows()
