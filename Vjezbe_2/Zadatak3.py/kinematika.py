import matplotlib.pyplot as plt
from math import sin, cos, pi
from numpy import linspace


def jednoliko_gibanje(m, F):
    brzine = []
    putevi = []
    t = linspace(0, 10, 100)
    a1 = []
    a = F/m

    for i in t:
        v = a*i
        x = v*i
        a1.append(a)
        brzine.append(v)
        putevi.append(x)

    fig, axs = plt.subplots(1, 3)
    axs[0].plot(t, a1)
    axs[0].set(xlabel="vrijeme, t [s]", ylabel="akceleracija, a [m/s^2]")
    axs[1].plot(t, brzine)
    axs[1].set(xlabel="vrijeme, t [s]", ylabel="brzina, v [m/s]")
    axs[2].plot(t, putevi)
    axs[2].set(xlabel="vrijeme, t [s]", ylabel="put, x [m]")
    axs[2].set_title("Put")
    axs[0].set_title("Akceleracija")
    axs[1].set_title("Brzina")
    plt.show()


def kosi_hitac(theta, v0):
    theta = (theta/360)*2*pi 
    xy_x = []
    xy_y = []
    g = 9.81
    time = linspace(0, 10, 1000)

    for i in time:
        x_os = v0 * i * cos(theta)
        y_os = (v0 * i * sin(theta)) - (0.5 * g * (i**2))
        xy_x.append(x_os)
        xy_y.append(y_os)

    fig, axs = plt.subplots(1, 3)

    axs[0].plot(xy_x, xy_y)
    axs[0].set_title("x - y Graf")

    axs[1].plot(time, xy_x)
    axs[1].set_title("x - t Graf")
    axs[1].set(xlabel="vrijeme, t [s]")

    axs[2].plot(time, xy_y)
    axs[2].set(xlabel="vrijeme, t [s]")
    axs[2].set_title("y - t Graf")

    plt.show()
