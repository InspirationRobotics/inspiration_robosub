from navigation.rc import RCLib
from navigation.ac import ACLib
import time
import navigation.imu as imu


rc = RCLib()

#ac = ACLib()

rc.setmode('MANUAL')

rc.arm()

print("start")

# global "origin" parameter
START = 73 
DEPTH_SEC = 1
SEC_PER_METER = 1
GATECENTER = 2500
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
    if wallDist > 3800:
        wallDist = 3800
    if wallDist <  500:
        wallDist = 500
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
    current_val, _  = fwdSonar.dist()
    diff_accum = 0
    diff = 0

    while (abs(diff) >25 or abs(diff_accum) < 2500):
        dist, conf = fwdSonar.dist()
        if(conf > 70):
            prev_val =  current_val
            current_val = dist
            diff = abs(current_val-prev_val)
            diff_accum = diff+diff_accum
            rc.raw('yaw', pwm)
            #log.info(' current %d' % current_val )
            #log.info(' diff %d' % diff)
            #log.info(' accu_diff %d' % diff_accum)
        else:
            rc.raw('yaw', pwm)
            pass
        time.sleep(0.01)
    rc.raw('yaw', 1500)



# depth hold and go down
rc.setmode('ALT_HOLD')
rc.throttle("time", DEPTH_SEC, -0.25)

# align with the origin 
rc.imu_turn(START)

rc.forward("time", 10, 0.32)
rc.close()
'''leftAlign(5100)
rc.imu_turn(START)
rc.forward("time", 5, 0.32)
leftAlign(5100)
rc.imu_turn(START)
rc.forward("time", 5, 0.32)
leftAlign(5100)
rc.imu_turn(START)
rc.forward("time", 5, 0.32)
leftAlign(5100)
rc.imu_turn(START)

#dance
rc.imu_turn(START+360)
rc.imu_turn(START)
rc.imu_turn(START+360)
rc.imu_turn(START)
rc.forward("time", 3, 0.32)
leftAlign(5100)
rc.imu_turn(START)

#buoy
##log.info('Starting buoy test')
rc.throttle("time", 1, -0.25)
lowestSonar(0.16)
buoyDist, _  = fwdSonar.dist()
buoyDist = buoyDist/2000
if buoyDist > 8:
   buoyDist = 8 
#log.info("buoyDist %d" % buoyDist)
rc.forward("time", buoyDist, 0.32)
rc.close()
#log.info('Done buoy test')
time.sleep(1)
#log.flush()
print("Done Buoy Test")

fwdSonar.stop()
rc.close()
'''
