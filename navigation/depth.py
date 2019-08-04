import numpy as np
import time
import threading

class DepthThread (threading.Thread):
 def __init__(self, master):
   threading.Thread.__init__(self)
   self.master = master
   self._active = 1
   self._depth = None
   self._pause = 1
   self.lock = threading.Lock()
   
 def stop (self) :
   self._active = 0

 def pause (self) :
    self._pause = 1

 def resume (self) :
    self._pause = 0
 def getDepth(self) :
     return self._depth
 def run(self):
    while(self._active == 1):
        try:

            if self._pause == 1 :
                time.sleep(0.1)
                continue
               
            ret = self.master.recv_match(type='ATTITUDE')
            if (ret != None) :
                depth_val = ret.to_dict()
                with self.lock :
                    self._depth = depth_val['alt']
                    print(self._depth)
                time.sleep(0.01)
             
        except Exception as e :
            print(e)
            pass
