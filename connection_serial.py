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
ser = serial.Serial("/dev/ttyACM0", baudrate=115200)

class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('connectionSerial')
        self.subscription = self.create_subscription(
            Twist,
            '/cmdVel',
            self.listener_callback,
            10)


    def listener_callback(self, msg):
        comando = "0"
        if(ms.angular.z == 1.0):
            comando = "4"
        elif(ms.angula.z == -1.0):
            comado = "3"
        elif(ms.linear.x == 1.0):
            comando = "1"
        elif(ms.linear.x == -1.0):
            comando = "2"
        comando = comando + "\n"
        comandoBytes = comando.encode()
        ser.write(comandoBytes)
        time.sleep(0.2)
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
