import pygame
import sys

pygame.init()
size = (510,510)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")

width = height = 40
red = (255, 255, 255)
margin = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    for col in range(10):
        for row in range(10):
            x = col * width + (col + 1) * margin
            y = row * height + (row + 1) * margin
            pygame.draw.rect(screen, red, (x,y, width, height))
    pygame.display.update()
