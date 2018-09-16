from world import World
from entities.particles import Particle, Anchor
from vector import Vector2
from entities.connections import Spring
import pygame

pygame.init()

displayWidth = 800
displayHeight = 576

display = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Particles")

clock = pygame.time.Clock()

world = World()
world.set_gravity(Vector2(0, 1000))

n = 50

particles = [Anchor(Vector2(0, 60))]
for i in range(n):
    particles.append(Particle(Vector2((i + 1) * 4, 60), mass=(1/100 if (i == n//2) else 1/100)))
    print(particles[i].mass)
particles.append(Anchor(Vector2((n + 1) * 4, 60)))

for i in range(len(particles) - 1):
    world.add_particle(particles[i])
    particles[i].connect(particles[i + 1], Spring(100, 0, damping=0.0))
world.add_particle(particles[-1])

tps = 100.0

crashed = False;
lastTime = 0
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    display.fill((33, 33, 33))

    if lastTime >= tps:
        dt = 1.0 / tps

        world.update(dt)
        # world.print_particles()

        world.integrate(1.0 / tps)

    world.render(display)

    clock.tick(tps)
    lastTime += clock.get_time()

    pygame.display.update()

pygame.quit()
