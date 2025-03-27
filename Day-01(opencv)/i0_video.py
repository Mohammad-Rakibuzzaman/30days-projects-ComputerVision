### video 
import cv2
import os

### read video
video_path = os.path.join('.', 'data', 'LISA-_MONEY.mp4')

video = cv2.VideoCapture(video_path)

## visualize video

ret = True
while ret:
    ret, frame = video.read()

    if ret:
        cv2.imshow('frame', frame)
        cv2.waitKey(30)

video.release()
cv2.destroyAllWindows()
 
# ret = True
# fps = video.get(cv2.CAP_PROP_FPS)  # Get the video frame rate
# delay = int(1000 / fps)           # Calculate delay per frame in milliseconds

# while ret:
#     ret, frame = video.read()
#     if ret:
#         cv2.imshow('frame', frame)
#         # cv2.waitKey(delay)  # Use dynamic delay based on FPS
#         fps = video.get(cv2.CAP_PROP_FPS)  # Get video's FPS
#         delay = int(1000 / fps)            # Calculate delay per frame
#         cv2.waitKey(delay)                 # Use dynamic delay

        
