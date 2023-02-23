import numpy as np

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
# Ejemplo!!!

# ar = 'D:\pythonProject\Robotica\path.txt'
# alli = converterTXT(ar)
# print(len(alli))
