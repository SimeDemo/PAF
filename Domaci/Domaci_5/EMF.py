import math as m
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


class EMF:

    def __init__(self, p, v, E, B, q, m, f):

        self.p = p
        self.t = [0]
        self.x = [self.p[0]]
        self.y = [self.p[1]]
        self.z = [self.p[2]]
        self.E = E
        self.f = f
        self.B = f(self.t[-1])
        self.q = q
        self.m = m
        self.v = v


    def acc(self, _v):

        ac = (self.q/self.m) * (np.add(self.E, np.cross(_v, self.B)))

        return ac


    def reset(self):

        self.x, self.y, self.z, self.t = [], [], [], []
        self.p, self. E, self.B, self.q, self.m, self.v = 0, 0, 0, 0, 0, 0


    def __move(self, dt):

        self.v = np.add(self.v, self.acc(self.v) * dt)
        self.p = np.add(self.p, self.v * dt)
        self.B = self.f(self.t[-1])
        self.t.append(self.t[-1] + dt)

        self.x.append(self.p[0])
        self.y.append(self.p[1])
        self.z.append(self.p[2])


    def euler(self, total_time, dt):

        while self.t[-1] <= total_time:

            self.__move(dt)

        return self.x, self.y, self.z


    def __moveRK(self, dt):

        self.B = self.f(self.t[-1])

        k1v = self.acc(self.v) * dt
        k1p = self.v * dt
        k2v = self.acc(np.add(self.v, k1v / 2)) * dt
        k2p = (np.add(self.v,k1v / 2)) * dt
        k3v = self.acc(np.add(self.v, k2v / 2)) * dt
        k3p = (np.add(self.v, k2v / 2)) * dt
        k4v = self.acc(np.add(self.v, k3v)) * dt
        k4p = (np.add(self.v, k3v)) * dt

        self.v = np.add(self.v, (1/6) * np.add(np.add(k1v, 2*k2v), np.add(2*k3v, k4v)))
        self.p = np.add(self.p, (1/6) * np.add(np.add(k1p, 2*k2p), np.add(2*k3p, k4p)))
        self.t.append(self.t[-1] + dt)

        self.x.append(self.p[0])
        self.y.append(self.p[1])
        self.z.append(self.p[2])

    
    def RK(self, total_time, dt):

        while self.t[-1] <= total_time:

            self.__moveRK(dt)

        return self.x, self.y, self.z


    def electron_vs_positron(self, electorn, positron):

        ax = plt.axes(projection = "3d")

        ax.plot3D(electorn.x, electorn.y, electorn.z, label = "electron")
        ax.plot3D(positron.x, positron.y, positron.z, label = "positron")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")

        plt.legend()
        plt.show()


    def euler_vs_RK(self, x, y, z, xRK, yRK, zRK):

        ax = plt.axes(projection = "3d")

        ax.plot3D(x,y,z, label = "Euler")
        ax.plot3D(xRK, yRK, zRK, '-.', label = "Runge-Kutta")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")
        plt.legend()
        plt.show()


    def const_vs_TV(self, x, y, z, xTV, yTV, zTV):

        ax = plt.axes(projection = "3d")

        ax.plot3D(x, y, z, label = "const. MF")
        ax.plot3D(xTV, yTV, zTV, label = "TIme-varying MF")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")
        plt.legend()
        plt.show()


    def electron_vs_positron_TV(self, xE, yE, zE, xP, yP, zP):

        ax = plt.axes(projection = "3d")

        ax.plot3D(xE, yE, zE, label = "electron")
        ax.plot3D(xP, yP, zP, label = "positron")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")
        plt.legend()
        plt.show()