import numpy as np

import matplotlib.pyplot as plt 


#Define the function 





def f(x):

	return (x-1.0)**2 * np.sin(x)


#define the derivative of the function 

	
def df(x):

	return 2.0*(x-1.0)* np.sin(x) + (x-1.0)**2 *np.cos(x)

"""	
	
#Plotting the function. 

 # plot a line, implicitly creating a subplot(111)
      plt.plot([1,2,3])
      # now create a subplot which represents the top plot of a grid
      # with 2 rows and 1 column. Since this subplot will overlap the
      # first, the plot (and its axes) previously created, will be removed
      plt.subplot(211)
      plt.plot(range(12))
      plt.subplot(212, facecolor='y') # creates 2nd subplot with yellow background
	  
	  
"""


plt.plot([1,2,3])
	
x = np.linspace(0.0, 2.0, 100)

plt.subplot(211)

plt.plot(x, f(x))

plt.xlabel('x')

plt.ylabel('y')
plt.grid(True)

plt.subplot(212)

plt.plot(x, df(x))

plt.xlabel('x')

plt.ylabel('dy/dx')

plt.grid(True) 


def NEWTON(f, df, x0, M =100, eps =1.0e-15):


	x = x0
	
	for i in range(M):  
		
		dx = -f(x)/df(x)
		
		x = x + dx 
		
		print("%3d %20.14f %20.14e" %(i, x, abs(f(x))))


		if abs(dx) < eps*abs(x):
		
			return x
			
	print("No convergence, current root = %e" % x) 
	
	
x0 = 2.0

x = NEWTON(f, df, x0) 

print (x) 
	
"""
	
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


#print ('when m= 1', Newton(2.0, 1) )
		
	
	
"""	
	
	
	




