import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as npla
from mpl_toolkits.mplot3d import Axes3D
import scipy as sp
import sympy as sy


A = np.matrix([[5,6,2],[4,7,19],[0,3,12]])

B = np.matrix([[14,-2, 12],[4,4,5],[5,5,1]])


#Solve linear Equation Ax = basestring


b = np.matrix([[-1],[2],[1]])

print(b) 


#Solve for xrange

x = np.linalg.solve(A,b)

print(x)


C = np.matrix([[8,5],[16,-25]])

D = np.matrix([[4],[-12]])

Solution = np.linalg.solve(C, D)

print (Solution)