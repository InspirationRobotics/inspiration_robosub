from navigation.rc import RCLib
import time
import navigation.imu as imu
from navigation.depth import DepthThread


rc = RCLib()
depththread = DepthThread(rc.getDev())

rc.setmode('ALT_HOLD')

rc.arm()

depththread.start()
depththread.resume()
while True:
    print(depththread.getDepth())
#while depththread.getDepth() > -0.5 :
    #rc.raw("throttle", 1430)

depththread.pause()
depththread.stop()
rc.disarm()
rc.close()
