#!/usr/bin/env python3 

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist 

#librería para el cliente
import sys
from turtle_bot_5.srv import SavePath

#libreria para leeer el archivo
import numpy as np

mylines = []


class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('turtle_bot_player')
        self.publisher_ = self.create_publisher(Twist, 'turtlebot_cmdVel' ,10)    
        #self.cli = self.create_client(SavePath, 'save_path')
        #while not self.cli.wait_for_service(timeout_sec=1.0):
        #    self.get_logger().info('service not available, waiting again...')	
        #self.req = SavePath.Request()
        #self.future = self.cli.call_async(self.req)
        #rclpy.spin_until_future_complete(self, self.future)
        #response = self.future.result()
        #self.path = response.path
	#CMabiar el path
        archivo = "/home/robotica/taller1/path.txt"
        self.mylines = self.converterTXT(archivo)
        (self.linearVel,self.angularVel) = self.lineal_angular(archivo)
        timer_period = 0.5
        self.i = 0
        self.timer = self.create_timer(timer_period, self.publisher_callback)
        #self.timer = self.publisher_callback()

    def publisher_callback(self):
        msg = Twist()
        if  self.i < len(self.mylines):
            j = self.mylines[self.i]
            if j==1:
                msg.linear.x = self.linearVel
            elif j==2:
                msg.linear.x = -self.linearVel
            elif j==3:
                msg.angular.z  = -self.angularVel
            elif j==4:
                msg.angular.z = self.angularVel
            self.publisher_.publish(msg)
            self.i +=1
        else:
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.publisher_.publish(msg)


    def converterTXT(self,archivo):
        mylines = []

        with open(archivo,'rt') as myfile:
            for i in myfile:
                i = i.rstrip() # Quitar espacio en caso de
                num = ''
                for x in i:
                    if x.find(','): # COnvertir coma en stirng para ser separado en el arreglo
                        num += str(x)

                    else:   
                        mylines.append(int(num))
                        num = ""

        return mylines
# Quitar self en caso de que se coloque la función por fuera de la clase
    def lineal_angular(self,archivo):
        alerta=1
        cont = 0
        global velAngular
        global velLineal
        with open(archivo, 'rt') as myfile:
            for y in myfile:
                if y.find(',') and alerta == 1:
                    cont += 1
                    if cont == 1:
                        velLineal = float(y)
                    if cont == 2:
                        velAngular = float(y)
                        alerta = 0
        return velLineal,velAngular
            
class MinimalClientAsync(Node):
    def __init__(self):
        super().__init__('turtle_bot_player')
        self.cli = self.create_client(SavePath, 'save_path')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')	
        self.req = SavePath.Request()
	
    def send_request(self):
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()

def main(args=None):
    rclpy.init()
    
    #publicar   
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
