from world import World
from particles import Particle
from vector import Vector2
from restraints import Spring
import pygame

pygame.init()

displayWidth = 800
displayHeight = 576

display = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Particles")

clock = pygame.time.Clock()

world = World()
world.set_gravity(Vector2(0, 0))

p1 = Particle(Vector2())
p2 = Particle(Vector2(0, 5), Vector2(0, -1))

s1 = Spring(1, 4, p1, p2)

world.add_particle(p1)
world.add_particle(p2)

tps = 5.0

crashed = False;
lastTime = 0
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    display.fill((33, 33, 33))

    if lastTime >= tps:
        world.update(1.0 / tps)
        world.print_particles()

        s1.update()

    clock.tick(tps)
    lastTime += clock.get_time()

    pygame.display.update()

pygame.quit()