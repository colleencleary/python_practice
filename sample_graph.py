'''This is a sample graph'''
import numpy as np
import matplotlib.pyplot as plt

mydata=np.loadtxt(data.txt)
x=mydata[:,0]
y=mydata[:,1]
plt.plot(x,y, color='green', marker='*')
plt.show()
