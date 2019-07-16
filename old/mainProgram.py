from navigation.rc import RCLib
import time
import navigation.imu as imu

kP = 0.04

#def clipSteer(steerinp):
#    if (steerinp > 1):
#        steer = 1
#    elif (steerinp < 0.15) :
#        steer = 0.15
#    return steer
        
#def fixAngle():
#    error = rc.getDeg() - 48
#
#    while (abs(error) > 3):
#        steer = abs(error)*kP
#        steer = clipSteer(steer)
#
#        if (error>0) rc.raw('yaw', (1500 - (400*steer)) elif (error<0) rc.raw('yaw', (1500 + (400*steer)
                                                                               #       error = rc.getDeg() -48
            
        
originAngle = 48

rc = RCLib()

rc.setmode('ALT_HOLD')

rc.arm()

#fixAngle()
#endTime = time.time() + 7
#while(time.time() < endTime):
#    rc.raw('pitch', 1700)

rc.throttle("time", 2.5, -0.5)

rc.forward("time", 8, 0.4)


