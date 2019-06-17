from navigation.rc import RCLib
import time
import navigation.imu as imu


rc = RCLib()

rc.setmode('MANUAL')

rc.arm()
rc.yaw("imu", -20, 1) 
