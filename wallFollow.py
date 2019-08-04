from navigation.rc import RCLib
from navigation.ac import ACLib
import time
import navigation.imu as imu

# global "origin" parameter
A1 = 50
A2 = 50
A3 = 50

D1 = 32
D2 = 24
D3 = 47

MIN_BUOY_DIST = 1
MAX_BUOY_DIST = 3

DEPTH_SEC = 1.5
SEC_PER_METER = 1
GATECENTER = 2500


rc = RCLib()

ac = ACLib()

rc.setmode('MANUAL')

rc.arm()

print("start")

def check() :

    pingReturn = ac.get_distance_left()
    wallDist1 = pingReturn[0]
    confidence = pingReturn[1]
    counter = 0
    while ((confidence < 65) and (counter < 3)):
        pingReturn = ac.get_distance_left()
        wallDist1 = pingReturn[0]
        confidence = pingReturn[1]
        counter = counter + 1
    print 'wall 1' , wallDist1

    pingReturn = ac.get_distance_right()
    wallDist2 = pingReturn[0]
    confidence = pingReturn[1]
    counter = 0
    while ((confidence < 65) and (counter < 3)):
        pingReturn = ac.get_distance_right()
        wallDist2 = pingReturn[0]
        confidence = pingReturn[1]
        counter = counter + 1
    print 'wall 2' , wallDist2

    if(wallDist1 > wallDist2 + 10):
       rc.raw('yaw', 1440);
       time.sleep(0.3)
       #rc.raw('yaw', 1500)

    if(wallDist2 > wallDist1 + 10):
       rc.raw('yaw', 1560);
       time.sleep(0.3)
       #rc.raw('yaw', 1500)

def leftAlign(value) :

    pingReturn = ac.get_distance_left()
    wallDist = pingReturn[0]
    confidence = pingReturn[1]
    counter = 0
    while ((confidence < 65) and (counter < 10)):
        pingReturn = ac.get_distance_left()
        wallDist = pingReturn[0]
        confidence = pingReturn[1]
        counter = counter + 1
    print 'wall' , wallDist 
    if wallDist > 7000:
        wallDist = 7000
    if wallDist <  1000:
        wallDist = 1000
    print 'wall' , wallDist 
    print 'counter ' , counter 
    diff =  value - wallDist
    print 'Laterl diff ' , diff
    rc.lateralDist(diff)


def lowestSonar(speed) :

    #pwm = 1500 + (0.4*speed*1000)
    pwm=1560
    rc.raw('yaw', pwm)
    
    prev_val = 0
    current_val = ac.get_distance_forward()[0]
    diff_accum = 0
    diff = 0

    while (abs(diff) >25 or abs(diff_accum) < 2500):
        dist = ac.get_distance_forward()[0]
        conf = ac.get_distance_forward()[1]
        if(conf > 70):
            prev_val =  current_val
            current_val = dist
            diff = abs(current_val-prev_val)
            diff_accum = diff+diff_accum
            rc.raw('yaw', pwm)
        else:
            rc.raw('yaw', pwm)
            pass
        time.sleep(0.01)
    rc.raw('yaw', 1500)



# depth hold and go down
rc.setmode('ALT_HOLD')
rc.throttle("time", DEPTH_SEC, -0.25)

i = 0
while ( i < 500 ):
    i = i + 1
    check()
    leftAlign(1500)
    rc.forward("time", 1, 0.32)
    time.sleep(0.4)


