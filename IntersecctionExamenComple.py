import matplotlib.pyplot as plt 
import numpy as np
from math import sin, cos, radians,sqrt
import Tools 

#______Coordenadas iniciales
xg=[]
yg=[]
zg=[]

#Cordenadas centrales
xc=40
yc=40
zc=60

#Plano y linea de sistema
x=[40,30,80]
y=[0,0,0,0]
z=[60,10,60]

####_____pedir al usaurio que eje desea trabajar y plotear el PlaneLine
while True:
    xh=int(input("Dame las coordenadas de 'x' para el hitpoint: "))
    x.append(xh)
    yh=int(input("Dame las coordenadas de 'y' para el hitpoint: "))
    y.append(yh)
    zh=int(input("Dame las coordenadas de 'z' para el hitpoint: "))
    z.append(zh)
    axis=input("Teclea el eje que deseas visualizar 'x,y,z' o teclea 'Esc' para salir ?:")
    if axis=='x':#plotear el eje X
        Rx=radians(float(input('Dame los grados de rotacion ?: ')))
        plotPlaneLinex(xc,yc,zc,Rx)#LLamamos a la funcion de ploteo
    if axis=='y':
        Ry=radians(float(input('Dame los grados de rotacion ?: ')))
        plotPlaneLiney(xc,yc,zc,Ry)#LLamamos a la funcion de ploteo
    if axis=='z':
        Rz=radians(float(input('Dame los grados de rotacion ?: ')))
        plotPlaneLinez(xc,yc,zc,Rz)#LLamamos a la funcion de ploteo
    if axis== 'Esc':
        break
    
for i in range(len(x)):
    xg.append(x[i]+xc)
    yg.append(y[i]+yc)
    zg.append(z[i]+zc)

#____Plotear el sistema 
def plotPlaneLine(xg,yg,zg):
    plt.axis([-20,150,100,-100])
    plt.axis('on')
    plt.grid(False)
    plt.title("INTERSECCIÓN")
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    areas()
    #Dibujamos el triángulo base
    plt.plot([xg[0],xg[1]],[yg[0],yg[1]],color='k')#plano
    plt.plot([xg[1],xg[2]],[yg[1],yg[2]],color='k')
    plt.plot([xg[2],xg[0]],[yg[2],yg[0]],color='k')
    plt.plot([xg[2],xg[0]],[yg[2],yg[0]],color='k')
    #Dibujamos las líneas al hitpoint del triangulo 0, 1, 3
    plt.plot([xg[3],xg[0]],[yg[3],yg[0]],color='r', linestyle='--')
    plt.plot([xg[3],xg[1]],[yg[3],yg[1]],color='r', linestyle='--')
    #Dibujamos las líneas al hitpoint del triangulo 0, 2, 3
    plt.plot([xg[3],xg[2]],[yg[3],yg[2]],color='r', linestyle='--')
   
    plt.show()

def areas ():
    #Área A triángulo base, *****calculamos las tres distancias de sus lados
    # lado a (0-1)
    a1=x[1]-x[0]
    b1=y[1]-y[0]
    c1=z[1]-z[0]
    distanciaA=sqrt(a1*a1+b1*b1+c1*c1)
    # lado b (1-2)
    a2=x[2]-x[1]
    b2=y[2]-y[1]
    c2=z[2]-z[1]
    distanciaB=sqrt(a2*a2+b2*b2+c2*c2)
    # lado c (2-0)
    a3=x[2]-x[0]
    b3=y[2]-y[0]
    c3=z[2]-z[0]
    distanciaC=sqrt(a3*a3+b3*b3+c3*c3)
    #sustituimos en la fórmula de heron
    s=(distanciaA+distanciaB+distanciaC)/2
    A=sqrt(s(s-distanciaA)(s-distanciaB)(s-distanciaC))

    #Área A1 triágulo 013 
    #ya tenemos las distancia A de 0-1, calculamos las que nos faltan hacia el hitpoint
    # lado b (1-3)
    a1=x[3]-x[1]
    b1=y[3]-y[1]
    c1=z[3]-z[1]
    distanciaB1=sqrt(a1*a1+b1*b1+c1*c1)
    # lado c (3-0)
    a2=x[3]-x[0]
    b2=y[3]-y[0]
    c2=z[3]-z[0]
    distanciaC1=sqrt(a2*a2+b2*b2+c2*c2)
    #sustituimos en la fórmula de heron
    s=(distanciaA+distanciaB1+distanciaC1)/2
    A1=sqrt(s(s-distanciaA)(s-distanciaB1)(s-distanciaC1))

    #Área A2 triágulo 023 
    #ya tenemos las distancia C de 0-2, calculamos las que nos faltan hacia el hitpoint
    # lado a (0-3)
    a1=x[3]-x[0]
    b1=y[3]-y[0]
    c1=z[3]-z[0]
    distanciaA2=sqrt(a1*a1+b1*b1+c1*c1)
    # lado c (3-2)
    a2=x[3]-x[2]
    b2=y[3]-y[2]
    c2=z[3]-z[2]
    distanciaB2=sqrt(a2*a2+b2*b2+c2*c2)
    #sustituimos en la fórmula de heron
    s=(distanciaA2+distanciaB2+distanciaC)/2
    A2=sqrt(s(s-distanciaA2)(s-distanciaB2)(s-distanciaC))

    #Una vez tenemos todas las áreas, comprobamos si estan dentro o fuera del plano
    if A1+A2>A:
        print("El hitpoint esta fuera del plano")
    else:
        print("El hitpoint esta dentro del plano")

def plotPlaneLinex(xc,yc,zc,Rx):
    for i in range(0,1, 2, 3):
        [xg[i],yg[i],zg[i]]=Tools.rotRx(xc,yc,zc,x[i],y[i],z[i],Rx)
        [x[i],y[i],z[i]]=[xg[i]-xc,yg[i]-yc,zg[i]-zc]
    plotPlaneLine(xg,yg,zg)

def plotPlaneLiney(xc,yc,zc,Ry):
    for i in range(0, 1, 2, 3):
        [xg[i],yg[i],zg[i]]=Tools.rotRy(xc,yc,zc,x[i],y[i],z[i],Ry)
        [x[i],y[i],z[i]]=[xg[i]-xc,yg[i]-yc,zg[i]-zc]
    plotPlaneLine(xg,yg,zg)

def plotPlaneLinez(xc,yc,zc,Rz):
    for i in range(0, 1, 2, 3):
        [xg[i],yg[i],zg[i]]=Tools.rotRz(xc,yc,zc,x[i],y[i],z[i],Rz)
        [x[i],y[i],z[i]]=[xg[i]-xc,yg[i]-yc,zg[i]-zc]
    plotPlaneLine(xg,yg,zg)