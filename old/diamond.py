from navigation.rc import RCLib
import time
import navigation.imu as imu

rc = RCLib()

rc.setmode('MANUAL')

rc.arm()

print(rc.getDeg())

# global "origin" parameter
start = 72

# depth hold and go down
rc.setmode('ALT_HOLD')
rc.throttle("time", 3, -0.25)

# align with the origin 
rc.imu_turn(start)

rc.forward("time", 10, 0.35)

rc.yaw("imu", -45, 0.2)
rc.forward("time", 5, 0.25)

rc.yaw("imu", 90, 0.2)
rc.forward("time", 5, 0.25)

rc.yaw("imu", 90, 0.2)
rc.forward("time", 5, 0.25)

rc.yaw("imu", 90, 0.2)
rc.forward("time", 5, 0.25)

rc.imu_turn(start+180)
rc.forward("time", 10, 0.25)


