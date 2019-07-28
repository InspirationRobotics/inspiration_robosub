from navigation.rc import RCLib
import time
import navigation.imu as imu
from navigation.log import *

log = LogLib()
rc = RCLib(log)

rc.setmode('ALT_HOLD')

rc.arm()

print 'Throttle'
rc.throttle("time", 3, -0.20)
rc.throttle("time", 120, 0)

