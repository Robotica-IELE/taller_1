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

class VentanaTurtleBot(Thread):

    def __init__(self, root):
        Thread.__init__(self)

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
        Button(frame_buttton, text='Detener', width=15, bg='white', fg='black', font='Helvetica 12 bold', command=self.b).pack(pady=5, side='left', expand=1)
        Label(frame_buttton, text="Grupo 5 - Robótica IELE 3338", bg="white", font='Helvetica 12 bold').pack(pady=5, side='left', expand=1)
        Button(frame_buttton, text='Guardar', width=15, bg='white', fg='black', font='Helvetica 12 bold', command=self.c).pack(pady=5, side='left', expand=1)


        self.root.mainloop()

    def animate(self, i):
        line, = ax.plot(x, np.sin(x), color='m', marker='o', linestyle='dotted', linewidth=5, markersize=1, markeredgecolor='m')
        line.set_ydata(np.sin(x+i/40))
        return line,

    def init(self, titulo):
        print(titulo)
        global ani 
        plt.title(titulo, color='black', size=16)
        ani = animation.FuncAnimation(fig, self.animate, interval=20, blit=True, save_count=10)
        canvas.draw()


    def b(self):
        print("bbbbbbbbbbbbb")

    def c(self):
        print("ccccccccccccc")

    def run(self):
        while True:
            sleep(1)
            print("xd")

def main(args=None):
    rclpy.init(args=args)

    # Thread encargado de la interfaz
    root = Tk()
    thread_plot = VentanaTurtleBot(root)
    thread_plot.start()

    # Proceso principal encargado de recibir las posiciones "(x, y)"
    minimal_subscriber= MinimalSubscriber()
    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()