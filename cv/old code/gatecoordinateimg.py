import cv2
import numpy as np
import argparse

#construct the argument parse and parse the arugments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())

# load the image
image = cv2.imread(args["image"])

#apply filters
#gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY);
#gray = cv2.GaussianBlur(gray, (5, 5), 0)
#bin = cv2.threshold(gray,120,255,1) # inverted threshold (light obj on dark bg)
#bin = cv2.dilate(bin, None)  # fill some holes
#bin = cv2.dilate(bin, None)
#bin = cv2.erode(bin, None)   # dilate made our shape larger, revert that
#bin = cv2.erode(bin, None)
#bin, contours, hierarchy = cv2.findContours(bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# define the list of boundaries
boundaries = [
	([40, 39, 59], [150, 149, 180])
]

# loop over the boundaries
for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
 
	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)
bin, contours, hierarchy = cv2.findContours(bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

rc = cv2.minAreaRect(contours[0])
box = cv2.boxPoints(rc)
for p in box:
    pt = (p[0],p[1])
    print pt
    cv2.circle(im,pt,5,(200,0,0),2)
cv2.imshow("plank", im)
cv2.waitKey()

#output should be coordinates