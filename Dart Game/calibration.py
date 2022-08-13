
# importing the module
import cv2
import numpy as np

clicks = 0
points = []
# function to display the coordinates of
# of the points clicked on the image

def reset_values():
    global clicks
    global points
    clicks = 0
    points = []

def click_event(event, x, y, flags, params):
    global clicks
    global points
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
 
        # displaying the coordinates
        # on the Shell
        points.append((x,y))
        clicks = clicks + 1
        if(clicks == 4):
            cv2.destroyAllWindows()
            return points


 
def select_points(image):
    # reading the image

    # displaying the image
    cv2.imshow('image', image)

    # setting mouse handler for the image
    # and calling the click_event() function
    cv2.setMouseCallback('image', click_event)

    # wait for a key to be pressed to exit
    cv2.waitKey(0)
    # close the window
    cv2.destroyAllWindows()

img = cv2.imread('left_cam.png', 1)
board = cv2.imread('board_calibration.png', 1)

select_points(board)
board_points = points
reset_values()

select_points(img)
cam_points = points
reset_values()

board_points = np.array([board_points[0], board_points[1], board_points[2], board_points[3]], dtype=np.float32)
cam_points = np.array([cam_points[0], cam_points[1], cam_points[2],cam_points[3]], dtype=np.float32)

cam_to_board = cv2.getPerspectiveTransform(cam_points, board_points)
print(cam_to_board)

warp = cv2.warpPerspective(img, cam_to_board, (640, 480))
print(cam_to_board)
np.save("transformation_matrix", cam_to_board, allow_pickle=True, fix_imports=True)
cv2.imshow("Warp", warp)
cv2.waitKey(0)

#warp = np.load('transformation_matrix.npy', mmap_mode='r')
