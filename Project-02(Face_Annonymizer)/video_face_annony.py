# this is for folder structure
import os

#this library using for video purpose
import argparse

import cv2
import mediapipe as mp


### This function is for video annonymization ###

def process_img(img, face_detection):
    
    H, W, _ = img.shape
    
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

#this is for video purpose#
args = argparse.ArgumentParser()
# args.add_argument("--mode", default='image')
args.add_argument("--mode", default='video')
# args.add_argument("--filePath", default='./data/herh1m.jpg')
args.add_argument("--filePath", default='./data/LISA-_MONEY.mp4')

args = args.parse_args()

#this is for video purpose#



output_dir = './output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


# detect face

mp_face_detection = mp.solutions.face_detection

with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
    # pass

    if args.mode in ['image']:
        # read image
        
        img = cv2.imread(args.filePath)
       
        img = process_img(img, face_detection)
   
        # save image
        cv2.imwrite(os.path.join(output_dir, 'herh1m_output.png'), img)

    # here comes video
    elif args.mode in ['video']:

        cap = cv2.VideoCapture(args.filePath)
        ret, frame = cap.read()


        output_video = cv2.VideoWriter(os.path.join(output_dir, 'output_video.mp4'), 
                                       cv2.VideoWriter_fourcc(*'mp4v'), 
                                       30, 
                                       (frame.shape[1], frame.shape[0])) #this is height and width of video frame.shap[1] is width and frame.shape[0] is height



        while ret:
            img = process_img(frame, face_detection)
            
            output_video.write(frame)

            ret, frame = cap.read()

        cap.release()

        output_video.release()



    # cv2.imshow('img', img)
    # cv2.waitKey(0)


