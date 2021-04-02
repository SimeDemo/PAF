import calculus as cal
import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos

trigo_list = []
cubic_list = []

def cubic(x):

    return x**3


def trigo(x):
    return sin(x)


y_cubic, x_os = cal.derivate_3pm(cubic, 0, 10, 0.01)
y_trigo, x_os = cal.derivate_3pm(trigo, 0, 10, 0.01)

for i in x_os: 
    trigo_list.append(cos(i))
    cubic_list.append((3*(i**2)))

fig, axs = plt.subplots(1, 2)
axs[0].scatter(x_os, y_trigo, s=10, c="black")
axs[0].plot(x_os, trigo_list)
axs[0].set(xlabel="x", ylabel="f(x)")
axs[0].set_title("Derivative of sin(x)")

axs[1].scatter(x_os, y_cubic, s=10, c="black")
axs[1].plot(x_os, cubic_list)
axs[1].set(xlabel="x", ylabel="f(x)")
axs[1].set_title("Derivative of x^3")

plt.show()
