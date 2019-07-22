import numpy as np
import cv2
import imutils
import time
from log import *

import threading

class CVThread (threading.Thread):
 def __init__(self, dump=0, logger=None):
   threading.Thread.__init__(self)

   if logger == None :
       logger = log.LogLib()
       
   self.log = logger
   
   self._active = 1
   self.write = dump

 def stop(self) :
   self._active = 0

 def test(self) :
    self.log.warning("test log from cv")

 def run(self):            
    cap = cv2.VideoCapture(0)
    width = int(cap.get(3))
    height = int(cap.get(4))
    out=None
    if self.write :
       out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (width,height))
    print 'h' + ' ' + str(height) + ' ' + 'w' + ' ' + str(width)
    self.log.warning("test log from cv")
    cycle = 0
    center_vals = []
    while(cap.isOpened() and (self._active == 1)):
        time.sleep(0.01)
            
    	ret, frame = cap.read()
        '''
        if self.write :
            timeStamp = str(time.localtime().tm_mon) + '_' + str(time.localtime().tm_mday) \
             + '_' + str(time.localtime().tm_hour) + '_' + str(time.localtime().tm_min) \
             + '_' + str(time.localtime().tm_sec) \
             + '_' + str((int(time.time()*1000))%1000)

            font                   = cv2.FONT_HERSHEY_SIMPLEX
            bottomLeftCornerOfText = (10,50)
            fontScale              = 1
            fontColor              = (0,0,255)
            lineType               = 2
            cv2.putText(frame, timeStamp , bottomLeftCornerOfText,
                        font, fontScale, fontColor, lineType)
            out.write(frame)
   
        '''
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
        self.log.info("Value: %s" % center)
        self.log.info("Array: %s" % center_vals)
        cycle = cycle + 1

        if cycle > 30 :
            sum_vals = 1
            for x in center_vals :
                sum_vals = sum_vals + int(x, 10)
            print(sum_vals/len(center_vals))

            center_vals = []
            cycle = 0
            
                
    cap.release()
    if self.write :
        out.release()
    cv2.destroyAllWindows()

