from math import pi, sin
import matplotlib.pyplot as plt

class ProjectileMotion:
    
    def __init__(self, y0, v0):
        
        self.theta = (90/360)*2*pi
        self.v0 = v0
        self.v = [self.v0 *sin(self.theta)] 
        self.y0 = y0
        self.y =[self.y0]
        self.t = [0]
        self.x = [0]

        print(f"Objekt je uspjesno stvore. Pocetna brzina objekta je {self.v0}, a visina {self.y0}.")

    
    def reset(self):

        self.v = [self.v0 *sin(self.theta)] 
        self.y =[self.y0]
        self.t = [0]
        self.x = [0]        


    def changeHeight(self, y0):

        self.y0 = y0


    def changeVelocity(self, v0):

        self.v0 = v0


    def __move(self, dt):

        g = 9.81
        self.v.append(self.v[-1] - g*dt)
        self.y.append(self.y[-1] + self.v[-1]*dt)
        self.x.append(0)
        self.t.append(self.t[-1] + dt)


    def eulersMethod(self, dt):
        
        while self.y[-1] >= 0:
            self.__move(dt)

        return self.t, self.x, self.y, self.v


    def maxHeight(self, dt):

        self.reset()

        while self.y[-1] >= 0:
            self.__move(dt) 

        self.y.sort()

        return print(f"Max height with dt={dt} is: {self.y[-1]}")


    def flightTime(self, dt):

        self.reset()

        while self.y[-1] >= 0:
            self.__move(dt) 

        return print(f"Flight time with dt={dt} is: {self.t[-1]}")


    def drag_force(self, k, v): # k is found between 0 and 1 

        return -k * abs(v)


    def __moveDrag(self, dt):


        self.drag = self.drag_force(0.8, self.v[-1])
        self.a = [self.drag / 10]
        g = 9.81
        self.t.append(self.t[-1] + dt)
        self.a.append(self.drag/10) # let mass = 10
        self.v.append(self.v[-1] - ((g-self.drag)*dt))
        self.y.append(self.y[-1] + self.v[-1]*dt)
        self.x.append(0)


    def dragged_motion(self, dt):

        self.reset()

        while self.y[-1] >= 0:
            self.__moveDrag(dt)

        return self.t, self.x, self.y, self.v


        

p1 = ProjectileMotion(10, 10)

tlist, xlist, ylist, vlist = p1.eulersMethod(0.01)

p1.maxHeight(0.01)
p1.flightTime(0.05)


def plotGraph():

    vlist2 = []

    for i in vlist:
        vlist2.append(abs(i))

    fig, axs = plt.subplots(1, 3)

    axs[0].plot(tlist, xlist)
    axs[0].set(ylabel="x coordinate", xlabel="time")
    axs[0].set_title("X coordinate over time")

    axs[1].plot(tlist, ylist)
    axs[1].set(ylabel="height", xlabel="time")
    axs[1].set_title("Height over time")

    axs[2].plot(tlist, vlist2)
    axs[2].set(ylabel="velocity", xlabel="time")
    axs[2].set_title("Velocity over time")

    plt.show()

plotGraph()

tlist_drag, xlist_drag, ylist_drag, vlist_drag = p1.dragged_motion(0.01)

ylist.sort()
ylist_drag.sort()
print("###################################")
print(f"Time without drag: {tlist[-1]}")
print(f"Time with drag: {tlist_drag[-1]}")
print("###################################")
print(f"Max height without drag: {ylist[-1]}")
print(f"Max height with drag: {ylist_drag[-1]}")
