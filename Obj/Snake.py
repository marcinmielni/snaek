import random
import pygame


class Snake:
    def __init__(self, x, y, segmentSize, color = (255, 255, 255)):
        self.x = x                    #head coordinates
        self.y = y
        self.segmentSize = segmentSize
        self.len = 1
        self.color = color
        self.segments = []
        self.segments.append((x, y))
        #self.direction = (0,0)

    def add(tupleA, tupleB):
            x = tupleA[0] + tupleB[0]
            y = tupleA[1] + tupleB[1]
            return (x, y)

    def Draw(self, surface):
        for x in self.segments[::-1]:
            pygame.draw.rect(surface, self.color, [x[0], x[1], self.segmentSize,self.segmentSize])

    '''def ChangeDirection(self, x, y):
        self.direction = (x, y)'''

    def Eat(self):
        self.len += 1

    def Move(self, direction):
        self.segments = self.segments[:] + [Snake.add(self.segments[-1], direction)]
        if self.len < len(self.segments):
            del self.segments[0]
        self.x = self.segments[-1][0]
        self.y = self.segments[-1][1]

    def isCollision(self):
        head = self.segments[-1]
        for seg in self.segments[:-1]:
            if head == seg:
                return True
        return False