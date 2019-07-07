from rc import RCLib
import time
import imu as imu

rc = RCLib()

rc.setmode('ALT_HOLD')

rc.arm()

rc.throttle('time', 2, -0.5)

rc.setmode('ALT_HOLD')

time.sleep(0.5)

rc.imu_turn(61)

rc.setmode('ALT_HOLD')

#print(rc.getDeg())

rc.yaw('time', 10, 0)
#time.sleep(10)

print("----------")
print(rc.getDeg())

time.sleep(10)
