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

time.sleep(60)

log.flush()

cv.stop()
