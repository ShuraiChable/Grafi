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
x=[40,30,80,-40,-20]
y=[0,0,0,0,-20,-10]
z=[60,10,60,15,0]

for i in range(len(x)):
    xg.append(x[i]+xc)
    yg.append(y[i]+yc)
    zg.append(z[i]+zc)

#____Plotear el sistema 
#def plotPlaneLine(xg,yg,zg,xh,yh,xhg,yhg,hitcolor):
def plotPlaneLine(xg,yg,zg,xh,yh,xhg,yhg,hitcolor):
    plt.axis([-20,150,100,-100])
    plt.axis('on')
    plt.grid(False)
    plt.plot([xg[0],xg[1]],[yg[0],yg[1]],color='k')#plano
    plt.plot([xg[1],xg[2]],[yg[1],yg[2]],color='k')
    plt.plot([xg[2],xg[0]],[yg[2],yg[0]],color='k')
    plt.plot([xg[3],xg[4]],[yg[3],yg[4]],color='b')#Line

    if hitcolor=='g':# Do not touch hit point
        plt.scatter(xg[5],yg[5],s=20,color=hitcolor)
    else:
        plt.scatter(xhg,yhg,s=20,color=hitcolor)

    plt.show()

def hitpoint(x,y,z):
    #_____distance point 3 to 4
    a=x[4]-x[3]
    b=y[4]-y[3]
    c=z[4]-z[3]
    Q45=sqrt(a*a+b*b+c*c) 
    # unit vector components point 3 to 2
    lx=a/Q45 
    ly=b/Q45
    lz=c/Q45
    #_____distance point 0 to 2
    a=x[2]-x[0]
    b=y[2]-y[0]
    c=z[2]-z[0]
    Q03=sqrt(a*a+b*b+c*c) 
    # unit vector components point 0 to 2
    ux=a/Q03 #———unit vector 0 to 2
    uy=b/Q03
    uz=c/Q03
    #_____distance point 0 to 1
    a=x[1]-x[0]
    b=y[1]-y[0]
    c=z[1]-z[0]
    Q01=sqrt(a*a+b*b+c*c)
    # unit vector components point 0 to 1
    vx=a/Q01 #———unit vector 0 to 1
    vy=b/Q01
    vz=c/Q01
    #_____normal vector unit
    nx=uy*vz-uz*vy 
    ny=uz*vx-ux*vz
    nz=ux*vy-uy*vx
    #___________vector components 0 t0 3
    vx1b=x[3]-x[0]
    vy1b=y[3]-y[0]
    vz1b=z[3]-z[0]
    #____perpenticular distance 3 to plane
    Qn=(vx1b*nx+vy1b*ny+vz1b*nz)

    #_____cos of angle p
    cosp=lx*nx+ly*ny+lz*nz

    #___distance 4 to hit point
    Qh=abs(Qn/cosp)

    #____Hit point coordinates
    xh=x[3]+Qh*lx
    yh=y[3]+Qh*ly
    zh=z[3]+Qh*lz

    #_____global hit point coodinates
    xhg=xh+xc
    yhg=yh+yc
   
    #________checar si la linea de 3 A 4 queda fuera de los valores del rectangulo
    #____Component of vector V0h
    a=xh-x[0]
    b=yh-y[0]
    c=zh-z[0]
    #dot products
    up=a*ux+b*uy+c*uz
    vp=a*vx+b*vy+c*vz
    #Si no estamos saliendo del plano del objeto rectangulo 
    hitcolor='r'
    if up<0:
        hitcolor='b'
    if up>Q03:
        hitcolor='b'
    if vp<0:
        hitcolor='b'
    if vp>Q01:
        hitcolor='b'
    
    #_____Si el punto de 3 a 4 no alcanza el hit point
    a=x[4]-x[3]
    b=y[4]-y[3]
    c=z[4]-z[3]
    Q45=sqrt(a*a+b*b+c*c)
    if Q45 < Qh:
        hitcolor='g'
    return xh,yh,xhg,yhg,hitcolor 

def plotPlaneLinex(xc,yc,zc,Rx):
    for i in range(0, 4):
        [xg[i],yg[i],zg[i]]=Tools.rotRx(xc,yc,zc,x[i],y[i],z[i],Rx)
        [x[i],y[i],z[i]]=[xg[i]-xc,yg[i]-yc,zg[i]-zc]
    xh,yh,xhg,yhg,hitcolor=hitpoint(x,y,z)
    plotPlaneLine(xg,yg,zg,xh,yh,xhg,yhg,hitcolor)

def plotPlaneLiney(xc,yc,zc,Ry):
    for i in range(0, 4):
        [xg[i],yg[i],zg[i]]=Tools.rotRy(xc,yc,zc,x[i],y[i],z[i],Ry)
        [x[i],y[i],z[i]]=[xg[i]-xc,yg[i]-yc,zg[i]-zc]
    xh,yh,xhg,yhg,hitcolor=hitpoint(x,y,z)
    plotPlaneLine(xg,yg,zg,xh,yh,xhg,yhg,hitcolor)

def plotPlaneLinez(xc,yc,zc,Rz):
    for i in range(0, 4):
        [xg[i],yg[i],zg[i]]=Tools.rotRz(xc,yc,zc,x[i],y[i],z[i],Rz)
        [x[i],y[i],z[i]]=[xg[i]-xc,yg[i]-yc,zg[i]-zc]
    xh,yh,xhg,yhg,hitcolor=hitpoint(x,y,z)
    plotPlaneLine(xg,yg,zg,xh,yh,xhg,yhg,hitcolor)

####_____pedir al usaurio que eje desea trabajar y plotear el PlaneLine
while True:
    axis=input("Teclea el eje que deseas visualizar 'x,y,z' o pulsa w para salir ?:")
    if axis=='x':#plotear el eje X
        Rx=radians(float(input('Dame los grados de rotacion ?: ')))
        plotPlaneLinex(xc,yc,zc,Rx)#LLamamos a la funcion de ploteo
    if axis=='y':
        Ry=radians(float(input('Dame los grados de rotacion ?: ')))
        plotPlaneLiney(xc,yc,zc,Ry)#LLamamos a la funcion de ploteo
    if axis=='z':
        Rz=radians(float(input('Dame los grados de rotacion ?: ')))
        plotPlaneLinez(xc,yc,zc,Rz)#LLamamos a la funcion de ploteo
    if axis== 'w':
        break


