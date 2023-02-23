#!/usr/bin/env python3 

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

#librería para el cliente
import sys
from turtle_bot_5.srv import SavePath

#libreria para leeer el archivo
import numpy as np

mylines = []
linearVel = 0
angularVel = 0

class MinimalPublisher(Node):
    def __init__(self):
    	super().__init__('turtle_bot_player')
    	self.publisher_ = self.create_publisher(Twist, 'turtlebot_cmdVel', self.publisher_callback,10)  	

    def publisher_callback(self):
        msg = Twist()
	for i in mylines:
            if i==1:
                msg.linear.x = linearVel
            elif i==2:
                msg.linear.x = -linearVel
            elif i==3:
                msg.angular.z  = -angularVel
            elif i==4:
                msg.angular.z = angularVel
            self.publisher_.publish(msg)
            
class MinimalClientAsync():
    self.cli = self.create_client(SavePath, 'save_path')
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
    
    # Ruta
    minimal_client = MinimalClientAsync()
    response = minimal_client.send_request()
    minimal_client.get_logger().info('Path: %d' %(response.path))
    archivo = response.path
    minimal_client.destroy_node()
    

    #Leer archivo 
    alerta=1
    cont = 0
       
    with open(archivo,'rt') as myfile:
        for y in myfile:
            if y.find(',') and alerta == 1:
                cont += 1
                if cont == 1:
                    linearVel = float(y)
                if cont == 2:
                    angularVel = float(y)
                    alerta = 0
        for i in myfile:
            i = i.rstrip() # Quitar espacio en caso de
            num = ''
            for x in i:
                if x.find(','): # COnvertir coma en stirng para ser separado en el arreglo
                    num += str(x)

                else:
                    mylines.append(int(num))
                    num = ""
    
    #publicar   
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
