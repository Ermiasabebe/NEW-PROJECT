import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as npla
from mpl_toolkits.mplot3d import Axes3D
import scipy as sp
import sympy as sy

A = np.array([[1,2], [3,4]])

print (A)

#Inverse Matrix 

B = npla.inv(A)

print(B) 


# Multiply A and B

I = A.dot(B)

print(I)
