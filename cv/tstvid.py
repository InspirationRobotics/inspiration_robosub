import numpy as np
import cv2

cap = cv2.VideoCapture('images/realgate.mp4')

while(cap.isOpened()):
	ret, frame = cap.read()

	cap_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# define the list of boundaries
	# lower mask (0-10)
	lower_red = np.array([0,10,10])
	upper_red = np.array([55,255,255])
	mask0 = cv2.inRange(cap_hsv, lower_red, upper_red)
	                      									#for red color
	# upper mask (170-180)
	lower_red = np.array([140,0,0])
	upper_red = np.array([185,255,255])
	mask1 = cv2.inRange(cap_hsv, lower_red, upper_red)

	# join my masks
	mask = mask0 + mask1

	output = cv2.bitwise_and(frame, frame, mask = mask)
	 
		# show the images
		#find contours 
		#instead of showing image on screen print x coordinages, convert into percentage, find width of gate 
	cv2.imshow("frames", np.hstack([frame, output]))


	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()