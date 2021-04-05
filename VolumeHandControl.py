import cv2
import time
import numpy as np
import HandTrackingModule as htm

# Setting the camera size
wCam, hCam = 640, 480

# Setting a variable to capture video from webcam.
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector()


while True:
    success, img = cap.read()
    
    img = detector.findHands(img)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}',(40,50), cv2.FONT_HERSHEY_COMPLEX, 1, (231, 76, 60), 3)
    cv2.imshow("Img", img)
    cv2.waitKey(1)

