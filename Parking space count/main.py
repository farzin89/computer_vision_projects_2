
import cv2
import pickle
import cvzone
import numpy as np

cap = cv2.VideoCapture('C:\Parking Sapace Video\carPark.mp4')

while True :

    # in order to loop video
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
       cap.set(cv2.CAP_PROP_POS_FRAMES,0)


    success,img = cap.read()
    cv2.imshow("Image",img)
    cv2.waitKey(1)