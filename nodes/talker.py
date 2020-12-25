#!/usr/bin/env python
import roslib; roslib.load_manifest('beginner_tutorials')  
import rospy
import time 
from std_msgs.msg import String
def talker(): 
    pub = rospy.Publisher('chatter', String) 
    rospy.init_node('talker') 
    while not rospy.is_shutdown():
        time_local  = time.localtime()
        time_format = time.strftime("%H:%M:%S", time_local)

        str = "\nSvechnikov N.S. %s\nAlexeev A.I. %s\nBykov E.A. %s" %(time_format, time_format, time_format)
        rospy.loginfo(str) 
        pub.publish(String(str)) 
        rospy.sleep(1.0)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
