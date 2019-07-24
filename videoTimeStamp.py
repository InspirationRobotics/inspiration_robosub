import cv2
import numpy as np
import time

cap = cv2.VideoCapture(2)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

fileName = 'capture' + '_' + str(time.localtime().tm_mon) + '_' + str(time.localtime().tm_mday) \
             + '_' + str(time.localtime().tm_hour) + '_' + str(time.localtime().tm_min) \
             + '_' + str(time.localtime().tm_sec) + '.avi'

out = cv2.VideoWriter(fileName,cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
success = 1
while(cap.isOpened()):

   success, frame = cap.read()
   if not success:
      break 

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
   

   #cv2.imshow('frame',frame)
   #if cv2.waitKey(1) & 0xFF == ord('q'):
   #   break 

cap.release()
out.release()
cv2.destroyAllWindows()
