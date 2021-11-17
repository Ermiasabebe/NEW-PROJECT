

import numpy as np 

import matplotlib.pyplot as plt 


import numpy as np

import matplotlib.pyplot as plt 


#define the function 


def f(x):

	return (np.exp(-x) -x) 


#define the derivative of the function 

	
def df(x):

	return (-np.exp(-x) -1) 
	
x = np.linspace(0.0, 2.0, 100)

plt.plot(x, f(x))

plt.xlabel('x')

plt.ylabel('y')

plt.grid(True) 

def Newton(x0, m):


	n = 50
	
	x = np.zeros(50)
	
	x[0] = x0
	
	print("%6d %24.14e" % (0, x[0])) 
	
	for i in range (1,50):
	
		x[i] = x[i-1] - m* f(x[i-1])/df(x[i-1])
		
		if i > 1:
		
			r = (x[i] -x[i-1])/(x[i-1] -x[i-2])
			
		else:
		
		
			r= 0.0 
			
			print ("%6d %24.14e %14.6e" % (i, x[i], r))
			
			if abs(f(x[i])) < 1.0e-16:
			
				break
				
				
		
		
		
Newton(2.0, 1) 
