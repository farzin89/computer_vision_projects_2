import time
import cv2
import mediapipe as mp

class FaceDetectior():
    def __init__(self,minDetectionCon=0.5):

        self.minDetectionCon = minDetectionCon
        self.mpFaceDetection = mp.solutions.face_detection
        self.moDraw = mp.solutions.drawing_utils
        self.mpFaceDetection = self.mpFaceDetection.FaceDetection(0.75)










def main():
    cap = cv2.VideoCapture(0)
    pTime = 0

    while True:
        success,img = cap.read()
        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime
        cv2.putText(img,f'FPS: {int(fps)}',(20,70),cv2.FONT_HERSHEY_PLAIN,3,(0,255,0),2)
        cv2.imshow("Image",img)
        cv2.waitKey(1)





if __name__ == "__main__":
    main()
