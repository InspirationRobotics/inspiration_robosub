from navigation.rc import RCLib
import time
import navigation.imu as imu


rc = RCLib()

rc.setmode('ALT_HOLD')

rc.arm()

rc.throttle("time", 4, -0.20)

rc.forward("time", 3, 0.20)
