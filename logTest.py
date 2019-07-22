from navigation.log import *
from navigation.rc import *
from navigation.cv import *
import time

log = LogLib()
log.setLevel(INFO)
rc = RCLib(log)
cv = CVThread(0, log)
cv.start()

log.critical("Test error %d" % 10 )
log.error("Test error %d" % 10 )
log.warning("Test Warning %d" % 10 )
log.info("Test info %d" % 10 )
log.debug("Test debug %d" % 10 )

rc.test()
cv.test()

time.sleep(6)
cv.stop()
time.sleep(1)
log.flush()
