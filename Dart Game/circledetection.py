import cv2
import numpy as np
  
# Read image.
img = cv2.imread('left_cam.png', cv2.IMREAD_COLOR)
kernel = np.ones((5, 5), 'uint8')
dilate_img = cv2.dilate(img, kernel, iterations=1)
img = cv2.erode(dilate_img, kernel, iterations=1)
#ret, img = cv2.threshold(img_erosion, 150, 255, cv2.THRESH_BINARY)
  
# Convert to grayscale.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
# Blur using 3 * 3 kernel.
gray_blurred = cv2.blur(gray, (3, 3))
  
# Apply Hough transform on the blurred image.
# detected_circles = cv2.HoughCircles(gray_blurred, 
#                    cv2.HOUGH_GRADIENT, 1, 2, param1 = 50,
#                param2 = 30, minRadius = 1, maxRadius = 40)
detected_circles = cv2.HoughCircles(gray_blurred, 
                   cv2.HOUGH_GRADIENT, 1, 2, param1 = 50,
               param2 = 30, minRadius = 50, maxRadius = 150)
  
# Draw circles that are detected.

if detected_circles is not None:
  
    # Convert the circle parameters a, b and r to integers.
    detected_circles = np.uint16(np.around(detected_circles))
  
    for pt in detected_circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]
  
        # Draw the circumference of the circle.
        cv2.circle(img, (a, b), r, (0, 255, 0), 2)
  
        # Draw a small circle (of radius 1) to show the center.
        cv2.circle(img, (a, b), 1, (0, 0, 255), 3)
        cv2.imshow("Detected Circle", img)
        cv2.waitKey(0)