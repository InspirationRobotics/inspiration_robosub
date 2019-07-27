from navigation.rc import RCLib
import time
import navigation.imu as imu

rc = RCLib()

rc.setmode('MANUAL')

rc.arm()

print(rc.getDeg())

#time.sleep(2)
#rc.forward("time", 6, 0.25)
#rc.yaw("time", 1.2, -0.25)
#rc.forward("time", 3, 0.25)
#rc.yaw("time", 1.2, -0.25)
#rc.forward("time", 6, 0.25)`

start = 72

rc.setmode('ALT_HOLD')
rc.throttle("time", 3, -0.25)
while(1):
    rc.yaw("imu", 90, 0.15)

#rc.imu_turn(121.5)

#rc.yaw('imu', 90, 0.25)
