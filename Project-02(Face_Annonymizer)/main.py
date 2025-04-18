import os

import cv2
import mediapipe as mp


### This function is for video annonymization ###

def process_img(img, face_detection):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    out = face_detection.process(img_rgb)

    # print(out.detections)

    if out.detections is not None:
        for detection in out.detections: 
            location_data = detection.location_data
            bbox = location_data.relative_bounding_box

            x1, y1, w, h = bbox.xmin, bbox.ymin, bbox.width, bbox.height       

            x1 = int(x1 * W)
            y1 = int(y1 * H)
            w = int(w * W)
            h = int(h * H)

            # img = cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 10)
    
            # blur faces
            img[y1:y1 + h, x1:x1 + w, :] = cv2.blur(img[y1:y1 + h, x1:x1 + w, :], (40, 40) )

    return img

output_dir = './output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# read image
img_path = './data/she.jpg'
img = cv2.imread(img_path)


H, W, _ = img.shape

# detect face

mp_face_detection = mp.solutions.face_detection

with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
    # pass
    img = process_img(img, face_detection)
   


    # cv2.imshow('img', img)
    # cv2.waitKey(0)

# save image
cv2.imwrite(os.path.join(output_dir, 'she_output.png'), img)
