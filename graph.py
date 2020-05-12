# -*- coding: utf-8 -*-
import pylab
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
pylab.minorticks_on()
pylab.grid(color="black", which="major", linewidth=1)
pylab.grid(color="black", which="minor", linestyle=":", linewidth=0.5)
data=np.loadtxt ("points.txt")
plt.plot(data[:,0], data[:,3],'ro',color='red')
plt.plot(data[:,0], data[:,4],'ro',color= 'blue')
plt.plot(data[:,3], data[:,4],'ro',color= 'green')
plt.plot(data[:,0], data[:,1],color='yellow')
plt.plot(data[:,0], data[:,2],color= 'yellow')
plt.plot(data[:,1], data[:,2],color= 'yellow')
plt.title("Zadacha Koshi, red- precise y(x), blue- precise y'(x), green- presice y'(y), yellow on graphs- iter solution")
plt.ylabel("y(x)")
plt.xlabel("x")

pylab.show()

    # z=y'
def dU_dx(U, x):
    # Here U is a vector such that y=U[0] and z=U[1]. This function should return [y', z']
    return [U[1], -U[0] + x*np.exp(-x)]
U0 = [1, 0]
xs = np.linspace(0, 2, 200)
Us = odeint(dU_dx, U0, xs)
ys = Us[:,0]
data=np.loadtxt ("points.txt")
pylab.minorticks_on()
pylab.grid(color="black", which="major", linewidth=1)
pylab.grid(color="black", which="minor", linestyle=":", linewidth=0.5)
plt.xlabel("x")
plt.ylabel("y(x)")
plt.title("Zadacha Koshi, vstroennaya f-ya, red- y(x), blue- y'(x), green- y'(y), yellow on graphs- iter solution ")
plt.plot(xs,ys,'ro', color='red')
plt.plot(xs,Us[:,1],'ro',color= 'blue' )
plt.plot(ys,Us[:,1],'ro',color='green')
plt.plot(data[:,0], data[:,1],color='yellow')
plt.plot(data[:,0], data[:,2],color= 'yellow')
plt.plot(data[:,1], data[:,2],color= 'yellow')
pylab.show()

data=np.loadtxt ("points.txt")
pylab.minorticks_on()
pylab.grid(color="black", which="major", linewidth=1)
pylab.grid(color="black", which="minor", linestyle=":", linewidth=0.5)
plt.xlabel("x")
plt.ylabel("y(x)")
plt.plot(data[:,0], data[:,1]-data[:,3],color='red')
plt.plot(data[:,0], data[:,2]-data[:,4],color='blue')
plt.plot(data[:,1], data[:,2]-data[:,4],color='green')
plt.title("Zadacha Koshi, raznost graph, red- y(x), blue- y'(x), green- y'(y)")

pylab.show()
