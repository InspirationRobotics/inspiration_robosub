from navigation.rc import RCLib
import time
import navigation.imu as imu


rc = RCLib()

rc.setmode('ALT_HOLD')

rc.arm()

rc.throttle("time", 1, -0.5)

start = rc.getDeg()
rc.imu_turn(start+90)


#i=0
#while (i<50) :
#   rc.getDeg()
#   rc.raw("yaw", 1555)
#   i = i+1

#start = rc.getDeg()
#print(start)
#print('Now Yawing')
#rc.yaw("imu", 45, 0.2)

#turn=90

#end = int(turn + start)

#rc.yaw("imu", -45, 0.8)
#rc.yaw("imu", turn, 0.8)
#rc.yaw("imu", turn - rc.getDeg(), 0.1)
#rc.yaw("time", 2, 0.5)

#rc.disconnect()
