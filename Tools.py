import numpy as np
from math import sin, cos, radians

# Rotación en X
def rotRx(xc, yc, zc, xp, yp, zp, Rx):
    a=[xp, yp, zp] 
    b=[1, 0, 0]
    xpp=np.inner(a, b)
    b=[0, cos(Rx), -sin(Rx)]
    ypp=np.inner(a, b)
    b=[0, sin(Rx), cos(Rx)]
    zpp=np.inner(a, b)
    [xg, yg, zg]=[xpp+xc, ypp+yc, zpp+zc]
    return[xg, yg, zg]

def rotRy(xc, yc, zc, xp, yp, zp, Ry):
    a=[xp, yp, zp]
    b=[cos(Ry), 0, sin(Ry)]
    xpp=np.inner(a, b)
    b=[0, 1, 0]
    ypp=np.inner(a, b)
    b=[-sin(Ry), 0, cos(Ry)]
    zpp=np.inner(a, b)
    [xg, yg, zg]=[xpp+xc, ypp+yc, zpp+zc]
    return[xg, yg, zg]

def rotRz(xc, yc, zc, xp, yp, zp, Rz):
    a=[xp, yp, zp]
    b=[cos(Rz), -sin(Rz), 0]
    xpp=np.inner(a, b)
    b=[sin(Rz), cos(Rz), 0]
    ypp=np.inner(a, b)
    b=[0, 0, 1]
    zpp=np.inner(a, b)
    [xg, yg, zg]=[xpp+xc, ypp+yc, zpp+zc]
    return[xg, yg, zg]

def coordenadas(r, phi1, phi2, dphi):
    x=[]
    y=[]
    z=[]
    xg=[]
    yg=[]
    zg=[]
    for phi in np.arange(phi1, phi2+dphi, dphi):
        xp=r*cos(phi)
        yp=r*sin(phi)
        zp=0

        x.append(xp)
        y.append(yp)
        z.append(zp)
        xg.append(xp)
        yg.append(yp)
        zg.append(zp)
    return(x, y, z, xg, yg, zg)
