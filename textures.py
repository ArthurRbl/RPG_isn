import pygame

pygame.init()


class Texture:

    def __init__(self):
        self.texture = ""

    def loadTexture(self, file, size):
        self.texture = pygame.image.load(file)
        #self.texture = pygame.transform.scale(size, size)
        return self.texture

    parquet = loadTexture('parquet.png', 64)


texture = Texture()
