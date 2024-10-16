from Vector2 import Vector2
import math
import pygame

class planet():
    UGC = 1
    accX = 0
    accY = 0
    def __init__(self, mass=100, posX=600, posY=450, velX=0, velY=0, radius=15, color='blue'):
        self.mass = mass
        self.pos = Vector2(posX, posY)
        self.vel = Vector2(velX, velY)
        self.acc = Vector2(0, 0)
        self.radius = radius
        self.color = color
    
    def gravity(self, masses):
        self.acc = Vector2(0,0)
        for other in masses:
            if other != self:
                dist = math.sqrt(pow((other.pos.x - self.pos.x), 2) + pow((other.pos.y - self.pos.y), 2))

                force = (other.mass * self.mass) / pow(dist, 2)
                acceleration = force / self.mass

                vectorDist = Vector2.diff(other.pos, self.pos)
                vectorDist = vectorDist.Normalize()

                accelerationV = Vector2.prod(vectorDist, acceleration)
                self.acc = Vector2.sum(self.acc, accelerationV)




    def update(self, FPS):
        self.vel = Vector2.sum(self.vel, Vector2.prod(self.acc, 10/FPS))
        self.pos = Vector2.sum(self.pos, Vector2.prod(self.vel, 10/FPS))

    