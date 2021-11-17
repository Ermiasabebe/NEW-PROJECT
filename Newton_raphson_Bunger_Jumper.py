import numpy as np 

import numpy as np 


import sympy as sym 

import matplotlib.pyplot as plt 

from sympy import Symbol, exp, atan, diff, lambdify

"""
Detrmine the mass of the bungee jumper with a drag coeficient of 0.25 kg/m to have a velocity of 36 m/s after 4 s of free fall. The acceleration of gravity is 9.8 m/s^2
"""

g = 9.8 

c = 0.25 

v = 36 

t = 4 


x = Symbol('x') 

#define the function 

fun = sym.sqrt(g*x/c)*sym.tanh(sym.sqrt(g*c/x)*t) - v

#compute its derivative 

der = sym.diff(fun, x)

print ("f = ", fun) 

print("df = ", der) 


# Make functions 


F = sym.lambdify(x, fun, modules =['numpy'])

DF = sym.lambdify(x, der, modules =['numpy'])

X = np.linspace(-1, 1, 100)

plt.figure(figsize = (9,4))

plt.subplot(1,2,1) 

plt.plot(X, F(X))

plt.grid(True)

plt.title("Function")

plt.subplot(1,2,2)

plt.plot(X, DF(X))

plt.grid(True)

plt.title('Derivatives')


M = 20   # maximum iterations

x = 0.5  # Initial guess 

eps = 1e-15 # relative tolerance on root 


f = F(x) 

for i in range(M):

	df = DF(x)
	
	dx = -f/df 
	
	x = x + dx 
	
	e = abs(dx)
	
	f = F(x) 
	
	print ("%6d %22.14e %22.14e %22.14e" %(i, x, e, abs(f)))
	
	if e < eps*abs(x):
	
		break 