
import cv2
import pickle
import cvzone
import numpy as np

cap = cv2.VideoCapture('C:\Parking Sapace Video\carPark.mp4')

with open('CarParkPos', 'rb') as f:
    posList = pickle.load(f)

width,height = 107,48

def checkParkingSpace():
    for pos in posList:
        x,y = pos

        imgCrop = img[y:y+height,x:x+width]
        cv2.imshow(str(x*y),imgCrop)
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)

while True :

    # in order to loop video
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
       cap.set(cv2.CAP_PROP_POS_FRAMES,0)
    success, img = cap.read()
    checkParkingSpace()


    cv2.imshow("Image",img)
    cv2.waitKey(1)

# is car inside the rectangle or not