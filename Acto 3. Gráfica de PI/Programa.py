#Equipo 3 ; LMV N3
#Comienzo del programa
#Librerias
from cmath import pi
from multiprocessing import pool
from multiprocessing.dummy import Pool
from random import randint
from turtle import width
from unicodedata import name
from matplotlib import pyplot as plt
import statistics
#Dimensiones
width = 1000
height = width
radio = width
#Calculos
npuntos = 0
ndentro = 0 
radio2 = radio*radio
replicas = 1000
promediopi = []
if _name_ == '_main_':
    with Pool(6) as p:
        for j in range (1,10000):
            x = randint (0,width)
            y = randint (0,width)
            npuntos += 1
            if x*x + y*y <= radio2:
                ndentro += 1
                pi = ndentro * 4 / npuntos
                promediopi.append(pi)
#Grafica
v = [0,1000,3,3.5]
plt.plot(promediopi,"b--")
plt.xlabel('Cantidad de replcias')
plt.ylabel('Valores de Pi')
plt.title('Grafica por Monte Carlo')
plt.axis(v)
plt.grid()
plt.show()
