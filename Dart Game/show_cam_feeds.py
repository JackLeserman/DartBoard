import numpy as np
import cv2

cam1 = cv2.VideoCapture(1)
cam2 = cv2.VideoCapture(2)

while True:
    # Capture frame-by-frame
    ret1, frame1 = cam1.read()
    ret2, frame2 = cam2.read()

    if (ret1):
        # Display the resulting frame
        cv2.imshow('Cam 1', frame1)

    if (ret2):
        # Display the resulting frame
        cv2.imshow('Cam 2', frame2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cv2.destroyAllWindows()