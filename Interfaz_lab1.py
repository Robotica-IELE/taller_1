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
        axis = fig.add_subplot(111)
        axis.set_title('Título')
        t = np.arange(0, 1, .01)
        axis.plot(t, t**2)  # AÑADIR "subbplot"

        axis.set_ylabel('Y (cm)')
        axis.set_xlabel('X (cm)')

        canvas = FigureCanvasTkAgg(fig, master=root)  # CREAR AREA DE DIBUJO DE TKINTER.
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        print("Entro para accionar")
root = Tk()
miVentana = VentanaTurtleBot(root)
root.mainloop()