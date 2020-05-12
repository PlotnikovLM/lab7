# -*- coding: utf-8 -*-
import pylab
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
    # z=y'
def dU_dx(U, x):
    # Here U is a vector such that y=U[0] and z=U[1]. This function should return [y', z']
    return [U[1], -U[0] + x*np.exp(-x)]
U0 = [1, 0]
xs = np.linspace(0, 2, 200)
Us = odeint(dU_dx, U0, xs)
ys = Us[:,0]
pylab.minorticks_on()
pylab.grid(color="black", which="major", linewidth=1)
pylab.grid(color="black", which="minor", linestyle=":", linewidth=0.5)
plt.xlabel("x")
plt.ylabel("y(x)")
plt.title("Zadacha Koshi, red- y(x), blue- y'(x), green- y'(y) ")
plt.plot(xs,ys, color='red')
plt.plot(xs,Us[:,1], color= 'blue' )
plt.plot(ys,Us[:,1], color='green')
pylab.show()