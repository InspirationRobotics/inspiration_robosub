from navigation.log import *
from navigation.rc import *
from navigation.cv import *
import time

log = LogLib()
rc = RCLib(log)
cv = CVThread()
cv.start()

log.setLevel(INFO)
log.critical("Test error %d" % 10 )
log.error("Test error %d" % 10 )
log.warning("Test Warning %d" % 10 )
log.info("Test info %d" % 10 )
log.debug("Test debug %d" % 10 )

rc.test()

log.flush()

time.sleep(6)

cv.stop()
