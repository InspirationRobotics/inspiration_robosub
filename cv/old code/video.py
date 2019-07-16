import numpy as np
import cv2
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help = "path to the video")
args = vars(ap.parse_args())

#load the video
cap = cv2.VideoCapture(args["video"])

while(cap.isOpened()):
	ret, frame = cap.read()

	#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)'''

	vid_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# define the list of boundaries
	# lower mask (0-10)
	lower_red = np.array([0,10,10])
	upper_red = np.array([55,255,255])
	mask0 = cv2.inRange(vid_hsv, lower_red, upper_red)
	                      									#for red color
	# upper mask (170-180)
	lower_red = np.array([140,0,0])
	upper_red = np.array([185,255,255])
	mask1 = cv2.inRange(vid_hsv, lower_red, upper_red)

	# join my masks
	mask = mask0 + mask1

	#define the list of boundaries
	'''lower_blue = np.array([5, 50, 50]) #[37.5, 50, 50]
	upper_blue = np.array([115, 255, 255]) #[105, 255, 255]

	mask = cv2.inRange(img_hsv, lower_blue, upper_blue)'''


	boundaries = [
		#([40, 39, 59], [150, 149, 180]) #gate.png 
		#([99, 99, 99], [104, 104, 104]) #gray2.png                            #must be converted to
		#([75, 94, 98], [113, 113, 119]) #gate2.png                             #HSV  
		#([74, 92, 96], [118, 122, 122]) #gate2.png #113 #this should work for most gates 
		#([60, 0, 0], [80, 2.6, 45.9]) #gate3.png HSV (rgb= ([78, 99, 99], [114, 117, 116]))
	]

	# loop over the boundaries
	'''for (lower, upper) in boundaries:
		# create NumPy arrays from the boundaries
		lower = np.array(lower, dtype = "uint8")
		upper = np.array(upper, dtype = "uint8")
	 
		# find the colors within the specified boundaries and apply
		# the mask
		mask = cv2.inRange(image, lower, upper)'''
	output = cv2.bitwise_and(frame, frame, mask = mask)
	 
		# show the images
		#find contours 
		#instead of showing image on screen print x coordinages, convert into percentage, find width of gate 
	#cv2.imshow("video", np.hstack([frame, output]))
	cv2.imshow('frame', output)
		#cv2.imwrite("gray.png", output)
		#cv2.imwrite("mask.png", output)
		#cv2.imwrite("mask2.png", output)
		#cv2.imwrite("mask3.png", output)
	#cv2.imwrite("mask4.png", output)
	#cv2.imwrite("mask5.png", output)



	#cv2.imshow('frame', gray)
	if cv2.waitKey(0) & 0xFF == ord('q'):
			break


	cap.release()
	cv2.destroyAllWindows()