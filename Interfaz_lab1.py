from tkinter import Tk, Label, Button
import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

class VentanaTurtleBot:
    def __init__(self, master):
        self.master = master
        master.geometry("600x600")
        master.title("Interzas TurtleBot")

        self.name = Label(master, text="Nombre de la gráfica:").place(x=30, y=6)
        self.e1 = tkinter.Entry(master).place(x=80, y=6)
        #-------------
        self.botonNombreGrafica = Button(master, text="Seleccione título", bg='#ffb3fe', command=self.seleccione)
        self.botonNombreGrafica.pack()
        ##
        self.botonGuardar = Button(master, text="Guardar", bg='#99FF99', command=self.guardar)
        self.botonGuardar.pack()
    def guardar(self):
        print("Entra para guardar archivo")
    def seleccione(self):
        fig = Figure(figsize=(5, 4), dpi=100)


        fig.add_subplot(111).set_title('Título')
        fig.add_subplot(111).set_ylabel('Y (cm)')
        fig.add_subplot(111).set_xlabel('X (cm)')
        t = np.arange(0, 1, .01)
        fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))  # AÑADIR "subbplot"

        canvas = FigureCanvasTkAgg(fig, master=root)  # CREAR AREA DE DIBUJO DE TKINTER.
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        print("Entro para accionar")
root = Tk()
miVentana = VentanaTurtleBot(root)
root.mainloop()