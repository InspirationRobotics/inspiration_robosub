from navigation.rc import RCLib
import time
import navigation.imu as imu


rc = RCLib()

rc.setmode('ALT_HOLD')

rc.arm()

print 'Throttle'
rc.throttle("time", 3, -0.20)


