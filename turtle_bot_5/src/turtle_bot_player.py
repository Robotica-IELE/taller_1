#!/usr/bin/env python3 

import sys
from turtle_bot_5.srv import DoPath
from turtle_bot_5.msg import Float32MultiArray
import rclpy
from geometry_msgs.msg import Twist 
from rclpy.node import Node

class MinimalService(Node):
    def __init__(self):
        super().__init__('turtle_bot_player')
        self.subscription = self.create_subscription(
            Twist,
            '/turtlebot_cmdVel',
            self.listener_callback,
            1)

    def listener_callback(self, msg):
        print("xd")

def main(args=None):
    rclpy.init(args=args)
    minimal_service = MinimalService()
    rclpy.spin(minimal_service)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
