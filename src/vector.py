import numpy as np


class Vector2:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def len(self):
        return np.sqrt(self.len2())

    def len2(self):
        return self.dot(self)

    def add(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def sub(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def mul(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)

    def mul(self, scalar):
        return Vector2(self.x / scalar, self.y / scalar)

    def __add__(self, other):
        self.add(other)

    def __sub__(self, other):
        return self.sub(other)

    def __mul__(self, scalar):
        return self.mul(scalar)

    def __div__(self, scalar):
        return self.div(scalar)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    # Rotates the vector anti-clockwise by angle (radians)
    def rot(self, angle):
        return Vector2(self.x * np.cos(angle) - self.y * np.sin(angle), self.x * np.sin(angle) + self.y * np.cos(angle))

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)
