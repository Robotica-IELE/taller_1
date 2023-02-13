from tkinter import Tk, Label, Button
import tkinter
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np


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


root = Tk()
miVentana = VentanaTurtleBot(root)
root.mainloop()
