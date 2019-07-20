from nms import non_max_suppression_fast
import numpy as np
import cv2
import imutils



cap = cv2.VideoCapture('images/realgate.mp4')

while(cap.isOpened()):
	ret, frame = cap.read()

	'''height = np.size(frame, 0)
	width = np.size(frame, 1)'''

	#convert images to grayscale
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(cap, (5,5), 0)
	#cv2.imshow("Gray", gray)
	#cv2.waitKey(0)


