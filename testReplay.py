from navigation.rc import RCLib
import time
import navigation.imu as imu


rc = RCLib()

rc.setmode('ALT_HOLD')

rc.arm()

rc.throttle("time", 2, -0.25)
#rc.imu_turn(290)
rc.replay2()

rc.disarm()
