import numpy as np
import cv2

left_cam = cv2.VideoCapture(1)
right_cam = cv2.VideoCapture(2)

while True:
    # Capture frame-by-frame
    ret0, frame0 = left_cam.read()
    ret1, frame1 = right_cam.read()

    if (ret0):
        # Display the resulting frame
        cv2.imshow('Cam 0', frame0)

    if (ret1):
        # Display the resulting frame
        cv2.imshow('Cam 1', frame1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture_0.release()
video_capture_1.release()
cv2.destroyAllWindows()