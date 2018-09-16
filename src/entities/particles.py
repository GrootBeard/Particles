from vector import Vector2 as Vec2


class Entity(object):

    def __init__(self):
        self.__id = -1

    def update(self):
        pass

    def set_id(self, i):
        if self.__id < 0 <= i:
            self.__id = i

    def get_id(self):
        return self.__id


class Particle(Entity):

    def __init__(self, position, velocity=Vec2(0, 0), mass=1):
        self.position = position
        self.velocity = velocity
        self.forces = Vec2()
        self.static_forces = Vec2()
        self.mass = mass
        self.connections = []
        super().__init__()

    def apply_force(self, force):
        self.forces += force

    def integrate(self, dt):
        # print("total force on {0}: {1}".format(self.get_id(), self.get_total_force()))
        self.velocity += self.get_total_force() * dt / self.mass
        self.position += self.velocity * dt

    def get_total_force(self):
        return self.forces + self.static_forces

    def clear_forces(self):
        self.forces = Vec2()

    def set_static_forces(self, force, is_acceleration=False):
        self.static_forces = force * (1 if not is_acceleration else self.mass)

    def connect(self, other, connection):
        connection.connect(self, other)
        self.connections.append(connection)
        other.connections.append(connection)

    def __str__(self):
        return "id: {0}, pos: {1}, vel: {2}".format(self.get_id(), self.position, self.velocity)

    @classmethod
    def from_particle(cls, particle):
        return Particle(particle.position, particle.velocity, particle.mass)


class Charge(Particle):

    def __init__(self, position, velocity=Vec2(), mass=1, charge=0):
        self.charge = charge
        super(self.__class__, self).__init__(position, velocity, mass)


class Anchor(Particle):

    def __init__(self, position, mass=1):
        super().__init__(position, Vec2(0, 0), mass)

    def integrate(self, dt):
        pass

    def release(self):
        return Particle(self.position, mass=self.mass)
