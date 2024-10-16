import math
class Vector2:
    x = None
    y = None
    mag = None
    theta = None

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mag = math.sqrt(pow(x,2) + pow(y,2))
        if x == 0:
            self.theta = 0
        else:
            self.theta = math.atan(y / x)

    def setMag(self, mag):
        self.mag = mag
        self.x = mag * math.cos(self.theta)
        self.y = mag * math.sin(self.theta)

    def setAngle(self, theta):
        self.theta = theta
        self.x = self.mag * math.cos(theta)
        self.y = self.mag * math.sin(theta)

    def sum(vector1, vector2):
        if type(vector1) == Vector2 and type(vector2) == Vector2:
            newVectorX = vector1.x + vector2.x
            newVectorY = vector1.y + vector2.y
            return Vector2(newVectorX, newVectorY)

    def diff(vector1, vector2):
        if type(vector1) == Vector2 and type(vector2) == Vector2:
            newVectorX = vector1.x - vector2.x
            newVectorY = vector1.y - vector2.y
            return Vector2(newVectorX, newVectorY)
        
    def dist(vector1, vector2):
        if type(vector1) == Vector2 and type(vector2) == Vector2:
            diffX = vector2.x - vector1.x
            diffY = vector2.y - vector1.y
            dist = math.sqrt(pow(diffX, 2) + pow(diffY, 2))
            return dist
        
    def divide(vector1, vector2):
        quotientX = vector1.x / vector2.x
        quotientY = vector1.x / vector2.x
        return Vector2(quotientX, quotientY)
    
    def prod(vector1, other):
        prodX = vector1.x * other
        prodY = vector1.y * other
        return Vector2(prodX, prodY)
    
    def normalize(num, mag):
        if num == 0:
            return 0
        return num / mag
    
    def Normalize(self):
        mag = math.sqrt(pow(self.x, 2) + pow(self.y, 2))
        return Vector2(self.x / mag, self.y / mag)
        


    def ZERO():
        return Vector2(0,0)
    
    def invert(self):
        self.x *= -1
        self.x *= -1

    def mag(self):
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))
    
    def calc(self, acc):
        vec = self.normalize
        vec.x *= acc
        vec.y *= acc
        return vec

