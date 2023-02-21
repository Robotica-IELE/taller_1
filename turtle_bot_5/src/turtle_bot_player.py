import sys
from turtle_bot_5.srv import DoPath
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

running = True
arreglo = []

class MinimalClientAsync:
    def __init__(self):
        super().__init__('turtle_bot_player')
        self.srv = self.create_service(DoPath, 'do_path', self.do_path_callback)
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = DoPath.Request()
        self.subscription = self.create_subscription(
                Twist
                '/turtlebot_cmdVel',
                self.listener_callback,
                10)

    def listener_callback(self):
        msg = Twist()
        for i in arreglo :
            if i==1:
                msg.linear = 10
            elif i==2:
                msg.linear = -10
            elif i==3:
                msg.angular  = -10
            elif i==4:
                msg.angular = 10
            
            publish(msg)
                  

    def do_path_callback(self, request, response):
        #"r" para leer el archivo
        with open(request.name,'r') as file:
            arreglo = file.read()
        for i in arreglo:
            i = i.rstrip()
            num = ''
            for x in i:
                if x.find(','):
                    num += str(x)
                else:
                    movements.append(int(num))
                    num = ""

    def movement():
        

def main():
    rclpy.init()
    minimal_client = MinimalClientAsync()
    response = minimal_client.converterArchivo()
    minimal_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()