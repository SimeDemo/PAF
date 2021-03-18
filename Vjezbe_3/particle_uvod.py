class Particle:
    def __init__(self, mass, x_0):
        self.mass = mass
        self.x_0 = x_0

    def printInfo(self):
        print(f"cestica ima masu {self.mass:.2f} i u pocetnom trenutku nalazi se na polozaju x={self.x_0:.2f}")

    
    def distance(self):
        print(f"Udaljenost od ishodista je {abs(self.x_0)}")

    
    def userDistance(self, x1):
        print(f"Udaljenost od ishodista je {abs(x1)}")



# p1 = Particle(10, -5)
# p1.printInfo()
# p1.distance()
# p1.userDistance(-73)

# p2 = Particle(20, 10)
# p2.printInfo()
# p2.mass = 10
# p2.printInfo()
# p2.distance()
