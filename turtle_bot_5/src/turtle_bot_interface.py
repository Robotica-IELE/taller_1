#!/usr/bin/env python3 

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist 

from time import sleep
from tkinter import Tk, Label, Button, Frame, Entry
import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from threading import Thread


fig, ax = plt.subplots(facecolor="#e5e5e5")
x = np.arange(0, 4*np.pi, 0.01)

xdata, ydata = [],[] 



class MinimalSubscriber(Node, Thread):
    def __init__(self):
        Thread.__init__(self)
        super().__init__('turtle_bot_interface')
        self.subscription = self.create_subscription(
            Twist,
            '/turtlebot_position',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        xdata.append(msg.linear.x)
        ydata.append(msg.linear.y)
        self.get_logger().info('xdata:: "%s"' % xdata)
        self.get_logger().info('ydata:: "%s"' % ydata)

    def run(self):
        rclpy.spin(self)

class VentanaTurtleBot(Thread):

    def __init__(self, root):
        # Configuración inicial root
        self.root = root
        self.root.geometry("800x800")
        self.root.title("Interfaz TurtleBot")
        self.root.minsize(width=800, height=800)
        self.root.resizable(False, False)

        # Configuración frame 
        frame_top= Frame(self.root, bg='white', bd=3)
        frame_top.pack(fill='both')
        
        frame_buttton = Frame(self.root, bg='white', bd=3)
        frame_buttton.pack(expand=1, fill='both')

        # Top   
        Label(frame_top, text="Nombre de la gráfica:",bg="white", font='Helvetica 12 bold').pack(pady=5, side='left', expand=1)
        titulo = tkinter.StringVar(self.root, value='')
        Entry(frame_top, textvariable=titulo, width=40).pack(pady=5, side='left', expand=1)
        Button(frame_top, text='Empezar', width=15, bg='white', fg='black', font='Helvetica 12 bold', command=lambda: self.init(titulo.get())).pack(pady=5, side='left', expand=1)

        # Center
        global canvas 
        canvas = FigureCanvasTkAgg(fig, master=frame_buttton)
        canvas.get_tk_widget().pack(padx=2, pady=2, expand=1, fill='both')

        # Bottom
        Button(frame_buttton, text='Detener', width=15, bg='white', fg='black', font='Helvetica 12 bold', command=self.detener).pack(pady=5, side='left', expand=1)
        Button(frame_buttton, text='Reanudar', width=15, bg='white', fg='black', font='Helvetica 12 bold', command=self.reanudar).pack(pady=5, side='left', expand=1)
        Label(frame_buttton, text="Grupo 5 - Robótica IELE 3338", bg="white", font='Helvetica 12 bold').pack(pady=5, side='left', expand=1)
        Button(frame_buttton, text='Guardar', width=15, bg='white', fg='black', font='Helvetica 12 bold', command=self.guardar).pack(pady=5, side='left', expand=1)


        self.root.mainloop()

    def animate(self, i):
        line, = ax.plot(x, np.sin(x), color='m', linewidth=3, markersize=1, markeredgecolor='m')
        line.set_data(xdata, ydata)
        return line,

    def init(self, titulo):
        print(titulo)
        global ani 
        plt.title(titulo, color='black', size=16)
        ax.set_xlim(-2.3, 2.3)
        ax.set_ylim(-2.3, 2.3)
        ani = animation.FuncAnimation(fig, self.animate, interval=20, blit=True, save_count=10)
        canvas.draw()


    def guardar(self):
        for item in canvas.get_tk_widget().find_all():
            canvas.get_tk_widget().delete(item)
        plt.plot(xdata, ydata, color='m', linewidth=3, markersize=1, markeredgecolor='m')
        plt.show()
        

    def detener(self):
        ani.event_source.stop()
        

    def reanudar(self):
        ani.event_source.start()

def main(args=None):
    rclpy.init(args=args)

    # Thread encargado de la interfaz

    # Proceso principal encargado de recibir las posiciones "(x, y)"
    minimal_subscriber= MinimalSubscriber()
    minimal_subscriber.start()

    root = Tk()
    thread_plot = VentanaTurtleBot(root)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()