import matplotlib.pyplot as plt
from math import sin, cos, pi, sqrt
import numpy as np

# rjesiti time problem 
def kosi_hitac(theta, v0, time):

    theta = (theta/360)*2*pi 
    g = 9.81
    counter = -1 
    counter2 = -1
    accuracy = 1000
    dt = time / accuracy
    x_os = [0]
    y_os = [0]
    t = [0]

    v0x = v0*cos(theta)
    v0y = v0*sin(theta)

    vy = [v0y]

    for i in range(accuracy):
        counter += 1
        x_os.append(x_os[counter] + (v0x * dt))
        vy.append(vy[counter] - g * dt)
        y_os.append(y_os[counter] + vy[counter] * dt)
        t.append(t[counter] + dt)

    for j in y_os:
        if j < 0:
            break
        counter2 += 1

    plt.plot(x_os, y_os)
    plt.axis("equal")
    plt.xlim(0, x_os[counter2-1])
    plt.ylim(bottom=0)
    plt.show()
    

def max_h(v0, theta): 
    # y komponenta brzine na max h je jednaka nuli
    g = 9.81
    theta = (theta/360)*2*pi 
    dt = 0.1

    v0y = v0*sin(theta)
    vy = v0y
    h = 0 # u zadatku nije pisalo pa sam stavio da je pocetna visina 0
 
    while vy > 0:
        vy -=  g * dt
        h += vy * dt

    return print(f"Maksimalna visina koju je tijelo postiglo iznosi {h} metara")


def domet(v0, theta):
    # slicno kao i max_h, samo je ovdje x = 0 glavni dio 
    theta = (theta/360)*2*pi 
    g = 9.81
    counter = -1 
    counter2 = -1
    dt = 0.1
    x_os = [0]
    y_os = [0]
    t = [0]

    v0x = v0*cos(theta)
    v0y = v0*sin(theta)

    vy = [v0y]

    for i in range(1000):
        counter += 1
        x_os.append(x_os[counter] + (v0x * dt))
        vy.append(vy[counter] - g * dt)
        y_os.append(y_os[counter] + vy[counter] * dt)
    
    for j in y_os:
        if j < 0:
            break
        counter2 += 1

    domet = x_os[counter2]
    return print(f"Domet projektila je {domet} metara")


def v_max(v0, theta, time):
    
    counter = -1
    theta = (theta/360)*2*pi 
    g = 9.81
    accuracy = 1000
    dt = time / accuracy
    v0x = v0*cos(theta)
    v0y = v0*sin(theta)

    vy = [v0y]
    
    for i in range(accuracy):
        counter += 1
        vy.append(vy[counter] - g * dt)

    vy.sort()

    return print(f"Maksimalna brzina projektila je {abs(vy[-1])} m/s")


def shooting(ox, oy, r, theta, v0, time):

    theta = (theta/360)*2*pi 
    v0 = 20
    g = 9.81
    counter = -1 
    counter2 = -1
    accuracy = 1000
    dt = time / accuracy
    x_os = [0]
    y_os = [0]
    t = [0]
    distance = []

    v0x = v0*cos(theta)
    v0y = v0*sin(theta)

    vy = [v0y]

    ax = plt.cla()
    ax = plt.gca()
    plt.axis("equal")
    kruznica = plt.Circle((ox, oy), r, color="r", fill=False)
    ax.add_patch(kruznica)

    for i in range(accuracy):
        counter += 1
        x_os.append(x_os[counter] + (v0x * dt))
        vy.append(vy[counter] - g * dt)
        y_os.append(y_os[counter] + vy[counter] * dt)

    for j in y_os:
        if j < 0:
            break
        counter2 += 1

    for k in range(len(x_os)):
        d = sqrt((x_os[k]-ox)**2 + (y_os[k]-oy)**2)
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


    plt.plot(x_os, y_os)
    plt.ylim(0)
    plt.xlim(0, x_os[counter2])
    plt.show()
