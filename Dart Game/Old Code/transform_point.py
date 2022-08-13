import cv2
import numpy as np

#takes in input of point and outputs it after transform
#transform is set manually using calibration.py
#Side takes in string "left" or "right"

def get_transformed_point(point, side):
    #MANUAL SET - USE CALIBRATION TO SET VALUES
    if side == "left":
        warp = np.matrix([ [ 7.18232998e-01, -2.67621067e-01, -6.53209732e+01],
        [ 6.50779498e-02,  6.17484423e-01, -4.71979062e+01],
        [-1.30298672e-03,  1.12829292e-04,  1.00000000e+00],])
    if side == "right":
        warp = np.matrix([[ 5.88593410e+00, -8.62448668e-01, -5.66390555e+02],
        [ 3.03848028e-01,  2.31995252e+00, -2.51899543e+02],
        [ 5.01098639e-03, -1.50815247e-03,  1.00000000e+00]])

    #dummy points to have a 3x3 and a 3x3 matix. Ignore (0,0) points.
    points = np.float32([[[point[0], point[1]]], [[0,0]], [[0,0]]])
    transformed = cv2.perspectiveTransform(points, warp)
    #board = cv2.imread('board.png')

    pt_x = int(transformed[0][0][0])
    pt_y = int(transformed[0][0][1])
    #print(pt_x, pt_y)
    point = (pt_x, pt_y)

    #Uncomment to show result on img
    # img = cv2.imread('board_calibration.png')
    # cv2.circle(img, point, 10, (0, 0, 255), -1)
    # cv2.imshow("img", img)
    # cv2.waitKey(0)

    return point


