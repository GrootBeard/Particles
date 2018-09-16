class ParticleManager(object):

    def __init__(self):
        self.particles = []
        self.id_counter = 0
        self.available_ids = []

    def update(self):
        for p in self.particles:
            p.clear_forces()
            p.update()

    def integrate(self, dt):
        for p in self.particles:
            p.integrate(dt)

    def subscribe_particle(self, particle):
        if len(self.available_ids) == 0:
            particle.set_id(self.id_counter)
            self.id_counter += 1
        else:
            particle.set_id(self.available_ids[-1])
            self.available_ids.pop()

        self.particles.append(particle)

    def unsubscribe_particle(self, particle):
        self.particles.remove(particle)
        self.available_ids.append(particle.get_id())

    def apply_global_force(self, force, static=True):
        if static:
            for p in self.particles:
                p.set_static_forces(force, True)
        else:
            for p in self.particles:
                p.apply_force(force)
