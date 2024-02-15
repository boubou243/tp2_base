import pygame

class Bullet(pygame.sprite.Sprite):
     def __init__(self, left, top, width, height,color,angle):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (left, top)
        self.color=color
        self.angle =angle
        self.left=left
        self.top = top
     def update(self):
         self.rect.center = (self.left, self.top)