

import numpy as np


import matplotlib.pyplot as plt


def expsin(x):

	f = np.exp(x) -np.sin(x)
	
	return f 
	

def linsin(x):

	f = x**2 - 4.0*x*np.sin(x) + (2.0*np.sin(x))**2
	
	return  f 
	
def linearsin(x):

	f = x**2 - 4.0*x*np.sin(x) + (2.0*np.sin(x))**2 -0.5
	
	return f
	
	
def Bisect(fun, a, b, N = 200, eps = 1.0e-4, delta = 1.0e-4, debug = False):

	fa, fb = fun(a), fun(b) 
	
	sa, sb = np.sign(fa), np.sign(fb)
	
	if abs(fa) < delta: 
	
		return (a,0)
		
	if abs(fb) < delta:
	
		return (b, 0)
		
	#Check the interval is admissible 
		
	if fa*fb > 0.0:
	
		if debug:
			
			print ("Interval is not admissable\n")
			
		return (0, 1)
		
		
	for i in range (N):
	
		e = b-a
		
		c = a + 0.5*e
		
		if abs(e) < eps*abs(c):
		
			if debug:
			
				print ("Interval size is below tolerance\n")
				
				
			return (c,0)
			
		fc = fun(c)
		
		if abs(fc) < delta:
		
			if debug:
			
				print ("Function value is below tolerance\n")
				
				
				
			return (c,0)
			
		sc = np.sign(fc)
		
		if sa != sc:
		
			b = c 
			
			fb = fc 
			
			sb = sc 
			
		else:
		
			a = c
			
			fa = fc 
			
			sa = sb 
			
		if debug:
		
			print ("%5d %16.8e %16.8e  %16.8e" %(i+1, c, abs(b-a), abs(fc)))
			
	print ("No convergence in %d iteration" % N) 
	
	return (0,2) 
	
	


M =  200

eps = 1.0e-4

delta = 1.0e-4 

a, b = -4.0, -2.0

r, status = Bisect(expsin, a, b, M, eps, delta, True)



M =  200

eps = 1.0e-4

delta = 1.0e-4 

a, b = -4.0, -2.0

r, status = Bisect(linsin, a, b, M, eps, delta, True)  


x = np.linspace(-3, 3, 500)

y = linsin(x)

plt.plot(x, y)

plt.grid(True) 


M =  200

eps = 1.0e-4

delta = 1.0e-4 

a, b = -4.0, -2.0

r, status = Bisect(linearsin, a, b, M, eps, delta, True)  		
		
		
	
			
			
			
			
			
			
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
	
	