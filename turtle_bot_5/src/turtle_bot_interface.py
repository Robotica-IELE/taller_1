#!/usr/bin/env python3 

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist 

from tkinter import Tk, Label, Button
import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
from pandas import pandass
from threading import Thread

class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('turtle_bot_interface')
        self.subscription = self.create_subscription(
            Twist,
            '/turtle1/cmd_vel',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg)

class VentanaTurtleBot:
    def __init__(self, master):
        self.master = master
        master.geometry("800x500")
        master.configure(bg="#1AA7EC")
        master.title("Interzas TurtleBot")

        titulo = tkinter.StringVar()  # Atributo titulo para usar en gráfica

        self.name = Label(master, text="Nombre de la gráfica:",background="#1AA7EC").grid(row=2, column=0)
        self.e1 = tkinter.Entry(master, textvariable=titulo).grid(row=2, column=1)

        # -------------
        self.botonNombreGrafica = Button(master, text="Seleccione título", bg='#ffb3fe',
                                         command=lambda: self.seleccione(titulo))
        self.botonNombreGrafica.grid(row=2, column=2)
        ##
        self.botonGuardar = Button(master, text="Guardar", bg='#99FF99', command=self.guardar)
        self.botonGuardar.grid(row=2, column=5)

    def guardar(self):
        direccion = filedialog.askopenfilename()
        print("Entra para guardar archivo")

    def seleccione(self, til):
        fig = Figure(figsize=(5, 4), dpi=100)
        axis = fig.add_subplot(111)
        axis.set_title(til.get())
        lista = np.random.randint(0,10,size=20)
        t = np.arange(0, 10, .5)
        axis.plot(t,lista)  # AÑADIR "subplot"

        axis.set_ylabel('Y (m)')
        axis.set_xlabel('X (m)')

        canvas = FigureCanvasTkAgg(fig, master=root)  # CREAR AREA DE DIBUJO DE TKINTER.
        canvas.draw()
        canvas.get_tk_widget().grid(row=3, column=1)
        print("Entro para accionar")

def main(args=None):
    rclpy.init(args=args)

    
    root = Tk()
    miVentana = VentanaTurtleBot(root)
    root.mainloop()

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()