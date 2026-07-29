import pygame
import random

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Digital Rain")
font = pygame.font.SysFont("monospace", 15, bold=True)

font_size = 15
columns = width // font_size
drops = [random.randint(0, height // font_size) for _ in range(columns)]

fade_surface = pygame.Surface((width, height))
fade_surface.set_alpha(20)
fade_surface.fill((0, 0, 0))

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(fade_surface, (0, 0))

    for i in range(len(drops)):
        char = chr(random.randint(33, 126))
        color = (0, random.randint(150, 255), 0)
        text = font.render(char, True, color)

        x = i * font_size
        y = drops[i] * font_size

        screen.blit(text, (x, y))

        if y > height and random.random() > 0.97:
            drops[i] = 0

        drops[i] += 1

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
