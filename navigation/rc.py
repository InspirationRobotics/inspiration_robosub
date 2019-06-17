# Import mavutil
import time
import imu
from pymavlink import mavutil

# Create the connection

class RCLib:

    def __init__(self):
        
        self.master = mavutil.mavlink_connection(
                '/dev/ttyACM0',
                baud=115200)

        self.master.wait_heartbeat()
        
    # Create a function to send RC values
    # More information about Joystick channels
    # here: https://www.ardusub.com/operators-manual/rc-input-and-output.html#rc-inputs
    def set_rc_channel_pwm(self, id, pwm=1500):
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
            self.master.mav.rc_channels_override_send(
                self.master.target_system,                # target_system
                self.master.target_component,             # target_component
                *rc_channel_values)
    
    def pitch_raw (self, pwm=1900) :
        
        self.set_rc_channel_pwm(1, pwm)
    
    def roll_raw (self, pwm=1900) :
        
        self.set_rc_channel_pwm(2, pwm)
    
    def throttle_raw (self, pwm=1900) :
    
        self.set_rc_channel_pwm(3, pwm)
    
    def yaw_raw (self, pwm=1900) :
    
        self.set_rc_channel_pwm(4, pwm)
    
    def forward_raw (self, pwm=1900) :
    
        self.set_rc_channel_pwm(5, pwm)
    
    def lateral_raw (self, pwm=1900) :
    
        self.set_rc_channel_pwm(6, pwm)
    
    def arm (self) :
    
        self.master.arducopter_arm()
        
    
    def forward (self, value) :
        
        runtime = time.time() + value
        while runtime > time.time() :
            self.forward_raw()
            print(runtime - time.time())
    
        self.forward_raw(1500)
    
    def yaw (self, unit, value, power) :
    
        pwm = 1500 + (400 * power)
    
        if unit == "time" :
    
            runtime = time.time() + value
            while runtime > time.time() :
    
                self.yaw_raw(pwm)
    
            self.yaw_raw(1500)
    
        if unit == "imu" :

            start = imu.getDeg(self.master)
            end = start + value
            offset = 0
            flag = 0
            
            if value > 0 :

                if (end > 360) :

                    offset = 360
                    
                while imu.getDeg(self.master) + (offset * flag) < end:

                    if imu.getDeg(self.master) < (start - 5):
                        flag = 1

                    self.yaw_raw(1700)
                    print(imu.getDeg(self.master))
                    
                self.yaw_raw(1500)
    
            if value < 0 :

                if (end < 0) :

                    offset = -360

                while imu.getDeg(self.master) + (offset * flag) > end:

                    if imu.getDeg(self.master) > (start + 5):
                        flag = 1

                    self.yaw_raw(1700)
                    print(imu.getDeg(self.master))

                self.yaw_raw(1500)
                
    
    def killall (self) :
    
        self.set_rc_channel_pwm(1, 1500)
        self.set_rc_channel_pwm(2, 1500)
        self.set_rc_channel_pwm(3, 1500)
        self.set_rc_channel_pwm(4, 1500)
        self.set_rc_channel_pwm(5, 1500)
        self.set_rc_channel_pwm(6, 1500)
        
    def setmode (self, mode_val) :
    
        mode = mode_val
        mode_id = self.master.mode_mapping()[mode]
        self.master.mav.set_mode_send(
                self.master.target_system,
                mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
                mode_id)
        
