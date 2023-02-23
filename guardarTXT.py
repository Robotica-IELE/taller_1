import numpy as np
# colocar fuera de la clase:
velAngular = 0
velLineal = 0

# Quitar self en caso de que se coloque la función por fuera de la clase
def converterTXT(self,archivo):
    mylines = []

    with open(archivo,'rt') as myfile:
        for i in myfile:
            i = i.rstrip() # Quitar espacio en caso de
            num = ''
            for x in i:
                if x.find(','): # COnvertir coma en stirng para ser separado en el arreglo
                    num += str(x)

                else:
                    mylines.append(int(num))
                    num = ""

    return mylines
# Quitar self en caso de que se coloque la función por fuera de la clase
def lineal_angular(self,archivo):
    alerta=1
    cont = 0
    global velAngular
    global velLineal
    with open(archivo, 'rt') as myfile:
        for y in myfile:
            if y.find(',') and alerta == 1:
                cont += 1
                if cont == 1:
                    velLineal = float(y)
                if cont == 2:
                    velAngular = float(y)
                    alerta = 0
    return velLineal,velAngular
# Ejemplo!!!

# ar = 'D:\pythonProject\Robotica\path.txt'
# alli = converterTXT(ar)
# ax = lineal_angular(ar)
