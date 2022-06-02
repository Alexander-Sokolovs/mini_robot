#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import rospy

class hello_class:
    def __init__(self):
        print("yeah")

if __name__ == '__main__':
    rospy.init_node("hello_node")

    hc = hello_class()
    print("Hello world!")