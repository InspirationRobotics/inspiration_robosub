from navigation.log import *
from navigation.rc import *
from navigation.cv import *
import time

log = LogLib()
log.setLevel(INFO)
rc = RCLib(log)
cv = CVThread()
cv.start()

time.sleep(6)

log.flush()

cv.stop()
