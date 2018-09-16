from particle_manager import ParticleManager
from vector import Vector2
import pygame


class World:

    particle_texture = pygame.image.load("../assets/textures/particle_white.png")

    def __init__(self):
        self.particle_mng = ParticleManager()
        self.gravity = Vector2()

    def set_gravity(self, gravity):
        self.gravity = gravity

    def refresh_states(self):
        self.particle_mng.apply_global_force(self.gravity, True)

    def add_particle(self, particle):
        self.particle_mng.subscribe_particle(particle)
        particle.set_static_forces(self.gravity, True)

    def update(self, dt):
        self.particle_mng.update(dt)

    def integrate(self, dt):
        self.particle_mng.integrate(dt)

    def render(self, display):
        for p in self.particle_mng.particles:
            display.blit(self.particle_texture, p.position.get())

    def print_particles(self):
        for p in self.particle_mng.particles:
            print(p)
