#!/usr/bin/env python3

import serial
from geometry_msgs.msg import PoseWithCovarianceStamped
def main():
    first = PoseWithCovarianceStamped()
    second = PoseWithCovarianceStamped()
    Sub = rospy.Subscriber('/lane_detect',String,position)
    Pub = rospy.Publisher('/usb_goal',PoseWithCovarianceStamped,queue_size=10)
    ser = serial.Serial('/dev/ttyACM0',115200)
    ser.flush()
    while True:
        if ser.in_watting>0:
            line = ser.readline().decode('utf-8').rstrip()
        if(line== 1):
            first.pose.pose.position.x = a.pose.pose.position.x
            first.pose.pose.position.y = a.pose.pose.position.y
            Pub.publish(first)
        else:
            second.pose.pose.position.x = a.pose.pose.position.x
            second.pose.pose.position.y = a.pose.pose.position.y
            Pub.publish(second)
            

def position(msg):
    global a = PoseWithCovarianceStamped()
    a.pose.pose.position.x = msg.pose.pose.position.x
    a.pose.pose.position.y = msg.pose.pose.position.y
    