from math import cos, sin, pi
import numpy as np 
import matplotlib.pyplot as plt

theta = (30/360)*2*pi 
v0 = 20
g = 9.81
counter = -1 
dt = 0.1
x_os = [0]
y_os = [0]
t = [0]

v0x = v0*cos(theta)
v0y = v0*sin(theta)

vy = [v0y]
#
for i in range(100):
    counter += 1
    x_os.append(x_os[counter] + (v0x * dt))
    vy.append(vy[counter] - g * dt)
    y_os.append(y_os[counter] + vy[counter] * dt)
    t.append(t[counter] + dt)

fig, axs = plt.subplots(1, 3)
axs[0].plot(x_os, y_os)
axs[0].set_title("x-y graf")
axs[1].plot(t, x_os)
axs[1].set_title('x-t graf')
axs[2].plot(t, y_os)
axs[2].set_title('y-t graf')
plt.show()