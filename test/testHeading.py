from rc import RCLib
import time
import imu as imu

rc = RCLib()

rc.setmode('ALT_HOLD')

rc.arm()

#print(rc.getDeg())

#time.sleep(5)
INIT_VAL = 70

rc.throttle('time', 5.5, -0.25)

rc.setmode('ALT_HOLD')

time.sleep(0.5)

rc.imu_turn(INIT_VAL)
rc.setmode('ALT_HOLD')
rc.forward("time", 5, 0.5)
rc.throttle('time', 1, 0.5)
rc.forward('time', 8, 0.5)
rc.setmode('ALT_HOLD')
rc.imu_turn(INIT_VAL+90)
rc.setmode('ALT_HOLD')
rc.forward("time", 1.5, 0.5)
rc.setmode('ALT_HOLD')
rc.imu_turn(INIT_VAL+181)
rc.setmode('ALT_HOLD')
rc.forward("time", 7, 0.5)
rc.throttle('time', 1.25, -0.5)
rc.forward('time', 3, 0.5)

#rc.setmode('ALT_HOLD')
#rc.setmode('ALT_HOLD')

#rc.imu_turn(227)
#rc.setmode('ALT_HOLD')


#rc.forward('time', 1.5, -0.4)

print(rc.getDeg())

#rc.yaw('time', 10, 0)
#time.sleep(10)

print("----------")
print(rc.getDeg())

time.sleep(5)
