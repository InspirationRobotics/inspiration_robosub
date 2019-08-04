from navigation.rc import RCLib
import time
import navigation.imu as imu


rc = RCLib()

rc.setmode('AUTO')

rc.arm()

while (True) :
   try:
      #print rc.getDeg()
      print rc.getAlt()
      time.sleep(0.01)
   except:
       print('exception in loop')
