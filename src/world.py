from .particle_manager import ParticleManager
from .vector import Vector2


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
            p.integrate(dt)

    def print_particles(self):
        for p in self.particle_mng.particles:
            print(p)
