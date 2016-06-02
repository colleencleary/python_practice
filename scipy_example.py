'''This is a SciPy example where we used curve fit to fit a curve and plot the results'''

#let's play with scipy
import numpy as np
import matplotlib.plot as plt
from scipy.optimize import curve_fit
def func(x, a, b, c):
    '''This returns an array from performing e?? on x where 
    x is the element in the array. a,b,c are just constants of the function.'''
    return a * np.exp(-b * x) + c

xdata = np.linspace(0, 4, 50)
y = func(xdata, 2.5, 1.3, 0.5)
ydata = y + 0.2 * np.random.normal(size=len(xdata))
#same as
#ydata= func(xdata, 2.4, 1.3, 0.5)+0.2*np.random.normal(sixe=len(xdata))
#e.g
#ydata=func(xdata, *params) + eps(ilon)
#popt=array([ 2.90001159,  1.23552219,  0.43274155])

#popt is an array of parameters minimizing sum of square error
#pcov covariance
popt, pcov = curve_fit(func, xdata, ydata)

#original y data that helped create perturbed y data
plt.plot(xdata, y, 'g')
# perturbed y data
plt.plot(xdata,ydata, color= 'blue', marker='*')
#best fit y data to the perturbed data
plt.plot(xdata, func(xdata, popt[0], popt[1], popt[2]), color='red',marker='o')

plt.show()
