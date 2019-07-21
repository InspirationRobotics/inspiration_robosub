import numpy as np
import cv2
import imutils
import time

import threading

class CVThread (threading.Thread):
 def __init__(self ):
   threading.Thread.__init__(self)
   self._active = 1

 def stop(self) :
   self._active = 0

 def run(self):            
    cap = cv2.VideoCapture(0)
    width = int(cap.get(3))
    height = int(cap.get(4))
    print 'h' + ' ' + str(height) + ' ' + 'w' + ' ' + str(width)

    cycle = 0
    center_vals = []
    while(cap.isOpened() and (self._active == 1)):
            
    	ret, frame = cap.read()
    
    	cap_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    	# lower mask (0-10)
    	lower_red = np.array([15,40,40])
    	upper_red = np.array([40,255,255])
    	mask0 = cv2.inRange(cap_hsv, lower_red, upper_red)
    	# upper mask (170-180)
    	lower_red = np.array([140,0,0])
    	upper_red = np.array([185,255,255])
    	mask1 = cv2.inRange(cap_hsv, lower_red, upper_red)
    	# join my masks
    	mask = mask0 + mask1
    
    	output = cv2.bitwise_and(frame, frame, mask = mask)
    
    	#convert images to grayscale
    	gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
    	gray = cv2.GaussianBlur(gray, (5,5), 0)
    
    	mask = gray.copy()
    	kernel = np.ones((5,5),np.uint8)
    	eroded = cv2.erode(mask, kernel, iterations=4)
    
    	#Erosions and dilations
    	mask = gray.copy()
    	kernel = np.ones((5,5),np.uint8)
    	dilated = cv2.dilate(eroded, kernel, iterations=3)
    
    	#edge detection
    	#applying edge detection 
    	edged = cv2.Canny(dilated, 30,150)
    
    	#detecting and drawing countours
        cnts, heirarchy = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
    		cv2.CHAIN_APPROX_SIMPLE)
    	cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:2]
    
    	boundingBoxes = np.empty((0, 4), float)
        x1 = 0
        y1 = 0
        x2 = 0
        y2 = 0
        i = 0 

    	for c in cnts:
    		x,y,w,h = cv2.boundingRect(c)
    		cv2.rectangle(frame,(x,y), (x+w, y+h), (0,255,0), 2)
    		cv2.imshow("bounding rectangle",frame)
                cv2.waitKey(0)
                
                if i == 0: 
                  x1 = (x + w/2 )
                  y1 = (y + h/2 )
                  i = 1
                elif i == 1: 
                  x2 = (x + w/2 )
                  y2 = (y + h/2 )

        center = str(((x1 + x2) /2) - (width / 2) )
        center_vals.append(center)
        print center
        print center_vals
        cycle = cycle + 1

        if cycle > 10 :
            sum_vals = 1
            for x in center_vals :
                sum_vals = sum_vals + int(x, 10)
            print(sum_vals/len(center_vals))

            center_vals = []
            cycle = 0
            
        time.sleep(0.1)
                
    cap.release()
    cv2.destroyAllWindows()

