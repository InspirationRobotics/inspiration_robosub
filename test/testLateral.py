from navigation.rc import RCLib
from navigation.ac import ACLib
import time
import navigation.imu as imu


rc = RCLib()
ac = ACLib()

rc.setmode('ALT_HOLD')

rc.arm()

rc.throttle("time", 3, -0.20)
#i = 0
#while i<500:
#    ac.get_distance_right()
#    rc.setmode('ALT_HOLD')
#    time.sleep(0.1)
#    i = i + 1
rc.forward("time", 6, 0.1)
wallDist = 0
counter = 0
while ((ac.get_distance_right()[1] < 70) and (counter < 50)):
        wallDist = ac.get_distance_right()[0]
        counter = counter +1
print 'wall' , wallDist
print 'counter ' , counter

diff =  ac.get_distance_right()[0] - 1500
print 'Laterl diff ' , diff
rc.lateralDist(diff)

rc.close()
