from math import cos

class Particle:
    def __init__(self, v0, theta, x0, y0):
        self.v0 = v0
        self.theta = theta
        self.x0 = x0
        self.y0 = y0
    

    def printinfo(self):
        print(f"v0 = {self.v0}, theta = {self.theta}")


    def reset(self):
        self.v0 = 0
        self.theta = 0
        self.x0 = 0
        self.y0 = 0

    
    def __move(self):
        x = [self.x0]
        counter = -1
        delta_t = 0.1
        for i in range(100):
            counter += 1
            x.append(x[counter] + self.v0*delta_t)

    def range(self):
        counter = -1
        delta_t = 0.1
        x_os = [self.x0]
        y_os = [self.y0]
        for i in range(10):
            counter += 1
            x_os.append(x_os[counter] + (self.v0 * delta_t * cos(self.theta)))
        return print(x_os)

    
            


p1 = Particle(10, 45, 5, 5)
# p1.reset()
p1.printinfo()
# p1.move()
p1.range()
