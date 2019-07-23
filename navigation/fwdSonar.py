import numpy as np
import time
import ac
import log

import threading

class FwdSonarThread (threading.Thread):
 def __init__(self , acLib, logger=None):
   threading.Thread.__init__(self)
   self._active = 1
   self._ac = acLib
   if logger == None:
      logger = log.LogLib()

   self._log = logger
   self._lastDist = 0
   self._lastConf = 0

 def stop(self) :
   self._active = 0

 def dist(self) :
    return self._lastDist, self._lastConf 

 def run(self):
    while(self._active == 1):
        time.sleep(0.01)
        self._lastDist = self._ac.get_distance_fwd()[0]
        self._lastConf = self._ac.get_distance_fwd()[1]
        self._log.info("Fwd Dist %d " % self._lastDist)
        self._log.info("Fwd Conf %d" % self._lastConf)
            

