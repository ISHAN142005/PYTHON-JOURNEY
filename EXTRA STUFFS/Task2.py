import pygame
import random
import math

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dynamic Particle System")
clock = pygame.time.Clock()


class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        angle = random.uniform(0, math.pi * 2)
        speed = random.uniform(2, 8)
        self.dx = math.cos(angle) * speed
        self.dy = math.sin(angle) * speed
        self.radius = random.randint(4, 10)
        self.color = [random.randint(100, 255) for _ in range(3)]
        self.life = 255

    def update(self):
        self.dy += 0.2
        self.x += self.dx
        self.y += self.dy
        self.life -= 3
        self.radius -= 0.05

        if self.y >= height - self.radius:
            self.y = height - self.radius
            self.dy *= -0.7

    def draw(self, surface):
        if self.radius > 0 and self.life > 0:
            pygame.draw.circle(
                surface, self.color, (int(self.x), int(self.y)), int(self.radius)
            )


particles = []
running = True

while running:
    screen.fill((10, 10, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_x, mouse_y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        for _ in range(5):
            particles.append(Particle(mouse_x, mouse_y))

    for particle in particles[:]:
        particle.update()
        particle.draw(screen)
        if particle.life <= 0 or particle.radius <= 0:
            particles.remove(particle)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
