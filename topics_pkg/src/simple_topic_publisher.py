#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
import csv

def talker():
    rospy.init_node('topic_publisher', anonymous=True)
    pub = rospy.Publisher('/counter', Int32, queue_size=1)
    rate = rospy.Rate(2) 
    count = Int32()
    count.data = 0
    
    with open('counter_log.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        writer.writerow(["Timestamp", "Value"])
        csvfile.flush()
        rospy.loginfo("Nodul a pornit. Se scrie în counter_log.csv...")

        while not rospy.is_shutdown():
    
            pub.publish(count) 
            writer.writerow([count.data])
            rospy.loginfo(f"Publicat și salvat: {count.data}")           
            count.data += 1           
            rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass