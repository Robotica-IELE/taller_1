#!/usr/bin/env python3
import rclpy
import time
import serial
from rclpy.node import Node
from geometry_msgs.msg import Twist 

 #Modificar el puerto serie de ser necesario

# try:
#     while True:
#         comando = input("Ingresa r comando (on/off): ") #Modificar esto que es el mensaje que se envia al arduino
#         comando = comando + "\n"
#         comandoBytes = comando.encode()
#         ser.write(comandoBytes)
#         time.sleep(0.1)
#         read = ser.readline()
#         print(read)

# except KeyboardInterrupt:
#     print("\nInterrupcion por teclado")
# except ValueError as ve:
#     print(ve)
#     print("Otra interrupcion")
# finally:
#     ser.close()

# Nodo de la aplicacion.
sendVelLin = True
sendVelAng = True
ser = serial.Serial("/dev/ttyACM0", baudrate=115200)

class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('connectionSerial')
        self.subscription = self.create_subscription(
            Twist,
            '/cmdVel',
            self.listener_callback,
            8)


    def listener_callback(self, msg):
        if(sendVelLin and msg.linear.x!=0):
            comando = msg.linear.x
            comando = comando +"L"
            comandoBytes = comando.encode()
            ser.write(comandoBytes)
            sendVelLin = False    

        if(sendVelAng and msg.angular.x!=0):
            comando = msg.angular.x
            comando = comando +"A"
            comandoBytes = comando.encode()
            ser.write(comandoBytes)
            sendVelAng = False    

        comando = "0"
        if(msg.angular.z > 0.0):
            comando = "3"
        elif(msg.angular.z < 0.0):
            comando = "4"
        elif(msg.linear.x > 0.0):
            comando = "1"
        elif(msg.linear.x < 0.0):
            comando = "2"
        comando = comando + "\n"
        comandoBytes = comando.encode()
        ser.write(comandoBytes)
        self.get_logger().info(comando)
       


            
def main(args=None):
    rclpy.init(args=args)

    # Thread encargado de la interfaz.

    # Proceso principal encargado de recibir las posiciones "(x, y)"
    minimal_subscriber= MinimalSubscriber()
    rclpy.spin(minimal_subscriber)
    ser.close()
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
