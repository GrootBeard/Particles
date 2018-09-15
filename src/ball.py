from particles import Particle, Charge, Anchor
from vector import Vector2


class ball(Particle):

    def __init__(self, position, velocity=Vector2(), mass=1, radius=1, elasticity=1):
        self.radius = 1
        self.elasticity = elasticity
        super().__init__(position, velocity, mass)
