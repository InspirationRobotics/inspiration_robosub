import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    #frame = cv2.imread('test.png')
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_orange = np.array([5, 50, 50],np.uint8)
    upper_orange = np.array([15, 255, 255],np.uint8)
    
    mask = cv2.inRange(hsv, lower_orange, upper_orange)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    #cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    #cv2.imshow('res',res)
   
    ret, thresh = cv2.threshold(mask, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #x,y,w,h = cv2.boundingRect(cnt[0])
    #cv2.rectangle(thresh,(x,y),(x+w,y+h),(0,255,0),2)
    #cv2.imshow('cnt',thresh)

    contours_poly = [None]*len(contours)
    boundRect = [None]*len(contours)
    centers = [None]*len(contours)
    radius = [None]*len(contours)
    for i, c in enumerate(contours):
        contours_poly[i] = cv2.approxPolyDP(c, 3, True)
        boundRect[i] = cv2.boundingRect(contours_poly[i])
        centers[i], radius[i] = cv2.minEnclosingCircle(contours_poly[i])
    min_length = 150
    max_width = 150
    for i in range(len(contours)):
        color = (255,255,0)
        cv2.drawContours(thresh, contours_poly, i, color)
        if((boundRect[i][2] < max_width) and (boundRect[i][3] > min_length)):
            cv2.rectangle(thresh, (int(boundRect[i][0]), int(boundRect[i][1])), \
          (int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3])), color, 2)
            #cv2.circle(thresh, (int(centers[i][0]), int(centers[i][1])), int(radius[i]), color, 2)
            print('Cnt %d, x1 %d , y1 %d, x2 %d, y2 %d' % (i, int(boundRect[i][0]), int(boundRect[i][1]), int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3])))

    cv2.imshow('Contours', thresh)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()