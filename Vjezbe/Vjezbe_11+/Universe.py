import math as m
import numpy as np


class Universe:

    def __init__(self):
        
        self.planets = []

    
    def create(self, planet):

        self.planets.append(planet)


    def __move(self, dt):

        for i in range(len(self.planets)):
            ga = np.array([0,0])
            
            for j in range(len(self.planets)):
                if i != j:
                    ga = ga + self.planets[i].GFA(self.planets[j])
                    # jel mozete dodatno pojasniti zasto se u liniji iznad mora pisati ga = ga...
                    # umjesti ga +=... , inace izacuje error
                    #numpy.core._exceptions.UFuncTypeError: Cannot cast ufunc 'add' output from
                    # dtype('float64') to dtype('int32') with casting rule 'same_kind'
            self.planets[i].ga = ga

        for planet in self.planets:

            planet.velocity = planet.velocity + planet.ga * dt # ocito i ovdje baca isti error...
            planet.position = planet.position + planet.velocity * dt
            planet.xcoords.append(planet.position[0])
            planet.ycoords.append(planet.position[1])

    
    def evolve(self, total_time, dt):
        time = 0
        while time < total_time:
            self.__move(dt) 
            time = time + dt # note, possible error here -> update: bome je i bio ovjde...
                             # to bi pod vjezbama objasnio jer me zanima zasto nije racunalo kako
                             # treba prije, ispalo bi sve oke samo bi graf izgledao ne kao vas


class Planet:

    def __init__(self, mass, r0, v0):

        self.m, self.r0, self.v0, self.a0 = mass, r0, v0, np.array([0, 0])
        self.position, self.velocity, self.ga = r0, v0, self.a0
        self.xcoords, self.ycoords = [], []


    def reset(self):
        
        mass, r0, v0 = self.m, self.r0, self.v0
        del self.m, self.r0, self.v0

        self.m, self.r0, self.v0, self.a0 = mass, r0, v0, np.array([0, 0])
        self.position, self.velocity, self.ga = r0, v0, self.a0
        self.xcoords, self.ycoords = [], []

    
    def r_magf(self, planet2):

        x1, y1 = self.position[0], self.position[1]
        x2, y2 = planet2.position[0], planet2.position[1]

        xcoord, ycoord = x1 - x2, y1 - y2

        return m.sqrt(pow(xcoord, 2) + pow(ycoord, 2))

    
    def GFA(self, planet2):

        G = 6.67408e-11

        r_mag = self.r_magf(planet2)
        r_vec = self.position - planet2.position
        r_hat = r_vec / r_mag

        return - ((G * planet2.m) / (pow(r_mag, 2))) * r_hat