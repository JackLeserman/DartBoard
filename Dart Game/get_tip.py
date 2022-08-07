import cv2
import numpy as np
image= cv2.imread('dart.png')
original_image= image

#Erode/Dialate

kernel = np.ones((5, 5), 'uint8')
dilate_img = cv2.dilate(original_image, kernel, iterations=1)
img_erosion = cv2.erode(dilate_img, kernel, iterations=1)
ret, dart_bnw = cv2.threshold(img_erosion, 150, 255, cv2.THRESH_BINARY)
img_erosion = dart_bnw


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



sorted_contours= sorted(contours, key=cv2.contourArea, reverse= True)
largest_contour = sorted_contours[0]

cv2.drawContours(img_erosion, sorted_contours[0], -1, (255,0,0),2)
right = tuple(largest_contour[largest_contour[:,:,0].argmax()][0])
cv2.circle(img_erosion, right, 5, (0, 255, 255), -1)
cv2.imshow('Dilated Image', img_erosion)
print(right) #RETURN POINT
cv2.waitKey(0)
cv2.destroyAllWindows()

