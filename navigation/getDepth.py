from rc import RCLib
import time
import imu as imu
from pymavlink import mavutil
import math
import time

master = mavutil.mavlink_connection(
                    '/dev/ttyACM0',
                    baud=115200)

master.wait_heartbeat()

while(True):
    try:
        att_val = master.recv_match(type='GLOBAL_POS_INT').to_dict()
        #print(att_val)
        yaw = att_val['alt']
        yaw_deg = math.floor(yaw * (180/3.141592))
        print(yaw_deg)
        #rc.getAllData()
        time.sleep(1)
    except:
        pass
                
