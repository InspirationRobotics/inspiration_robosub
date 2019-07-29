from navigation.log import *
from navigation.rc import *
from navigation.cv import *
import time

print  cv2.__file__
log = LogLib()
log.setLevel(INFO)
rc = RCLib(log)
cv = CVThread()
cv.start()

seeingGate = 1
while seeingGate:
    
    print(cv.getCVOut())
    time.sleep(0.1)
    
log.flush()

cv.stop()
