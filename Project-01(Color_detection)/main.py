
import cv2
from util import get_limits
from PIL import Image # Pillow library for image processing specially for drawing bounding boxes

purple = [128, 0, 128] #purple in BGR colorspace

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()


    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=purple)

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask) # Convert mask to PIL Image for drawing

    bbox = mask_.getbbox() # Get bounding box of the mask



    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5) # Draw bounding box on the original frame

    # print(bbox) # Print the bounding box coordinates

    cv2.imshow('frame', frame)
    # cv2.imshow('frame', mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()

cv2.destroyAllWindows()