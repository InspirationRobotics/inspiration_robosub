from rc import RCLib
import time

rc = RCLib()

rc.arm()

rc.throttle('time', 8, -0.25)

rc.setmode('ALT_HOLD')

rc.yaw('time', 20, 0)
