import numpy as np
from scipy.optimize import curve_fit
from scipy_gendat import gendat
from scipy_plot import plot_fit
from scipy_functions import func

#generate data
xdata=np.linspace(0, 4, 50)
y,ydata=gendat(xdata)

#fit the curve
popt, copt = curve_fit(func, xdata, ydata)

#plot the curves and best fit
plot_fit(func=func, xdata=xdata, ydata=ydata, y=y, popt=popt)
