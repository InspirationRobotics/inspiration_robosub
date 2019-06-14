import time
# Import mavutil
from pymavlink import mavutil

# Create the connection
#  If using a companion computer
#  the default connection is available
#  at ip 192.168.2.1 and the port 14550
# Note: The connection is done with 'udpin' and not 'udpout'.
#  You can check in http:192.168.2.2:2770/mavproxy that the communication made for 14550
#  uses a 'udpbcast' (client) and not 'udpin' (server).
#  If you want to use QGroundControl in parallel with your python script,
#  it's possible to add a new output port in http:192.168.2.2:2770/mavproxy as a new line.
#  E.g: --out udpbcast:192.168.2.255:yourport
master = mavutil.mavlink_connection(
                    '/dev/ttyACM0',
                    baud=115200)
# Wait a heartbeat before sending commands
master.wait_heartbeat()
'''master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_DO_SET_HOME,
        1, 0, 0, 0, 0, 0, 0, 0)
'''
# Get some information !

def getDeg() :
    while True:
        try:
            att_val = master.recv_match(type='ATTITUDE').to_dict()
            roll = ((180/3.14159265358618)* att_val['yaw'])

            if roll < 0:

                return 360 + roll

            if roll > 0:

                return(roll)
            
#        print(master.recv_match(type='HOME_POSITION').to_dict())
#        dict = master.recv_match(type='RAW_IMU').to_dict()
#        print('xmag: ', dict['xmag'], 'ymag: ', dict['ymag'], 'zmag: ', dict['zmag'])
        except:
            pass
        time.sleep(0.1)

print(getDeg())
