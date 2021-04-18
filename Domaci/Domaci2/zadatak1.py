import matplotlib.pyplot as plt

class ForceCalculator:

    def __init__(self, m, x0, v0, t, force):

        self.m = m
        self.x0 = x0
        self.x = [self.x0]
        self.v0 = v0
        self.v = [self.v0]
        self.t = t
        self.t_list = [0]
        self.force = force(self.v[-1], self.x[-1], self.t_list[-1])
        self.a = [self.force/ self.m]
        self.name = force

    
    def reset(self):

        self.x =[self.x0]
        self.v = [self.v0]
        self.t_list = [0]
        self.a = [self.force/ self.m]

    def __move(self, force):

        dt = 0.0001

        for i in range(int(self.t/dt)):

            self.force = force(self.v[-1], self.x[-1], self.t_list[-1])
            self.t_list.append(self.t_list[-1] + dt)
            self.a.append(self.force/self.m)
            self.v.append(self.v[-1] + (self.a[-1] * dt))
            self.x.append(self.x[-1] + (self.v[-1] * dt))


    def graphing(self):

        self.__move(self.name)

        fig, axs = plt.subplots(1, 3)

        axs[0].plot(self.t_list, self.a)
        axs[0].set_title("akceleracija")

        axs[1].plot(self.t_list, self.v)
        axs[1].set_title("brzina")

        axs[2].plot(self.t_list, self.x)
        axs[2].set_title("pomak")

        plt.show()


def constant_force(v, x, t):

    F = 100

    return F


def elastic_force(v, x, t):

    k = 100
    F = -k * x
    
    return F


p1 = ForceCalculator(10, 0, 10, 10, constant_force)
p1.graphing()