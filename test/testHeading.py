from navigation.rc import RCLib
import time
import navigation.imu as imu


rc = RCLib()

rc.setmode('MANUAL')

rc.arm()

while(1):
  print(rc.getDeg())

rc.close()

