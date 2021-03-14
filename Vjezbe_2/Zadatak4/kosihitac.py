import matplotlib.pyplot as plt
from math import sin, cos, pi, sqrt
import numpy as np


def kosi_hitac(theta, v0, time):

    xy_x = []
    xy_y = []
    g = 9.81
    time = np.linspace(0, time, 1000)
    theta = (theta/360)*2*pi 
    counter = -1

    for i in time:
        x_os = v0 * i * cos(theta)
        y_os = (v0 * i * sin(theta)) - (0.5 * g * (i**2))
        xy_x.append(x_os)
        xy_y.append(y_os)

    for j in xy_y:
        counter += 1
        if j < 0:
            print(j)
            print(counter)
            break

    plt.plot(xy_x, xy_y)
    plt.axis("equal")
    plt.ylim(0)
    plt.xlim(0, xy_x[counter])
    plt.gca()
    plt.show()
    

def max_h(v0, theta): 

    g = 9.81
    theta = (theta/360)*2*pi 
    max_h = ((v0**2) * (sin(theta)**2)) / (2 * g)

    return print(f"Maksimalna visina koju je tijelo postiglo iznosi {max_h} metara")


def domet(v0, theta):

    g = 9.81
    theta = (theta/360)*2*pi
    domet = ((v0**2) * sin(2 * theta)) / g

    return print(f"Domet projektila je {domet} metara")


def v_max(v0):
    return print(f"Maksimalna brzina projektila je {v0} m/s")


def shooting(ox, oy, r, theta, v0, time):

    xy_x = []
    xy_y = []
    g = 9.81
    time = np.linspace(0, time, 1000)
    theta = (theta/360)*2*pi 
    counter = -1
    distance = []

    ax = plt.cla()
    ax = plt.gca()
    plt.axis("equal")
    kruznica = plt.Circle((ox, oy), r, color="r", fill=False)
    ax.add_patch(kruznica)

    for i in time:
        x_os = v0 * i * cos(theta)
        y_os = (v0 * i * sin(theta)) - (0.5 * g * (i**2))
        xy_x.append(x_os)
        xy_y.append(y_os)

    for j in xy_y:
        counter += 1
        if j < 0:
            print(j)
            print(counter)
            break

    for k in range(len(xy_x)):
        d = sqrt((xy_x[k]-ox)**2 + (xy_y[k]-oy)**2)
        distance.append(d)

    distance.sort()

    for l in distance:
        if l <= r:
            print("Meta je pogodjena")
            break
        elif l-r < 0.001:
            print("Meta je pogodjena")
            break
        else:
            print(f"Meta nije pogodjena, najbliza udaljenost je {l-r}")
            break


    plt.plot(xy_x, xy_y)
    plt.ylim(0)
    plt.xlim(0, xy_x[counter])
    plt.show()
