# importing libraries
import numpy as np
import cv2

list_avg_x = []
list_avg_y = []
# creating object
fgbg1 = cv2.bgsegm.createBackgroundSubtractorMOG()
  
# capture frames from a camera 
cap = cv2.VideoCapture(1)

while(1):
    # read frames
    ret, img = cap.read()
      
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
        right = tuple(largest_contour[largest_contour[:,:,0].argmax()][0])
        print(right) #RETURN POINT    
        print(largest_area)


    except:
        print("error")
    k = cv2.waitKey(200) & 0xff
    if k == 27:
        break

    

print("DONE")
cap.release();
cv2.destroyAllWindows();