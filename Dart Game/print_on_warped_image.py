import cv2
point = (270, 326)
img = cv2.imread('board.png')
cv2.circle(img, point, 10, (0, 0, 255), -1)
img = cv2.imread('board_calibration.png')
cv2.imshow("img", img)
cv2.waitKey(0)