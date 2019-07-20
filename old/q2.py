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
DEPTH_SEC = 5
SEC_PER_METER = 1
GATECENTER = 2500

# depth hold and go down
rc.setmode('ALT_HOLD')
rc.throttle("time", DEPTH_SEC, -0.25)

# align with the origin 
rc.imu_turn(START+180)

rc.forward("time", 5, -0.35)
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
diff =  wallDist - GATECENTER
print 'Laterl diff ' , diff
rc.lateralDist(diff)
rc.imu_turn(START+180)

rc.forward("time", 5, -0.35)
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
diff =  wallDist - GATECENTER
print 'Laterl diff ' , diff
rc.lateralDist(diff)
rc.imu_turn(START+180)

rc.forward("time", 5, -0.35)
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
diff =  wallDist - GATECENTER
print 'Laterl diff ' , diff
rc.lateralDist(diff)

rc.imu_turn(START)



while (ac.get_distance_fwd()[0] > 8900):
  rc.forward("time", 1, 0.35)

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

diff =  wallDist - GATECENTER
print 'Laterl diff ' , diff
rc.lateralDist(diff)

rc.imu_turn(START+175)
rc.forward("time", 7, 0.35)
#while (ac.get_distance_fwd()[0] > 1000):
#  rc.forward("time", 1, 0.35)

rc.close()
