import matplotlib.pyplot as plt
from math import sin, cos, pi
import numpy as np


v0 = 30
theta = (30/360)*2*pi 
xy_x = []
xy_y = []
g = 9.81
time = np.linspace(0, 10, 1000)

for i in time:
    x_os = v0 * i * cos(theta)
    y_os = (v0 * i * sin(theta)) - (0.5 * g * (i**2))
    xy_x.append(x_os)
    xy_y.append(y_os)

plt.plot(xy_x, xy_y)
plt.gca()
plt.show()
