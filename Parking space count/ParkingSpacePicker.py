
import cv2
import pickle

img = cv2.imread('carParkImg.png')

width,height = 107,48    #(50 -158)=107 and 240-192 = 48 each rectangle width and height
posList= []
def mouseClick(events,x,y,flags,params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x,y))
while True:

    #cv2.rectangle(img,(50,192),(158,240),(255,0,255),2)
    cv2.imshow('image',img)
    cv2.setMouseCallback("image",mouseClick)
    cv2.waitKey(1)


