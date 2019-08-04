import time

# Import mavutil
from pymavlink import mavutil

def getDeg(master) :
    while True:
        try:

            ret = master.recv_match(type='ATTITUDE')
            if (ret != None ):
               att_val = ret.to_dict() 
               roll = ((180/3.14159265358618)* att_val['yaw'])
            else:
               roll = 0
            
            if roll < 0:

                return 360 + roll

            if roll > 0:

                return(roll)

        except Exception as e:
            print(e)
            pass

def getAlt(master) :
    while True:
        try:
            ret = master.recv_match(type='VFR_HUD', blocking=True)
            if (ret != None ):
               gp_val = ret.to_dict() 
               alt = (gp_val['alt'])
            #else:
               #alt = 0
            
            return(alt)

        except Exception as e:
            print(e)
            pass



def getAllData(master) :
    while True:
        try:

            att_val = master.recv_match(type='ATTITUDE').to_dict()

            return att_val

        except:
            pass
