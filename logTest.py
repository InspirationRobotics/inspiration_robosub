from navigation.log import *
from navigation.rc import *

log = LogLib()
rc = RCLib(log)

log.setLevel(DEBUG)
log.warning("Test Warning %d" % 10 )
log.error("Test error %d" % 10 )
log.info("Test info %d" % 10 )
log.debug("Test debug %d" % 10 )

rc.test()

log.flush()
