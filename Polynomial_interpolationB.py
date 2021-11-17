

import pandas as pd 

import matplotlib.pyplot as plt


hours = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.]
temperature_celcius = [22, 20.5, 19, 18.5, 18, 18, 18.5, 19, 21, 23, 24, 24.5, 25, 26, 27, 28, 28, 26, 24.5, 23, 22, 22, 21.5, 21, 22]


#Creat a pandas dataframe 

data = pd.DataFrame({'hours':hours, 'temp': temperature_celcius})

data 

#Create a scatter plot from the temprature per hour 

plt.figure(figsize =(12, 10))

plt.scatter(data.hours, data.temp)

plt.xlabel('Time')

plt.ylabel("Temperature")

plt.grid()

plt.show()

import numpy as np

import scipy.interpolate as interpolate


#Create a linear interpollation function based on the original dataframe

linear_interpolation_func = interpolate.interp1d(data.hours, data.temp, kind = 'linear')

#Note that 1 hour = 60 minutes. Hence, there are 10 divisions in one 1 hour. 24 hours have 240 divisions. 

Hour_scale = np.linspace(0.0, 24.0, 24*10)

#Interpolate the temparature on the 6-minute scale 

#Note that 1 hour = 60 minutes. Hence, there are 10 divisions in one 1 hour

Lin_inter_y = linear_interpolation_func (Hour_scale)

plt.figure(figsize=(12,10))

plt.scatter(data.hours, data.temp)

plt.plot(Hour_scale, Lin_inter_y, 'red')

plt.legend(['Linear Interpolation', 'Original'])

plt.xlabel('Time')

plt.ylabel('Temperature')

plt.grid()

plt.show()


# Create an interpolation function for Nearest Neighbors interpolation
nearestneighbors_interpolation_func = interpolate.interp1d(list(data.hours), list(data.temp), kind='nearest')

# Use the 6-mitue scale from before to interpolate values using the Nearest Neighbors interpolation function
nearestneighbors_interpolated_y = nearestneighbors_interpolation_func(Hour_scale)

# Plot the results of the Nearest Neighbors interpolation on top of the Linear interpolation
plt.figure(figsize=(12, 10), dpi=80)
plt.scatter(data.hours, data.temp)
plt.plot(Hour_scale, Lin_inter_y, 'red')
plt.plot(Hour_scale, nearestneighbors_interpolated_y, 'green')
plt.legend(['Linear Interpolation', 'Nearest Neighbors interpolation', 'Original'])
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.grid()
plt.show()
"""
degree_2_polynomial = lambda x: 1 + x + x**2
plt.plot(x, [degree_2_polynomial(i) for i in x])
"""



import matplotlib.pyplot as plt
from scipy import interpolate
x = np.arange(0, 10)
y = np.exp(-x/3.0)
f = interpolate.interp1d(x, y)

xnew = np.arange(0, 9, 0.1)
ynew = f(xnew)   # use interpolation function returned by `interp1d`
plt.plot(x, y, 'o', xnew, ynew, '-')
plt.show()























