import matplotlib.pyplot as plt 
import numpy as np
from math import sin, cos, radians,sqrt


def hitpoint(x, y):

    #Área A triángulo base, *****calculamos las tres distancias de sus lados
        # lado a (0-1)
    a1=40-30
    b1=60-10
    distanciaA=float(sqrt(a1*a1+b1*b1))
        # lado b (1-2)
    a2=80-30
    b2=60-10
    distanciaB=float(sqrt(a2*a2+b2*b2))
        # lado c (2-0)
    a3=80-40
    b3=60-60
    distanciaC=float(sqrt(a3*a3+b3*b3))
        #sustituimos en la fórmula de heron
    s=float((distanciaA+distanciaB+distanciaC)/2)
    A=int(sqrt(s*(s-distanciaA)*(s-distanciaB)*(s-distanciaC)))
        
    #Área A1 triágulo 013 
    #ya tenemos las distancia A de 0-1, calculamos las que nos faltan hacia el hitpoint
        # lado b (1-3)
    a1=x-30
    b1=y-10
    distanciaB1=float(sqrt(a1*a1+b1*b1))
        # lado c (3-0)
    a2=x-40
    b2=y-60
    distanciaC1=float(sqrt(a2*a2+b2*b2))
        #sustituimos en la fórmula de heron
    s=float((distanciaA+distanciaB1+distanciaC1)/2)
    A1=int(sqrt(s*(s-distanciaA)*(s-distanciaB1)*(s-distanciaC1)))
    
    #Área A2 triágulo 023 
    #ya tenemos las distancia C de 0-2 y 3-0, calculamos las que nos faltan hacia el hitpoint
        # lado c (3-2)
    a2=x-80
    b2=y-60
    distanciaB2=float(sqrt(a2*a2+b2*b2))
        #sustituimos en la fórmula de heron
    s=float((distanciaC1+distanciaB2+distanciaC)/2)
    A2=int(sqrt(s*(s-distanciaC1)*(s-distanciaB2)*(s-distanciaC)))

    #Una vez tenemos todas las áreas, comprobamos si estan dentro o fuera del plano
    if (A1+A2)>A:
        plt.text(0, 120, "El hitpoint esta fuera del plano")
    else:
        plt.text(0, 120, "El hitpoint esta dentro del plano")
        
 


def plotPlane(x, y):
    plt.axis([-10,150,-10,150])
    plt.axis('on')
    plt.grid(False)
    plt.title("INTERSECCIÓN")
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    
    hitpoint(x, y)
    #Dibujamos el triángulo base
    plt.plot([40,30] ,[60, 10],color='k')#plano
    plt.text(35, 60, '0')
    plt.plot([30,80] ,[10, 60],color='k')
    plt.text(30, 6, '1')
    plt.plot([80,40] ,[60, 60],color='k')
    plt.text(81, 60, '2')
    plt.text(45, 70, 'A (0, 1, 2)')
    plt.text(x+2, y+2, '3')

    plt.text(120, 140,'A1 (0, 1, 3)')
    plt.text(120, 130, 'A2 (0, 2, 3)')
 
    #Dibujamos las líneas al hitpoint del triangulo 0, 1, 3
        #Ya tenemos las lineas del 0-1, asi que dibujamos del 0-3 y 1-3
    plt.plot([40,x] ,[60, y],color='r', linestyle='--', linewidth=1) #0-3
    plt.plot([30,x] ,[10, y],color='r', linestyle='--', linewidth=1) #1-3
    #Dibujamos las líneas al hitpoint del triangulo 0, 2, 3
        #Ya tenemos las lineas del 0-2, tambien 0-3, solo nos falta del 2-3
    plt.plot([80,x] ,[60, y],color='r', linestyle='--', linewidth=1) #1-3
   
    plt.show()

while True:

    xh=float(input("Dame las coordenadas de 'x' para el hitpoint: ")) 
    yh=float(input("Dame las coordenadas de 'y' para el hitpoint: "))
    plotPlane(xh, yh)
    axis=input("Teclea'Esc' para salir ?:")
    if axis== 'Esc':
        break

