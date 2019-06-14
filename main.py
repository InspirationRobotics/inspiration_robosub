
import navigation.rc as rc
import time
import navigation.imu as imu

rc.setmode('MANUAL')

rc.arm()
rc.yaw("imu", 90, 1) 
