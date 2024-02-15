import pygame
from src.wall import Wall


class ColoredWall(Wall):
     def __init__(self, x, y, width, height,color):
        super().__init__(x, y, width, height)
        if(color == "Red"):
            self.image = pygame.image.load('./assets/red.png')
        if(color == "Blue"):
            self.image = pygame.image.load('./assets/blue.png')
        if(color == "Green"):
            self.image = pygame.image.load('./assets/green.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y