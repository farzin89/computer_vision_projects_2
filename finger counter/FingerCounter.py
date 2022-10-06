import cv2
import mediapipe as mp
import os

wCam,hCam = 640,480
cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

folderPath = "fingerImages"
myList = os.listdir(folderPath)

print(myList)
overlayList =[]
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
   # print((f'{folderPath}/{imPath}'))
    overlayList.append(image)
print(len(overlayList))


while True:
    success,img = cap.read()
    h,w,c = overlayList[0].shape
    img[0:h,0:w]=overlayList[0]

    

    cv2.imshow("image",img)
    cv2.waitKey(1)