from navigation.rc import RCLib
import time
import navigation.imu as imu


rc = RCLib()

rc.setmode('MANUAL')

rc.arm()

rc.getDeg()
#rc.throttle("time", 4, -0.25)
#rc.forward("time", 15, 0.25)
#rc.lateral("time", 2, 0.25)
#rc.forward("time", 3, 0.25)
#rc.lateral("time", 7, -0.25)
#rc.forward("time", 3, -0.25)
#rc.lateral("time", 3, -0.25)
#rc.forward("time", 15, -0.25)
