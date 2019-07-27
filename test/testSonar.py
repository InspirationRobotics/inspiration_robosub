from navigation.ac import ACLib
import time


ac = ACLib()

i=0
#while i < 10:
while (1):
    #print 'left' , ac.get_distance_left()[0], ac.get_distance_left()[1]
    print 'right' , ac.get_distance_right()[0], ac.get_distance_right()[1]
    #print 'fwd' , ac.get_distance_fwd()[0], ac.get_distance_fwd()[1]
    print '--'


