from particleManager import ParticleManager
from vector import Vector2
from particles import Particle


class World:

    def __init__(self):
        self.particle_mng = ParticleManager()
        self.gravity = Vector2()

    def set_gravity(self, gravity):
        self.gravity = gravity

    def refresh_states(self):
        self.particle_mng.apply_global_force(self.gravity)

    def add_particle(self, particle):
        self.particle_mng.subscribe_particle(particle)
        particle.set_static_forces(self.gravity)

    def update(self, dt):
        for p in self.particle_mng.particles:
            #print(p.forces*dt)
            p.velocity += p.get_total_force() * dt
            p.position += p.velocity * dt

    def print_particles(self):
        for p in self.particle_mng.particles:
            print(p)


world = World()
world.set_gravity(Vector2(0, -1))

p1 = Particle(Vector2())

world.add_particle(p1)

while True:
    world.update(0.01)
    world.print_particles()
