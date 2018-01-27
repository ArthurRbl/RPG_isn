import pygame
from textures import *

pygame.init()
gameDisplay = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('RPG ISN')
clock = pygame.time.Clock()

crashed = False

#player = pygame.image.load()

for x in range(int(1280/4), int((1280/4)*3), 32):
    for y in range(128, 594, 32):
        gameDisplay.blit(texture.parquet, (x,y))

pygame.display.flip()

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()