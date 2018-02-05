# coding: UTF-8

import numpy as np
import matplotlib.pylab as plt

def relu(x):
    return np.maximum(0,x)

x = np.array([-1.0,1.0,2.0])
print(relu(x))

x = np.arange(-5.0,5.0,0.1)
y = relu(x)
plt.plot(x,y)
plt.ylim(-1.0,5)
plt.show()
