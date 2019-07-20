# Import mavutil
from pymavlink import mavutil
import time

# Create the connection
master = mavutil.mavlink_connection('/dev/ttyACM0',
                baud=115200)
# Wait a heartbeat before sending commands
master.wait_heartbeat()

# Request all parameters
master.mav.param_request_list_send(
    master.target_system, master.target_component
)
while True:
    time.sleep(0.01)
    print("while")
    try:
	print(master.recv_match().to_dict())
    except Exception as e:
        print(e)
        exit(0)
