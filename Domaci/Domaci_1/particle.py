from math import pi, cos, sin, sqrt
import matplotlib.pyplot as plt
import time

start_time = time.time()

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


    def total_time(self, delta_t):

        return len(self.y) * delta_t


    def max_speed(self):

        return print(sqrt((self.v0x**2) + (max(self.v0y, key=abs)**2)))


    def drawCircle(self, ox, oy, r):

        ax = plt.gca()
        ax.cla()
        kruznica = plt.Circle((ox, oy), r, color="r", fill=False)
        ax.add_patch(kruznica)


    def velocity_to_hit_target(self, ox, oy, r):

        velocities_to_hit = []
        self.drawCircle(ox, oy, r)
        self.v0 = 0

        while True:
            
            distance = []
            self.v0x = self.v0 * cos(self.theta)
            self.v0y = [self.v0*sin(self.theta)]
            self.x = [self.x0]
            self.y = [self.y0]

            while self.y[-1] >= 0:
                self.__move(0.001)

            for i in range(len(self.y)):
                distance.append(sqrt(((self.x[i]-ox)**2) + ((self.y[i]-oy)**2)))

            for j in distance:
                
                if j <= r:
                    velocities_to_hit.append(self.v0)
                    break
                elif j - r < 0.001:
                    velocities_to_hit.append(self.v0)
                    break

            self.v0 += 0.01

            if self.v0 > 50:
                break

        return velocities_to_hit


    def angle_to_hit_target(self, ox, oy, r):
        
        angles_to_hit = []
        self.drawCircle(ox, oy, r)
        self.theta = 0

        while True:

            distance = []
            self.v0x = self.v0 * cos(self.theta)
            self.v0y = [self.v0*sin(self.theta)]
            self.x = [self.x0]
            self.y = [self.y0]

            while self.y[-1] >= 0:
                self.__move(0.001)

            for i in range(len(self.y)):
                distance.append(sqrt(((self.x[i]-ox)**2) + ((self.y[i]-oy)**2)))

            for j in distance:

                if j <= r:
                    angles_to_hit.append((self.theta * 180) / pi) # pretvaram u stupnjeve 
                    break
                elif j - r < 0.001:
                    angles_to_hit.append((self.theta * 180) / pi) 
                    break

            self.theta += (0.5/360)*2*pi

            # self.drawCircle(ox, oy, r)
            # plt.plot(self.x, self.y)
            # plt.show()

            if self.theta > pi:
                break

        return angles_to_hit # u stupnjevima

p1 = Particle(30, 30, 0, 0)
p1.velocity_to_hit_target(4, 4, 2) # treba mu malo duze da izracuna rezultat, 1min otprilike na battery savingu na laptopu
p1.angle_to_hit_target(4, 4, 2)


print("--- %s seconds ---" % (time.time() - start_time))