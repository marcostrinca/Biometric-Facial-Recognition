import cv2
import numpy as np

CASCADE_PATH = "haarcascade_frontalface_default.xml"

def getFaceCoordinates(image):
    cascade = cv2.CascadeClassifier(CASCADE_PATH)
    
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.equalizeHist(img_gray)
    rects = cascade.detectMultiScale(
        img_gray,
        scaleFactor=1.1,
        minNeighbors=3,
        minSize=(48, 48)
        )

    # For now, we only deal with the case that we detect one face.
    if(len(rects) != 1) :
        return None
    
    face = rects[0]
    bounding_box = [face[0], face[1], face[0] + face[2], face[1] + face[3]]

    return bounding_box