from navigation.rc import RCLib
from navigation.ac import ACLib
import time
import navigation.imu as imu

# global "origin" parameter (In degrees)
A1 = 287
#A1: Dock to gate
A2 = 287
#A2: Gate to Octagon
A3 = 119
#A3: Octagon to buoy
A4 = 119-90
#A4: Point left of buoy (A3 - 90)


#DIstance values for movement, but it is in seconds!
D1 = 15.66
#D1: Dock to gate
D2 = 25.07
#D2: Gate to octagon

#Sonar values in milimeters
S1 = 5600
#Sonar dist from center of octagon to front wall
S2 = 4600
#Sonar dist from center of octagon to side wall

MIN_BUOY_DIST = 3
MAX_BUOY_DIST = 8

WALL_DIFF = 3
WALL_DISTANCE = 4800

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
    while ((confidence < 65) and (counter < 5)):
        pingReturn = ac.get_distance_left()
        wallDist1 = pingReturn[0]
        confidence = pingReturn[1]
        counter = counter + 1
    print 'wall 1' , wallDist1

    pingReturn = ac.get_distance_right()
    wallDist2 = pingReturn[0]
    confidence = pingReturn[1]
    counter = 0
    while ((confidence < 65) and (counter < 5)):
        pingReturn = ac.get_distance_right()
        wallDist2 = pingReturn[0]
        confidence = pingReturn[1]
        counter = counter + 1
    print 'wall 2' , wallDist2

    if(wallDist1 > wallDist2 + WALL_DIFF):
       rc.raw('yaw', 1440);
       time.sleep(0.3)
       #rc.raw('yaw', 1500)

    if(wallDist2 > wallDist1 + WALL_DIFF):
       rc.raw('yaw', 1560);
       time.sleep(0.3)
       #rc.raw('yaw', 1500)

def fwdAlign(value) :
    
    pingReturn = ac.get_distance_forward()
    wallDist = pingReturn[0]
    confidence = pingReturn[1]
    counter = 0
    while ((confidence < 20) and (counter < 10)):
        pingReturn = ac.get_distance_forward()
        wallDist = pingReturn[0]
        confidence = pingReturn[1]
        counter = counter + 1
    print 'wall' , wallDist
    if wallDist > 10000:
        wallDist = 10000
    if wallDist <  1000:
        wallDist = 1000
    print 'wall' , wallDist
    print 'counter ' , counter
    diff =  value - wallDist
    print 'Fwd diff ' , diff
    
    diffTime = (diff/10)*(1/91.44)
    if diffTime > 0:
        rc.forward('time', diffTime*2, 0.32)
    if diffTime < 0 :
        rc.forward('time', diffTime*2, -0.32)


def leftAlign(value) :

    pingReturn = ac.get_distance_left()
    wallDist = pingReturn[0]
    confidence = pingReturn[1]
    counter = 0
    while ((confidence < 30) and (counter < 10)):
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

    if diff > 200 :
        rc.lateralDist(diff)
    

def rightAlign(value) :
    pingReturn = ac.get_distance_right()
    wallDist = pingReturn[0]
    confidence = pingReturn[1]
    counter = 0
    while ((confidence < 90) and (counter < 50)):
        pingReturn = ac.get_distance_right()
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
    diff =   wallDist - value
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
    i = 0
    while ((abs(diff) >25 or abs(diff_accum) < 1500) and i < 500):
        i = i+1
        dist = ac.get_distance_forward()[0]
        conf = ac.get_distance_forward()[1]
        if(conf > 50):
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
    buoyDist = ac.get_distance_forward()[0]
    buoyDist = (buoyDist/(1000*0.45)) + 2
    rc.forward('time', buoyDist, 0.32)
    rc.forward('time', buoyDist, -0.32)
    
def lowestSonarNeg(speed) :

    #pwm = 1500 + (0.4*speed*1000)
    pwm=1440
    rc.raw('yaw', pwm)
    
    prev_val = 0
    current_val = ac.get_distance_forward()[0]
    diff_accum = 0
    diff = 0
    i = 0
    while ((abs(diff) >25 or abs(diff_accum) < 1500) and i < 500):
        i = i+1
        dist = ac.get_distance_forward()[0]
        conf = ac.get_distance_forward()[1]
        if(conf > 50):
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
    buoyDist = ac.get_distance_forward()[0]
    buoyDist = (buoyDist/(1000*0.45)) + 2
    rc.forward('time', 10, 0.32)
    rc.forward('time', 10, -0.32)

# Begin program
# depth hold and go down
rc.setmode('ALT_HOLD')
rc.throttle("time", DEPTH_SEC, -0.5)

# align with the origin 
rc.imu_turn(A1)

rc.forward("time", D1, 0.8)


#dance
rc.yaw("imu", 180, 0.3)
rc.yaw("imu", 180, 0.3)
rc.yaw("imu", 180, 0.3)
rc.yaw("imu", 200, 0.3)


rc.imu_turn(A2)
rc.forward("time", (0.75*D2), 0.32)

fwdAlign(S1)
leftAlign(S2*2)
fwdAlign(S1)
leftAlign(S2)

rc.throttle("time", 6, 0.5)
rc.throttle("time", DEPTH_SEC, -0.5)

rc.imu_turn(A3)
rc.forward('time', 6.561, 0.8)

rc.throttle('time', 4, -0.5)

rc.imu_turn(A4)
lowestSonar(0.16)

rc.imu_turn(A3)

i = 0
while(i < 10):
    rc.lateralDist(500)
    meters = 6 + i
    meterTime = (meters*100)/91.44
    rc.forward('time', meterTime, 0.8)
    rc.forward('time', meterTime, -0.8)
    rc.imu_turn(A3)
    i = i+1

rc.disarm()
rc.close()
