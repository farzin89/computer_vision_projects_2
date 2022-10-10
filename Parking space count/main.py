
import cv2
import pickle
import cvzone
import numpy as np

cap = cv2.VideoCapture('C:\Parking Sapace Video\carPark.mp4')

with open('CarParkPos', 'rb') as f:
    posList = pickle.load(f)

width,height = 107,48

def checkParkingSpace(imagepro):
    for pos in posList:
        x,y = pos

        imgCrop = img[y:y+height,x:x+width]
        cv2.imshow(str(x*y),imgCrop)


while True :

    # in order to loop video
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
       cap.set(cv2.CAP_PROP_POS_FRAMES,0)
    success, img = cap.read()

    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(3,3),1)

    # convert to binary image
    imgThreshold = cv2.adaptiveThreshold(imgBlur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                             cv2.THRESH_BINARY_INV,25,16)
    imgMedian = cv2.medianBlur(imgThreshold,5)

    #make thicker
    kernel = np.ones((3,3),np.uint8)
    imDilate = cv2.dilate(imgMedian,kernel,iterations = 1)



    checkParkingSpace(imDilate)
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)


    cv2.imshow("Image",img)
    cv2.imshow("ImageBlur", imgBlur)
    cv2.imshow("ImageThreshold", imgThreshold)
    cv2.imshow("ImageMedian", imgMedian)
    cv2.imshow("ImageDilate", imDilate)
    cv2.waitKey(1)

# is car inside the rectangle or not