from navigation.rc import RCLib
from navigation.ac import ACLib
import time
import navigation.imu as imu

# global "origin" parameter
D1 = 50

DEPTH_SEC = 1

rc = RCLib()

ac = ACLib()

rc.setmode('MANUAL')

rc.arm()

# depth hold and go down
rc.setmode('ALT_HOLD')
rc.throttle("time", DEPTH_SEC, -0.25)
rc.forward("time", D1, 0.32)

rc.disarm()
rc.close()
