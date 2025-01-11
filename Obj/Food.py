import random
import pygame


class Food:
    def __init__(self, size, mapSize, color = (0,0, 200)):
        self.x = random.randrange(0, mapSize, size)
        self.y = random.randrange(0, mapSize, size)
        self.size = size
        self.mapSize = mapSize
        self.color = color

    def GetNew(self):              #selecting random position for food object, concluding that map is a square (not rectangle)
        self.x = random.randrange(0, self.mapSize, self.size)
        self.y = random.randrange(0, self.mapSize, self.size)

    def Draw(self, surface):
        pygame.draw.rect(surface, self.color, [self.x, self.y, self.size, self.size])
