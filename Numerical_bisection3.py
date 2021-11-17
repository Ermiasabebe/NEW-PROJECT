

 

import numpy as np


import matplotlib.pyplot as plt


import numpy as np

import matplotlib.pyplot as plt



def fun(x):

	rational = 1/x - 0.5
	
	return rational
	
	
x = np.linspace(0.5, 3.0, 200)

rational = fun(x)

plt.plot(x, rational, 'r')

plt.grid(True)

plt.xlabel('x')

plt.ylabel('y') 


#initial interval [a. b]

a, b = 0.5, 3.0

N = 200 # maximum number of iteration 

eps = 1.0e-4  # Tolerance on the interval 

delta = 1.0e-4 # Tolerance on the function 


fa, fb = fun(a), fun(b) 

sa, sb = np.sign(fa), np.sign(fb) 

"""
Returns an element-wise indication of the sign of a number.

The `sign` function returns ``-1 if x < 0, 0 if x==0, 1 if x > 0``.  nan
is returned for nan inputs.

For complex inputs, the `sign` function returns
``sign(x.real) + 0j if x.real != 0 else sign(x.imag) + 0j``.

complex(nan, 0) is returned for complex nan inputs.

"""


for i in range(N):

	e = b-a 
	
	c = a + 0.5*e 
	
	if abs(e) < eps*abs(c):
	
		print ("Interval function is below tolerance\n")
		
		break 
		
	fc = fun(c) 
	
	if abs(fc) < delta:
	
		print ("Function value is below tolerance\n")
		
		break
		
	sc = np.sign(fc)
	
	if sa != sc:
		b = c
		
		fb = fc 
		
		sb = sc 
		
	else:
	
		a = c
		
		fa = fc 
		
		sb = sc 
		
		print ("%5d %16.8e %16.8e %16.8e"%(i+1, c, abs(b-a), abs(fc)))