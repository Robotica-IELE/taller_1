#!/usr/bin/env python3 

# Librerias generales
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist 
import sys
import time
import math 

# Servicio
from turtle_bot_5.srv import DoPath

# Indica si los datos ya fueron cargados
data_loaded = False
temp_line_x = 0
temp_line_y = 0
temp_ang = 0
t = 0.01 #en s debe ser igual a la del arduino

class MinimalService(Node):
    def __init__(self):
        super().__init__('turtle_bot_player')
        self.publisher = self.create_publisher(Twist, '/turtlebot_position', 1) 
        self.subscription = self.create_subscription(
            Twist,
            '/cmdVel',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        global temp_line_x 
        global temp_line_y
        global temp_ang
        data = Twist()
        temp_ang = temp_ang+msg.angular.z*t
        temp_line_x = temp_line_x + msg.linear.x*t*math.cos(temp_ang)
        temp_line_y = temp_line_y + msg.linear.x*t*math.sin(temp_ang)
        data.linear.x = temp_line_x
        data.linear.y = temp_line_y
        
        
        self.get_logger().info('xpos:: "%s"' % msg.linear.x)
        self.get_logger().info('ypos:: "%s"' % msg.angular.z)
        self.publisher.publish(data)

def main(args=None):
    rclpy.init(args=args)
    minimal_service = MinimalService()
    rclpy.spin(minimal_service)
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()
