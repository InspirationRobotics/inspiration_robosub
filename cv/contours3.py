 # import the necessary packages
import numpy as np
import argparse
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

'''cap = cv.VideoCapture('5feet.mp4')
while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    if cv.waitKey(0) == ord('q'):
        break'''

# define the list of boundaries
# lower mask (0-10)
lower_red = np.array([0,10,10])
upper_red = np.array([55,255,255])
mask0 = cv2.inRange(img_hsv, lower_red, upper_red)
                                                        #for red color
# upper mask (170-180)
lower_red = np.array([140,0,0])
upper_red = np.array([185,255,255])
mask1 = cv2.inRange(img_hsv, lower_red, upper_red)

# join my masks
mask = mask0 + mask1

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

for i in range(len(contours)):
    color = (0,0,255)
    cv2.drawContours(thresh, contours_poly, i, color)
    '''if((boundRect[i][2] < max_width) and (boundRect[i][3] > min_length)):
        cv2.rectangle(thresh, (int(boundRect[i][0]), int(boundRect[i][1])), \
      (int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3])), color, 2)
        #cv2.circle(thresh, (int(centers[i][0]), int(centers[i][1])), int(radius[i]), color, 2)
        print('Cnt %d, x1 %d , y1 %d, x2 %d, y2 %d' % (i, int(boundRect[i][0]), int(boundRect[i][1]), int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3])))'''

print(len(contours))
cv2.imshow('Contours', thresh)
k = cv2.waitKey(0) & 0xFF
#if k == 27:
    #break
