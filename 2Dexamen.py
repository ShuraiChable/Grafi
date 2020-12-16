import matplotlib.pyplot as plt
import numpy as np

plt.axis([0, 25, 0, 25])
plt.axis('off')
plt.grid(False)
    #Coordenadas del centro y grados de rotación
xc=10
yc=10
rz=36*np.pi/180
    #Lista de puntos del rectángulo
x=[-5, 5, 5, -5]
y=[3, 3, -3, -3]
    #Coordenadas globales
xg=[0, 1, 2, 3]
yg=[0, 1, 2, 3]
    #Escala RGB
r=1/10
g=6/10
b=6/10
#Dibujar rectángulo sin rotar
def drawBox(xg, yg):
    for i in(0, 1, 2):
        plt.plot([xg[i],xg[i+1]],[yg[i], yg[i+1]], linewidth=1, color=(r, g, b))
    plt.plot([xg[3],xg[0]],[yg[3], yg[0]], linewidth=1, color=(r, g, b))
#Función de rotación
def rotZ(xp, yp, rz):
    CRz11=np.cos(rz)
    CRz12=-np.sin(rz)
    CRz21=np.sin(rz)
    CRz22=np.cos(rz)
    xpp=xp*CRz11+yp*CRz12
    ypp=xp*CRz21+yp*CRz22
    [xg, yg] =[xc+xpp, yc+ypp]
    return[xg, yg]
#Rotación en Z
def plotBox(xc, yc, rz):
    for i in np.arange(0, 4):
        [xg[i], yg[i]]=rotZ(x[i], y[i], rz)   
    drawBox(xg, yg)
    #Llamamos a la función que rotará nuestro rectángulo
plotBox(xc, yc, rz)
    #Modificamos los valores de xc y yc y llamamos de nuevo a la función
xc=xg[1]
yc=yg[1]
plotBox(xc, yc, rz)
    #Radio del círculo, los mismos valores del centro
r=2.5
    #Angulo inicial y angulo final convertido en radianes
alpha1 = np.radians(0)
alpha2 = np.radians(360)
difalpha = np.radians(1)
    #Recorremos del grado 0 al 360 de 1 en 1
for alpha in np.arange(alpha1, alpha2, difalpha):
    x=xc+r*np.cos(alpha)
    y=yc+r*np.sin(alpha)
    plt.scatter(x, y, s=0.1, color='k')

plt.show()