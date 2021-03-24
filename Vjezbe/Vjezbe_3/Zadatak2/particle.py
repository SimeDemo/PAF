from math import pi, cos, sin, sqrt
import matplotlib.pyplot as plt

class Particle:

    def __init__(self, v0, theta, x0, y0):

        self.theta = (theta/360)*2*pi
        self.v0 = v0
        self.v0x = v0*cos(self.theta)
        self.v0y = []
        self.v0y.append(v0*sin(self.theta))
        self.x0 = x0
        self.y0 = y0
        self.x = []
        self.y = []
        self.x.append(self.x0)
        self.y.append(self.y0)

    
    def printinfo(self):

        print(f"v0 = {self.v0}, theta = {self.theta}")


    def reset(self):

        self.theta = 0
        self.v0 = 0
        self.v0x = 0
        self.v0y = []
        self.x0 = 0
        self.y0 = 0
        self.x = []
        self.y = []

    
    def __move(self, dt):
        
        global g
        g = 9.81
        self.v0y.append(self.v0y[-1] - g*dt)
        self.x.append(self.x[-1] + self.v0x*dt)
        self.y.append(self.y[-1] + self.v0y[-1]*dt)
        

    def range_p(self, delta_t):

        while self.y[-1] >= 0:
            self.__move(delta_t)

        global counter3 
        counter3 = -1 

        for j in self.y:
            if j < 0:
                break
            counter3 += 1

        return self.x[counter3] - self.x0

    
    def plot_trajectory(self):
        plt.plot(self.x, self.y)
        plt.show()
    
            
    def analytically(self):

        return (self.v0x * (self.v0y[0] + sqrt((self.v0y[0])**2 + 2*9.81*self.y0)) / 9.81)

