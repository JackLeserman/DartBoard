# importing the module
import cv2
import point_to_score
# function to display the coordinates of
# of the points clicked on the image
def click_event(event, x, y, flags, params):
 
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
 
        # displaying the coordinates
        # on the Shell

        point = (x,y)
        score = point_to_score.get_score(point)
        print(score)
        #point_to_score.score_to_text(score)
 
        # displaying the coordinates
        # on the image window
        cv2.imshow('image', img)
 
    # checking for right mouse clicks    
 
# driver function
if __name__=="__main__":
 
    # reading the image
    img = cv2.imread('board_crosshair.png', 1)
 
    # displaying the image
    cv2.imshow('image', img)
 
    # setting mouse handler for the image
    # and calling the click_event() function
    cv2.setMouseCallback('image', click_event)
 
    # wait for a key to be pressed to exit
    cv2.waitKey(0)
 
    # close the window
    cv2.destroyAllWindows()