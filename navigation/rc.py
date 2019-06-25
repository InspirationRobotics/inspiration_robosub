# Import mavutil
import time
import imu
from pymavlink import mavutil

# Create the connection

class RCLib:

    def __init__(self):
        try: 
            self.master = mavutil.mavlink_connection(
                '/dev/ttyACM0',
                baud=115200)

            self.master.wait_heartbeat()
        except:
            print('Exception in connect')
        
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
        
    def throttle (self, unit, value, power) :
	
	pwm = 1500 + (400 * power)
	
	if unit == "time" :

	    runtime = time.time() + value
	    while runtime > time.time() :
	        self.throttle_raw(pwm)
            self.throttle_raw(1500)

    def forwardAngle (self, unit, value, power, angle) :
        
	if unit == "time" :
            
	    self.setmode('ALT_HOLD')
	    pwm = 1500 + (400 * power)
	    runtime = time.time() + value
            while runtime > time.time() :
                self.forward_raw(pwm)
                print(runtime - time.time())
    
            self.forward_raw(1500)
    	    self.setmode('MANUAL')
 
		
    def forward (self, unit, value, power) :
        
	if unit == "time" :
            
	    self.setmode('ALT_HOLD')
	    pwm = 1500 + (400 * power)
	    runtime = time.time() + value
            while runtime > time.time() :
                self.forward_raw(pwm)
                print(runtime - time.time())

            self.forward_raw(1500)
    	    self.setmode('MANUAL')
    
    def deg (self) :

        print(imu.getDeg(self.master)) 

    def yaw (self, unit, value, power) :

        power = power * (value/abs(value))
    
        pwm = 1500 + (400 * power)
    
        if unit == "time" :
   
            runtime = time.time() + value
            while runtime > time.time() :
    
                self.yaw_raw(pwm)
    
            self.yaw_raw(1500)
    
        if unit == "imu" :

            start = imu.getDeg(self.master)
            print('start angle: %s' % start)

            end = start + value
            offset = 0
            flag = 0
            
            if value > 0 :

                if (end > 360) :

                    offset = 360
                    
                self.yaw_raw(pwm)
                while imu.getDeg(self.master) + (offset * flag) < end:
                    #print('Loop 1')
                    pwm = 1500 + (end - (imu.getDeg(self.master) + (offset * flag)))*0.5 + 100
                    print ('pwm = %d') % pwm

                    if imu.getDeg(self.master) < (start - 10):
                        flag = 1

                    self.yaw_raw(pwm)
                    #print(imu.getDeg(self.master))
                    #print(time.time())
                self.yaw_raw(1500)
    
            if value < 0 :

                if (end < 0) :

                    offset = -360

                self.yaw_raw(pwm)
                while imu.getDeg(self.master) + (offset * flag) > end:

                    pwm = 1500 - ((imu.getDeg(self.master) + (offset * flag)) - end)*0.5 - 100

                    if imu.getDeg(self.master) > (start + 10):
                        flag = 1

                    self.yaw_raw(pwm)
                    #print(imu.getDeg(self.master))

                self.yaw_raw(1500)

            #print('before delay')
	    #print(imu.getDeg(self.master))
            #r = time.time() + 20
	    #while (r > time.time()):
		#print(imu.getDeg(self.master)) 

            #time.sleep(10) 
	    #print('after delay')
	    #print(imu.getDeg(self.master))
            
            print('Expected End angle: %s' % end)
            print('Actual End angle: %s' % imu.getDeg(self.master))

        def getDeg (self) :
                r = imu.getDeg(self.master)
                print(r)
                return imu.getDeg(self.master) 
                  
    def lateral (self, unit, value, power) :

        if unit == "time" :

            self.setmode('ALT_HOLD')
            pwm = 1500 + (400 * power)
            runtime = time.time() + value
            while runtime > time.time() :
                self.lateral_raw(pwm)
                print(runtime - time.time())

            self.lateral_raw(1500)
            self.setmode('MANUAL')
    
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
        
