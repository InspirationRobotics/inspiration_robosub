from navigation.rc import RCLib
from navigation.log import *
import time
import navigation.imu as imu


log = LogLib()
log.setLevel(INFO)
rc = RCLib(log)

rc.setmode('ALT_HOLD')

rc.arm()

rc.throttle("time", 1, -0.25)

rc.forward("time", 3, 0.35)
log.flush()
