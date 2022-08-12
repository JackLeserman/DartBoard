import cv2
import numpy as np

point = (270, 326)
point = np.matrix([270, 326, 0])

#MANUAL SET - USE CALIBRATION TO SET VALUES
warp = np.matrix([[ 7.89968272e-01, -2.64541343e-01, -8.38197078e+01],
 [ 9.19084850e-02,  6.81550635e-01, -6.53920643e+01],
 [-1.27777356e-03,  2.04800396e-04,  1.00000000e+00]])
print(warp)
tf = np.matmul(point, warp)
print(tf)

img = cv2.imread('board_calibration.png')
x = int(tf.item((0, 0)))
y = int(tf.item((0, 1)))
point = (x,y)
cv2.circle(img, point, 10, (0, 0, 255), -1)
cv2.imshow("img", img)
cv2.waitKey(0)