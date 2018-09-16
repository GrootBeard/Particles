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
world.set_gravity(Vector2(0, 9.8))

p1 = Particle(Vector2(30, 60), mass=1)
p2 = Particle(Vector2(60, 60), Vector2())
p3 = Particle(Vector2(90, 60), Vector2(0, 0), mass=1)
p4 = Particle(Vector2(120, 60), mass=1)
p5 = Particle(Vector2(150, 60), Vector2())
p6 = Particle(Vector2(180, 60), Vector2(0, 0), mass=1)
p7 = Particle(Vector2(210, 60), Vector2(0, 0), mass=1)


a1 = Anchor(Vector2(0, 60))
a2 = Anchor(Vector2(240, 60))

c = 5
l = 1

s0 = Spring(c, l, a1, p1)
s1 = Spring(c, l, p1, p2)
s2 = Spring(c, l, p2, p3)
s3 = Spring(c, l, p3, p4)
s4 = Spring(c, l, p4, p5)
s5 = Spring(c, l, p5, p6)
s6 = Spring(c, l, p6, p7)
s7 = Spring(c, l, p7, a2)


world.add_particle(p1)
world.add_particle(p2)
world.add_particle(p3)
world.add_particle(p4)
world.add_particle(p5)
world.add_particle(p6)
world.add_particle(p7)
world.add_particle(a1)
world.add_particle(a2)

tps = 100.0

crashed = False;
lastTime = 0
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    display.fill((33, 33, 33))

    if lastTime >= tps:
        world.update()
        # world.print_particles()

        s0.update()
        s1.update()
        s2.update()
        s3.update()
        s4.update()
        s5.update()
        s6.update()
        s7.update()

        world.integrate(1.0 / tps)

    world.render(display)

    clock.tick(tps)
    lastTime += clock.get_time()

    pygame.display.update()

pygame.quit()
