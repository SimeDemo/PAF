import calculus as cal
import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos

trigo_list = []
cubic_list = []
der_range = np.linspace(0, 10, 100) # tbc

def cubic(x):

    return x**3

def trigo(x):
    return sin(x)


for i in der_range:
    trigo_list.append(cos(i))
    cubic_list.append((3*i)**2)


print(cubic_list)
print("###############################")
print(cal.derivate_3pm(cubic, 0, 10, 0.0001))

# fig, axs = plt.subplots(1, 2)
# axs[0].plot(cal.derivate_3pmm(trigo, 0, 10, 0.0001), cal.derivate_3pm(trigo, 0, 10, 0.0001))
# axs[0].plot(der_range, trigo_list, "--")
# axs[0].set(xlabel="x", ylabel="f(x)")
# axs[0].set_title("Derivative of sin(x)")
# axs[1].plot(cal.derivate_3pmm(cubic, 0, 10, 0.000001), cal.derivate_3pm(cubic, 0, 10, 0.000001))
# axs[1].plot(der_range, cubic_list, "--")
# axs[1].set(xlabel="x", ylabel="f(x)")
# axs[1].set_title("Derivative of x^3")
# plt.show()
