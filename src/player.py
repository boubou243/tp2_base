import math
import pygame

from src.bullet import Bullet 

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./assets/tank.png')
        self.rect = self.image.get_rect()
        self.rect.center = (248, 149)
        self.speed = 6
        self.angle = 0
        self.rotation_speed=6
        self.bullets =[]
        self.bullet_speed=5
        self.wait_time =200
        self.last_input_time =0
        self.nbr_red_bullets = 2
        self.nbr_green_bullets = 0
        self.nbr_blue_bullets = 0


    def update(self):
        print(self.nbr_red_bullets)
        print(self.nbr_green_bullets)
        print(self.nbr_blue_bullets)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or  keys[pygame.K_a] :
            self.rotate(self.rotation_speed)
        if keys[pygame.K_RIGHT] or  keys[pygame.K_d]:
            self.rotate(-self.rotation_speed)
        if keys[pygame.K_UP] or  keys[pygame.K_w]:
            self.move_forward()
        if keys[pygame.K_DOWN] or  keys[pygame.K_s]:
             self.move_backward()
        current_time = pygame.time.get_ticks()
        if current_time - self.last_input_time > self.wait_time:
                          
            self.last_input_time = current_time
            
            if keys[pygame.K_z] and self.nbr_red_bullets > 0  :
                bullet = Bullet(self.rect.center[0],self.rect.center[1],5,5,pygame.Color('red'),self.angle)
                self.bullets.append(bullet)
                self.nbr_red_bullets-=1
            if keys[pygame.K_x] and self.nbr_green_bullets> 0 :
                bullet = Bullet(self.rect.center[0],self.rect.center[1],5,5,pygame.Color('green'),self.angle)
                self.bullets.append(bullet)
                self.nbr_green_bullets -= 1
            if keys[pygame.K_c] and self.nbr_blue_bullets> 0 :
                bullet = Bullet(self.rect.center[0],self.rect.center[1],5,5,pygame.Color('blue'),self.angle)
                self.bullets.append(bullet)
                self.nbr_blue_bullets -=1
        



    

    def rotate(self, angle_change):
        self.angle += angle_change
        
    def move_forward(self):
        self.rect.x += self.speed * math.cos(math.radians(self.angle))
        self.rect.y -= self.speed * math.sin(math.radians(self.angle))
        
    def move_backward(self):
        self.rect.x -= self.speed * math.cos(math.radians(self.angle))
        self.rect.y += self.speed * math.sin(math.radians(self.angle))

    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        rotated_rect = rotated_image.get_rect(center=self.image.get_rect(topleft=(self.rect.x, self.rect.y)).center)
        screen.blit(rotated_image, rotated_rect)
        
        for bullet in self.bullets:
         #   pygame.draw.rect(screen,bullet.color,bullet)
            screen.blit(bullet.image,bullet.rect)

        for bullet in self.bullets:
            bullet.left+= self.bullet_speed * math.cos(math.radians(bullet.angle))
            bullet.top -= self.bullet_speed * math.sin(math.radians(bullet.angle))
            bullet.update()
            