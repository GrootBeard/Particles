from particles import Particle, Charge, Anchor
from vector import Vector2


class Disk(Particle):

    def __init__(self, position, velocity=Vector2(), mass=1, radius=1, elasticity=1):
        super().__init__(position, velocity, mass)
        self.radius = 1
        self.elasticity = elasticity
