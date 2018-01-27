import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('RPG ISN')
clock = pygame.time.Clock()

crashed = False

parquet = pygame.image.load('parquet64.png')
player = pygame.image.load('player/player_down0.png').convert_alpha()

for x in range(int(1280/4), int((1280/4)*3), 64):
    for y in range(128, 594, 64):
        gameDisplay.blit(parquet, (x, y))

gameDisplay.blit(player, (1280/2, 720/2))

pygame.display.flip()
pygame.mixer.music.load('sound/SEQ_OPENING.sseq.mp3')
pygame.mixer.music.play(0)

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                gameDisplay.blit(parquet, (1280/2, 720/2+24))
                gameDisplay.blit(parquet, (1280 / 2, 720 / 2 - 40))
                player = pygame.image.load('player/player_up0.png').convert_alpha()
                gameDisplay.blit(player, (1280 / 2, 720 / 2))
            if event.key == pygame.K_s:
                gameDisplay.blit(parquet, (1280 / 2, 720 / 2 + 24))
                gameDisplay.blit(parquet, (1280 / 2, 720 / 2 - 40))
                player = pygame.image.load('player/player_down0.png').convert_alpha()
                gameDisplay.blit(player, (1280 / 2, 720 / 2))
            if event.key == pygame.K_a:
                gameDisplay.blit(parquet, (1280 / 2, 720 / 2 + 24))
                gameDisplay.blit(parquet, (1280 / 2, 720 / 2 - 40))
                player = pygame.image.load('player/player_left0.png').convert_alpha()
                gameDisplay.blit(player, (1280 / 2, 720 / 2))
            if event.key == pygame.K_d:
                gameDisplay.blit(parquet, (1280 / 2, 720 / 2 + 24))
                gameDisplay.blit(parquet, (1280 / 2, 720 / 2 - 40))
                player = pygame.image.load('player/player_right0.png').convert_alpha()
                gameDisplay.blit(player, (1280 / 2, 720 / 2))

        print(event)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
