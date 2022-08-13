import numpy as np
import cv2
import math
from transform_point import get_transformed_point

list_avg_x = []
list_avg_y = []
point = (0,0)
# creating object
fgbg1 = cv2.bgsegm.createBackgroundSubtractorMOG()
  
# capture frames from a camera 
cap = cv2.VideoCapture(1)
ret, frame = cap.read()
#frame = cv2.rotate(frame,cv2.ROTATE_180)
cv2.imwrite('board.png', frame)


while(1):
    # read frames
    ret, img = cap.read()
    #img = cv2.rotate(img,cv2.ROTATE_180)
    # apply mask for background subtraction
    fgmask1 = fgbg1.apply(img)

    kernel = np.ones((5, 5), 'uint8')
    dilate_img = cv2.dilate(fgmask1, kernel, iterations=1)
    img_erosion = cv2.erode(dilate_img, kernel, iterations=1)
    ret, img_erosion = cv2.threshold(img_erosion, 150, 255, cv2.THRESH_BINARY)

    #Contour Detection

    gaussian = cv2.GaussianBlur(img_erosion,(3,3),cv2.BORDER_DEFAULT)
    edges = cv2.Canny(gaussian,100,200)
    contours, hierarchy= cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    def get_contour_areas(contours):

        all_areas= []

        for cnt in contours:
            area= cv2.contourArea(cnt)
            all_areas.append(area)

        return all_areas


    try:
        sorted_contours= sorted(contours, key=cv2.contourArea, reverse= True)
        largest_contour = sorted_contours[0]
        largest_area = cv2.contourArea(largest_contour)
        left = tuple(largest_contour[largest_contour[:, :, 0].argmin()][0])
        
        if(largest_area > 600):
            point = left
            break
            #print(right) #RETURN POINT    
            #print(largest_area)


    except:
        print("error")
    cv2.imshow('frame', img_erosion)
    k = cv2.waitKey(200) & 0xff
    if k == 27:
        break

def rotate_point(frame, point):
    dimensions = frame.shape
    frame_x = dimensions[1]
    frame_y = dimensions[0]
    x = abs(point[0] - frame_x)
    y = abs(point[1] - frame_y)
    point = (x, y)
    return(point)

#TODO right version
point = rotate_point(frame, point)
point = get_transformed_point(point)

img = cv2.imread('board_calibration.png')


cv2.circle(img, point, 5, (0, 0, 255), -1)
cv2.imshow("img", img)

cv2.waitKey(0)

print("DONE")
cap.release()
cv2.destroyAllWindows()

#TODO 
#FIX ANGLED/WARP BOARD PLOTTING, ON THIS
#MIGHT HAVE TO DO WITH THE ROTATE_POINT