from navigation.rc import RCLib
from navigation.ac import ACLib
import time
import navigation.imu as imu

rc = RCLib()
ac = ACLib()

rc.setmode('MANUAL')

rc.arm()

print(rc.getDeg())

# global "origin" parameter
START = 240
DEPTH_SEC = 4
SEC_PER_METER = 1
GATECENTER = 2500
def leftAlign() :
    pingReturn = ac.get_distance_fwd()
    wallDist = pingReturn[0]
    confidence = pingReturn[1]
    counter = 0
    while ((confidence < 70) and (counter < 50)):
        pingReturn = ac.get_distance_fwd()
        wallDist = pingReturn[0]
        confidence = pingReturn[1]
        counter = counter + 1
    print 'wall' , wallDist 
    print 'counter ' , counter 
    diff =  GATECENTER - wallDist
    print 'Laterl diff ' , diff
    rc.lateralDist(diff)

def rightAlign() :
    pingReturn = ac.get_distance_right()
    wallDist = pingReturn[0]
    confidence = pingReturn[1]
    counter = 0
    while ((confidence < 70) and (counter < 50)):
        pingReturn = ac.get_distance_right()
        wallDist = pingReturn[0]
        confidence = pingReturn[1]
        counter = counter + 1
    print 'wall' , wallDist 
    print 'counter ' , counter 
    diff =  GATECENTER - wallDist
    print 'Laterl diff ' , diff
    rc.lateralDist(diff)


# depth hold and go down
rc.setmode('ALT_HOLD')
rc.throttle("time", DEPTH_SEC, -0.25)

# align with the origin 
rc.imu_turn(START)

rc.forward("time", 10, 0.35)
leftAlign()
rc.imu_turn(START)
rc.forward("time", 10, 0.35)
leftAlign()
rc.imu_turn(START)
rc.forward("time", 10, 0.35)
leftAlign()

#diamond
rc.imu_turn(START-45)
rc.forward("time", 5, 0.25)

rc.imu_turn(START+45)
rc.forward("time", 5, 0.25)

rc.imu_turn(START+135)
rc.forward("time", 5, 0.25)

rc.imu_turn(START+225)
rc.forward("time", 5, 0.25)

rc.imu_turn(START+175)

rc.forward("time", 10, 0.35)
rightAlign()
rc.imu_turn(START+175)
rc.forward("time", 10, 0.35)
rightAlign()
rc.imu_turn(START+175)
rc.forward("time", 10, 0.35)
rightAlign()


rc.close()
