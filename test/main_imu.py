
import navigation.rc as rc
import time

# pwm value to move in the opposite direction; do not enter any value into the movement functions for a positive motion
reverse = 1100
stop = 1500

# arm the vehicle
rc.arm()

# move downwards, use reverse value

rc.forward(10)
