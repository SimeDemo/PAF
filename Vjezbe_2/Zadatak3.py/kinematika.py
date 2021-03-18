import matplotlib.pyplot as plt
from math import sin, cos, pi
from numpy import linspace


def jednoliko_gibanje(m, F):
    
    brzine = []
    putevi = []
    dt = 0.1
    a1 = []
    v = [0]
    x = [0]
    t = []
    a = F/m
    counter = -1 

    for i in range(100):
        counter += 1
        v.append(v[counter] + a*dt)
        x.append(x[counter] + v[counter]*dt)
        a1.append(a)
        t.append(dt*i)

    v.pop(0)
    x.pop(0)

    fig, axs = plt.subplots(1, 3)
    axs[0].plot(t, a1)
    axs[0].set(xlabel="vrijeme, t [s]", ylabel="akceleracija, a [m/s^2]")
    axs[1].plot(t, v)
    axs[1].set(xlabel="vrijeme, t [s]", ylabel="brzina, v [m/s]")
    axs[2].plot(t, x)
    axs[2].set(xlabel="vrijeme, t [s]", ylabel="put, x [m]")
    axs[2].set_title("Put")
    axs[0].set_title("Akceleracija")
    axs[1].set_title("Brzina")
    plt.show()


def kosi_hitac(theta, v0):

    theta = (theta/360)*2*pi 
    g = 9.81
    counter = -1 
    dt = 0.1
    x_os = [0]
    y_os = [0]
    t = [0]

    v0x = v0*cos(theta)
    v0y = v0*sin(theta)

    vy = [v0y]

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
