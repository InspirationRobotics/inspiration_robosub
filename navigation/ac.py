from brping import Ping1D
import time
import argparse

from builtins import input

class ACLib:
    def __init__(self):
        try:
           print("ACLib constructor")
           self._pinger1 = Ping1D('/dev/ttyUSB0', 115200)
           if self._pinger1.initialize() is False:
               print("Failed to initialize Ping 1!")
               exit(1)

           time.sleep(1)
           self._pinger2 = Ping1D('/dev/ttyUSB1', 115200)
           #if self._pinger2.initialize() is False:
           #    print("Failed to initialize Ping 2!")
           #    exit(1)
           #time.sleep(1)
           self._pinger3 = Ping1D('/dev/ttyUSB2', 115200)
           if self._pinger3.initialize() is False:
               print("Failed to initialize Ping 3!")
               exit(1)
           print("ACLib constructor done")
        except Exception as e:
            print(e)
        
    def get_distance_fwd(self):
       return [self._pinger1.get_distance()["distance"], self._pinger1.get_distance()["confidence"]]
    def get_distance_left(self):
       return [self._pinger2.get_distance()["distance"], self._pinger2.get_distance()["confidence"]]
    def get_distance_right(self):
       return [self._pinger3.get_distance()["distance"], self._pinger3.get_distance()["confidence"]]
