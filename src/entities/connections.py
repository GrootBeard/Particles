from entities.particles import Entity
from vector import Vector2


class Connection(Entity):

    def __init__(self):
        self.p1 = None
        self.p2 = None

    def connect(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def disconnect(self):
        self.p1 = None
        self.p2 = None

    def update(self):
        pass


class Spring(Connection):

    def __init__(self, constant, rest_length, damping=0.0):
        super().__init__()
        self.spring_constant = constant
        self.rest_length = rest_length
        self.damping = damping
        self.orientation = Vector2()

    def update(self, dt):
        self.orientation = self.p1.position - self.p2.position

        stretch = max(0, self.orientation.len() - self.rest_length)
        linear_damp = (self.p1.velocity + self.p2.velocity) * self.damping

        self.p1.apply_force(
            -self.orientation.unit() * stretch * self.spring_constant - (linear_damp if stretch > 0 else Vector2()))
        self.p2.apply_force(
             self.orientation.unit() * stretch * self.spring_constant + (linear_damp if stretch > 0 else Vector2()))
