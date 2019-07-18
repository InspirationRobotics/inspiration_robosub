from nms import non_max_suppression_fast
import numpy as np
import cv2
import imutils

cap = cv2.VideoCapture('underwaterpaper.mp4')

while(cap.isOpened()):
	ret, frame = cap.read()

	#crop_img = frame[60:120, 0:160]

	height = np.size(frame)
	width = np.size(frame)


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
	#cv2.imshow("frames", np.hstack([frame, output]))

	#convert images to grayscale
	gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (5,5), 0)
	#cv2.imshow("Gray", gray)
	#cv2.waitKey(0)


	mask = gray.copy()
	kernel = np.ones((5,5),np.uint8)
	eroded = cv2.erode(mask, kernel, iterations=4)
	#cv2.imshow("eroded", eroded)
	#cv2.waitKey(0)

	#Erosions and dilations
	#erosions are apploed to reduce the size of foreground objects
	mask = gray.copy()
	kernel = np.ones((5,5),np.uint8)
	dilated = cv2.dilate(eroded, kernel, iterations=3)
	#cv2.imshow("dilated", dilated)
	#cv2.waitKey(0)

	#cv.Mat vesselImage = cv.imread(mask)


	#edge detection
	#applying edge detection 
	edged = cv2.Canny(dilated, 30,150)
	#cv2.imshow("Edged", edged)
	#cv2.waitKey(0)

	#detecting and drawing countours
	#find contours(outlines) of the foreground objects in the thresholded image
	cnts, heirarchy = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	#cv2.drawContours(immat,contours,-1,CV_RGB(255,0,0),2);
	cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:2]

	print('cnts:')
	print(cnts)
	print('=========')
	#cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	# cnts = imutils.grab_contours(cnts)
	#grabbedcnts = imutils.grab_contours(cnts)
	#output = image.copy()

	#loop over the contours
	'''for c in grabbedcnts:
			#draw wach contour on the output image with a 3px thick purple
			#outline, then display the output contours one at a time
			cv2.drawContours(output, [c], -1, (0,255,0),1)
			cv2.imshow("Contours", output)'''
	#cnts = cnts[0]50
	M = cv2.moments(cnts[0])
	print (M)
	#print(len(cnts))
	#draw the total number of countours found in purple
	#text = "{} objects found!!!!!!".format(len(cnts))
	#cv2.putText(output, text, (10.25), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
		#(240,0,159),2)
	#cv2.imshow("Contours", output)
	#cv2.waitKey(0)

	#this same code can be applied with Dilate/Dilated instead of Erode/Eroded

	# loop over the contours

	boundingBoxes = np.empty((0, 4), float)

	for c in cnts:
		#approcimate the contour
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.02 * peri, True)

		for x in range(len(approx)):
			cv2.circle(frame, (approx[x][0][0], approx[x][0][1],), 7, (0, 0, 255), -1)
		#cv2.Circle(image, (approx[1][0][0], approx[1][0][1],), 7, (0, 0, 255), -1)

		print(approx)


		x,y,w,h = cv2.boundingRect(c)
		#boundingBoxes.append(np.array[x,y,w,h])
		boundingBoxes = np.append(boundingBoxes, np.array([[x,y,x+w,y+h]]), axis = 0)
		#boundingBoxes = np.append(boundingBoxes, np.array([[h,w,y,x]]), axis = 0)
		cv2.rectangle(frame,(x,y), (x+w, y+h), (0,255,0), 2)
		cv2.imshow("bounding rectangle",frame)
		#cv2.waitKey(0)

		print(str(x/width) + " " + str(y/height) + " " + str((x+w)/width) + " " +  str((y+h)/height))


		if M["m00"] != 0:
			cX = int(M["m10"] / M["m00"])
			cY = int(M["m01"] / M["m00"])
		else:
			cX, cY = 0,0


		print(cX/width, cY/height)

	print("Bounding Boxes:")
	print(boundingBoxes)
	 
	# perform non-maximum suppression on the bounding boxes
	pick = non_max_suppression_fast(boundingBoxes, 0.1)
	print ("[x] after applying non-maximum, %d bounding boxes" % (len(pick)))

	# loop over the picked bounding boxes and draw them
	for (startX, startY, endX, endY) in pick:
		cv2.rectangle(frame, (startX, startY), (endX, endY), (255, 255, 255), 2)

	# display the images
	#cv2.imshow("Original", orig)
	cv2.imshow("After NMS", frame)
	#cv2.waitKey(0)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()