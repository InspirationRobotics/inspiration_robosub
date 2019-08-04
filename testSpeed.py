from navigation.rc import RCLib
import time
import navigation.imu as imu

rc = RCLib()
rc.arm()
# depth hold and go down
rc.setmode('ALT_HOLD')
rc.throttle("time", 2, -0.5)
rc.forward("time", 4, 0.8)

rc.disarm()
rc.close()
