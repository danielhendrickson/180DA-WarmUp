# References: https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html, https://docs.opencv.org/4.x/dd/d49/tutorial_py_contour_features.html

import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

while(1):
			# Read captured webcam frame
	_, frame = cap.read()
			# Convert color frame into HSV (for RGB ignore this line and change upper and lower boundary values)
	hsv_img = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
			# Specify HSV range of object
	lower_blue = np.array([110,50,50])
	upper_blue = np.array([130,255,255])
	mask = cv.inRange(hsv_img, lower_blue, upper_blue)
			# Find contours from HSV masked image
	contours, hierarchy = cv.findContours(mask,cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)[-2:]
	cnt = [cv.contourArea(c) for c in contours]
			# If there are contours
	if len(cnt) > 0:
		max_index = np.argmax(cnt)
		count = contours[max_index]
		x,y,w,h = cv.boundingRect(count)
		cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0), 2)
 			# Display the resulting frame
	cv.imshow('frame',frame)
	k = cv.waitKey(5) & 0xFF
	if k == 27:
		break

cv.destroyAllWindows()
