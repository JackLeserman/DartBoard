from ensurepip import version
import cv2
import numpy as np

grn_Upper_HSV = (92, 186, 199)
grn_Lower_HSV = (30, 35, 142)

red_Upper_HSV = (12, 255, 255)
red_Lower_HSV = (0, 61, 148)

Upper_HSV = (100, 255, 255)
Lower_HSV = (86, 85, 165)

centroids = []
westmost = (0,0)
eastmost = (0,0)
northmost = (0,0)
southmost = (0,0)

img = cv2.imread('p1.png')

def get_rings():
    img = cv2.imread('transform.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask_grn = cv2.inRange(img, grn_Lower_HSV, grn_Upper_HSV)
    mask_red = cv2.inRange(img, red_Lower_HSV, red_Upper_HSV)

    rings = cv2.add(mask_grn, mask_red)

def get_transform_points():
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, Lower_HSV, Upper_HSV)

    #contour detection
    gaussian = cv2.GaussianBlur(mask,(3,3),cv2.BORDER_DEFAULT)
    edges = cv2.Canny(gaussian,100,200)
    contours, hierarchy= cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    def get_contour_areas(contours):

        all_areas= []

        for cnt in contours:
            area= cv2.contourArea(cnt)
            all_areas.append(area)

        return all_areas



    sorted_contours= sorted(contours, key=cv2.contourArea, reverse= True)
    for i in range(4):
        i = sorted_contours[i]
        M = cv2.moments(i)
        if M['m00'] != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            centroid = (cx, cy)
            centroids.append(centroid)


    northmost = centroids[0]
    southmost = centroids[0]
    eastmost = centroids[0]
    westmost = centroids[0]

    for i in centroids:
        if northmost[1] > i[1]:
            northmost = i 
        if southmost[1] < i[1]:
            southmost = i
        if westmost[0] > i[0]:
            westmost = i 
        if eastmost[0] < i[0]:
            eastmost = i

    # cv2.putText(img, "north", (northmost),
    #                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    # cv2.putText(img, "south", (southmost),
    #                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    # cv2.putText(img, "west", (westmost),
    #                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    # cv2.putText(img, "east", (eastmost),
    #                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    # cv2.line(img, northmost, southmost, (0, 255, 0), 2)
    # cv2.line(img, eastmost, westmost, (0, 0, 255), 2)

    print("North = " + str(northmost))
    print("South = " + str(southmost))
    print("West = " + str(westmost))
    print("East = " + str(eastmost))
    
    src_pts = np.array([northmost, southmost, westmost, eastmost], dtype=np.float32)
    dst_pts = np.array([(250,0), (250,500),(0,250),(500,250)], dtype=np.float32)

    M = cv2.getPerspectiveTransform(src_pts, dst_pts)
    warp = cv2.warpPerspective(img, M, (500, 500))

    cv2.imshow("Difference", warp)
    cv2.waitKey(0)
    return(M)


get_rings()
#get_transform_points()