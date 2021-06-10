from matplotlib.animation import FuncAnimation
import Universe as uni
import numpy as np
import matplotlib.pyplot as plt

au, day = 1.496e11, 60*60*24
year = 365.242 * day


sun = uni.Planet(1.989e30, np.array([0,0]), np.array([0,0]))
mercury = uni.Planet(3.3e24, np.array([0,0.466*au]), np.array([-47362,0]))
venus = uni.Planet(4.8685e24, np.array([0.723*au,0]), np.array([0,35020]))
earth = uni.Planet(5.9742e24, np.array([-au,0]), np.array([0,-29783]))
mars = uni.Planet(6.417e23, np.array([0,-1.666*au]), np.array([24007,0]))

comet = uni.Planet(1.989e15, np.array([4*au, 4*au]), np.array([-10000, -15000]))
# comet = uni.Planet(1.989e13, np.array([4*au, 4*au]), np.array([-10000, -15000]))

ss = uni.Universe()

ss.create(sun)
ss.create(mercury)
ss.create(venus)
ss.create(earth)
ss.create(mars)
ss.create(comet)

ss.evolve(5 * year, day)

fig, ax = plt.figure(figsize=(10, 10)), plt.axes(xlim=(-10*au, 10*au), ylim=(-10*au, 10*au))

line, = ax.plot([], [], 'o',color="brown")
line1, = ax.plot([], [], 'o',color="red")
line2, = ax.plot([], [], 'o',color="orange")
line3, = ax.plot([], [], 'o',color="blue")
line4, = ax.plot([], [], 'o',color="yellow")
line5, =ax.plot([], [], 'o', color="black")

plt.plot(sun.xcoords, sun.ycoords, label="Sun", color="yellow", linewidth=5.0)

plt.plot(mercury.xcoords, mercury.ycoords, label="Mercury", color="orange")

plt.plot(venus.xcoords, venus.ycoords, label="Venus", color="red")

plt.plot(earth.xcoords, earth.ycoords, label="Earth", color="blue")

plt.plot(mars.xcoords, mars.ycoords, label="Mars", color="brown")

plt.plot(comet.xcoords, comet.ycoords, label="comet", color="black")

xmer, xven, xear, xmar, xsun, xcom = [], [], [], [], [], []
ymer, yven, year, ymar, ysun, ycom = [], [], [], [], [], []


def init():

    line.set_data([], [])
    line1.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])
    line4.set_data([], [])
    line5.set_data([], [])

    return line, line1, line2, line3, line4, 


def animate(i):

    xsun.append(sun.xcoords[i])
    ysun.append(sun.ycoords[i])

    xmer.append(mercury.xcoords[i])
    ymer.append(mercury.ycoords[i])
    
    xven.append((venus.xcoords[i]))
    yven.append((venus.ycoords[i]))

    xear.append((earth.xcoords[i]))
    year.append((earth.ycoords[i]))

    xmar.append((mars.xcoords[i]))
    ymar.append((mars.ycoords[i]))
    
    xcom.append(comet.xcoords[i])
    ycom.append(comet.ycoords[i])

    line.set_data(xmer[i], ymer[i])
    line1.set_data(xven[i], yven[i])
    line2.set_data(xear[i], year[i])
    line3.set_data(xmar[i], ymar[i])
    line4.set_data(xsun[i], ysun[i])
    line5.set_data(xcom[i],ycom[i])

    # ax.plot(xven, yven, color="gray")
    # ax.plot(xear, year, color="blue")
    # ax.plot(xmar, ymar, color="red")

    return line,

# plt.xlabel("x")
# plt.ylabel("y")
#plt.legend(loc="upper right")
anim = FuncAnimation(fig, animate, init_func=init, interval=1)
plt.show()
