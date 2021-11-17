import numpy as np 


import sympy as sym 

import matplotlib.pyplot as plt 

from sympy import Symbol, exp, atan, diff, lambdify

def f(x):

	return np.exp(x) -3.0/2.0 -np.arctan(x) 

#f = lambda x : np.exp(x) -3.0/2.0 -np.arctan(x) 

def fun(x):

	return (-x**3 - np.cos(x))
	
def runall(): 

	x = np.linspace(0.0, 1.0, 100)
	
	plt.figure(figsize = (9,4))

	plt.subplot(1,2,1) 

	plt.plot(x, f(x))

	plt.grid(True)

	plt.title("Exp and arctan Function")

	plt.subplot(1,2,2)

	plt.plot(x, fun(x))

	plt.grid(True)

	plt.title('x and Cos function')

	plt.plot(x, f(x))

	plt.grid(True)

	M = 50 # Maximum number of iterations

	eps = 1.0e-6 # Tolerance for stopping 

	x0, x1 = 0.5, 0.6 

	for i in range (M):

		f0, f1 = f(x0), f(x1)
	
		x2 = x1 - f1*(x1-x0)/(f1-f0)
	
		if abs(x2-x1) < abs(x2)*eps:
	
			break 
		
		print (i, x0, x1, f0, f1)
	
	
		x0, x1 = x1, x2
	
	
	print ("Number of iterations = ", i)

	print ("Final solution = ", x2, f(x2))