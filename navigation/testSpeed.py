from rc import RCLib
import time

rc = RCLib()

rc.arm()

rc.throttle('time', 4, -0.25)

rc.imu_turn(71.5)

SPEED = 0.75

rc.forward('time', 9, SPEED)

