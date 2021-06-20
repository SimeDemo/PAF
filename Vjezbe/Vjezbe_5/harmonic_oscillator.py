from math import sin, pi, sqrt
from numpy import linspace
import matplotlib.pyplot as plt

class HarmonicOscillator:

    def __init__(self, m, k, x0, v0, t):

        self.m = m
        self.k = k
        self.x0 = x0
        self.x = [self.x0]
        self.v0 = v0
        self.v = [self.v0]
        self.a = [(-self.k / self.m) * self.x[-1]]
        self.t = t
        self.t_list = [0]

    def reset(self):
        self.x = [self.x0]
        self.v = [self.v0]
        self.a = [(-self.k / self.m) * self.x[-1]]
        self.t_list = [0]


    def oscillate(self, dt):

        for i in range(int(self.t/dt)):

            self.t_list.append(self.t_list[-1] + dt)
            self.a.append((-self.k / self.m) * self.x[-1])
            self.v.append(self.v[-1] + (self.a[-1] * dt))
            self.x.append(self.x[-1] + (self.v[-1] * dt))

        #print(f"t={self.t_list[-1]}, a={self.a[-1]}, v={self.v[-1]}, x={self.x[-1]}")

    
    def plot_oscillation(self):

        precision = [0.1, 1]
        color = ["black", "green"]
        size = [1, 5]

        fig, axs = plt.subplots(1, 3)

        axs[0].plot(self.t_list, self.a)
        axs[0].set_title("akceleracija")

        axs[1].plot(self.t_list, self.v)
        axs[1].set_title("brzina")

        axs[2].plot(self.t_list, self.x)
        axs[2].set_title("pomak")

        for i in range(2):

            self.reset()

            self.oscillate(precision[i])

            axs[0].scatter(self.t_list, self.a, s=size[i], c=color[i])
            axs[1].scatter(self.t_list, self.v, s=size[i], c=color[i])
            axs[2].scatter(self.t_list, self.x, s=size[i], c=color[i])
        # dodati legendu i tjt
        plt.show()

    def cal_period(self, dt):

        x0 = self.x0
        
        self.oscillate(dt)
        period = dt

        if self.x[-1] > x0:
            
            j = 1
        
        else:
            
            j = 2

        while True:

            x1 = self.x[-1]
            self.oscillate(dt)
            period += dt
            x2 = self.x[-1]

            if j == 1:
                if (x2 > x0) and (x1 < x0):
                    break
            else:
                if (x2 < x0) and (x1 > x0):
                    break

        return period


    def cal_period_analitical(self):

        return 2 * pi * sqrt(self.m / self.k)
