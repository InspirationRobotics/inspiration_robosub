# Import mavutil
import time
import imu

from pymavlink import mavutil

# Create the connection
master = mavutil.mavlink_connection(
                '/dev/ttyACM0',
                baud=115200)
# Wait a heartbeat before sending commands
master.wait_heartbeat()

# Create a function to send RC values
# More information about Joystick channels
# here: https://www.ardusub.com/operators-manual/rc-input-and-output.html#rc-inputs
def set_rc_channel_pwm(id, pwm=1500):
    """ Set RC channel pwm value
    Args:
        id (TYPE): Channel ID
        pwm (int, optional): Channel pwm value 1100-1900
    """
    if id < 1:
        print("Channel does not exist.")
        return

    # We only have 8 channels
    #http://mavlink.org/messages/common#RC_CHANNELS_OVERRIDE
    if id < 9:
        
        rc_channel_values = [65535 for _ in range(8)]
        rc_channel_values[id - 1] = pwm
        master.mav.rc_channels_override_send(
            master.target_system,                # target_system
            master.target_component,             # target_component
            *rc_channel_values)                  # RC channel list, in microseconds.

def pitch_raw (pwm=1900) :
    
    set_rc_channel_pwm(1, pwm)

def roll_raw (pwm=1900) :

    set_rc_channel_pwm(2, pwm)

def throttle_raw (pwm=1900) :

    set_rc_channel_pwm(3, pwm)

def yaw_raw (pwm=1900) :

    set_rc_channel_pwm(4, pwm)

def forward_raw (pwm=1900) :

    set_rc_channel_pwm(5, pwm)

def lateral_raw (pwm=1900) :

    set_rc_channel_pwm(6, pwm)

def arm () :

    master.arducopter_arm()
    

def forward (value) :
    
    runtime = time.time() + value
    while runtime > time.time() :
        forward_raw()
        print(runtime - time.time())

    forward_raw(1500)

def yaw (unit, value, power) :

    pwm = 1500 + (400 * power)

    if unit == "time" :

        runtime = time.time() + value
        while runtime > time.time() :

            yaw_raw(pwm)

        forward_raw(1500)

    if unit == "imu" :

        start = imu.getDeg()
        end = start + value

        if value > 0 :

            while imu.getDeg() < end:

                yaw_raw(1700)

            yaw_raw(1500)

        if value < 0 :

            while imu.getDeg() > end:

                yaw_raw(1300)

            yaw_raw(1500)

def killall () :

    set_rc_channel_pwm(1, 1500)
    set_rc_channel_pwm(2, 1500)
    set_rc_channel_pwm(3, 1500)
    set_rc_channel_pwm(4, 1500)
    set_rc_channel_pwm(5, 1500)
    set_rc_channel_pwm(6, 1500)
    
def setmode (mode_val) :

    mode = mode_val
    mode_id = master.mode_mapping()[mode]
    master.mav.set_mode_send(
            master.target_system,
            mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
            mode_id)
    
#print master.mode_mapping()
