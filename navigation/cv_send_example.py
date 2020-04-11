import nav_interface
import logging

nav_i  = nav_interface.Nav_send_intf("192.168.1.22", 5005, 'cv_nav_log', logging.INFO)


nav_i.send_cv_data(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
