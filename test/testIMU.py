from navigation.rc import RCLib
import time
import navigation.imu as imu


rc = RCLib()

rc.setmode('MANUAL')

rc.arm()

while (True) :
   try:
      rc.getDeg()
   except:
      print('in loop')
