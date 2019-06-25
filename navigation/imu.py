import time

# Import mavutil
from pymavlink import mavutil

def getDeg(master) :
    while True:
        try:

            att_val = master.recv_match(type='ATTITUDE').to_dict()
            roll = ((180/3.14159265358618)* att_val['yaw'])
            
            if roll < 0:

                return 360 + roll

            if roll > 0:

                return(roll)

        except:
            pass
