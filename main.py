import pygame
import sys
from src.coloredWall import ColoredWall
from src.player import Player
from src.wall import Wall
from src.collectibles import Collectibles
from src.sortie import Sortie


pygame.init()

ammo_font = pygame.font.SysFont(None, 60)
sortie_font = pygame.font.SysFont(None, 20)


bullets = []



def display_number(bulletCounts, letters, colors, x, y):
    #affiche les balles restantes selon la couleurs
    for i, number in enumerate(bulletCounts):
        number_surface = ammo_font.render(str(number), True, BLACK)
        number_rect = number_surface.get_rect()
        number_rect.topleft = (x, y + i * ammo_font.get_height())
        screen.blit(number_surface, number_rect)
    #affiche les caractère pour les balles du tank
    for i, (letter, color) in enumerate(zip(letters, colors)):
        letter_surface = ammo_font.render(letter, True, color)
        letter_rect = letter_surface.get_rect()
        letter_rect.topleft = (x + 100, y + i * ammo_font.get_height())
        screen.blit(letter_surface, letter_rect)
    j=0
    #affiche les lettres pour la zone de sortie
    for caracter in ['S','O','R','T','I','E']:

        sortie_surface =sortie_font.render(caracter,True,pygame.Color('red'))
        sortie_rect = sortie_surface.get_rect()
        sortie_rect.topleft =(210+ j*sortie_font.get_height() ,340 )
        screen.blit(sortie_surface,sortie_rect)
        j=j+1


     

# Define colors
BG_COLOR = (153, 178, 178)
BLACK = (0,0,0)
# Initialize Pygame
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Create entities
player = Player()
#bullet = Bullet(player.rect.center[0],player.rect.center[1],5,5,pygame.Color('red'))
#bullets.append(bullet)
walls = pygame.sprite.Group()
redWall1 = pygame.sprite.Group()
redWall2 = pygame.sprite.Group()
greenWalls = pygame.sprite.Group()
blueWall1 = pygame.sprite.Group()
blueWall2 = pygame.sprite.Group()
sortie_box = pygame.sprite.Group()

green_ammo_box = pygame.sprite.Group()
blue_ammo_box = pygame.sprite.Group()
for x in range(6):
    if(x!=5):
        walls.add(Wall(100*x+200,0,100,100))
    if(x !=2 and x !=3):
        walls.add(Wall(100*x+200,200,100,100))
        walls.add(Wall(100*x+200,500,100,100))
wall1= Wall(300,300,100,100)
wall2= Wall(600,300,100,100)

red1 = ColoredWall(600,100,100,100,"Red")
red2 = ColoredWall(600,400,100,100,"Red")

blue1 = ColoredWall(400,200,100,100,"Blue")
blue2 = ColoredWall(500,200,100,100,"Blue")

green = ColoredWall(300,400,100,100,"Green")

blue_ammo = Collectibles(50,50,pygame.Color('blue'))
blue_ammo.rect.topleft=(725,25)

green_ammo = Collectibles(50,50,pygame.Color('green'))
green_ammo.rect.topleft=(725,325)

green_ammo_box.add(green_ammo)
blue_ammo_box.add(blue_ammo)

sortie = Sortie(96,96,(200,122,122))
sortie.rect.topleft=(200,300)

sortie_box.add(sortie)



walls.add(wall1,wall2,red1,red2,blue1,blue2,green)
redWall1.add(red1)
redWall2.add(red2)
blueWall1.add(blue1)
blueWall2.add(blue2)
greenWalls.add(green)

green_ammo_destroy=False
blue_ammo_destroy=False
        
#wall0 = Wall(0, 0, 50, 50)
#wall1 = Wall(500, 150, 100, 100)
#wall2 = Wall(250, 50, 100, 100)

# Main game loop
playing = True
while playing:

  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

  
    # before player update
    previous_x = player.rect.x
    previous_y = player.rect.y

    # player update 
    player.update()
     
    for bullet in player.bullets:
        bulletRemoved = False

        red_bullet_collision1= pygame.sprite.spritecollide(bullet, redWall1, False)
        red_bullet_collision2= pygame.sprite.spritecollide(bullet, redWall2, False)

        green_bullet_collisions= pygame.sprite.spritecollide(bullet, greenWalls, False)
        
        blue_bullet_collision1= pygame.sprite.spritecollide(bullet, blueWall1, False)
        blue_bullet_collision2= pygame.sprite.spritecollide(bullet, blueWall2, False)
        bullet_collisions = pygame.sprite.spritecollide(bullet, walls, False)

        for bullet_collision in red_bullet_collision1:
            if(bullet.color ==pygame.Color('red')):
                player.bullets.remove(bullet)
                walls.remove(red1)
                bulletRemoved = True
        for bullet_collision in red_bullet_collision2:
            if(bullet.color ==pygame.Color('red')):
                player.bullets.remove(bullet)
                walls.remove(red2)
                bulletRemoved = True
        for bullet_collision in blue_bullet_collision1:
            if(bullet.color ==pygame.Color('blue')):
                player.bullets.remove(bullet)
                walls.remove(blue1)
                bulletRemoved = True
        for bullet_collision in blue_bullet_collision2:
            if(bullet.color ==pygame.Color('blue')):
                player.bullets.remove(bullet)
                walls.remove(blue2)
                bulletRemoved = True
        for bullet_collision in green_bullet_collisions:
            if(bullet.color ==pygame.Color('green')):
                player.bullets.remove(bullet)
                walls.remove(green)
                bulletRemoved = True
        for bullet_collision in bullet_collisions:
            if(not bulletRemoved):
                player.bullets.remove(bullet)
                
   
        
        


    # check for collisions between player and walls
    wall_collisions = pygame.sprite.spritecollide(player, walls, False)

    green_ammo_box_collisions = pygame.sprite.spritecollide(player, green_ammo_box, False)
    blue_ammo_box_collisions = pygame.sprite.spritecollide(player, blue_ammo_box, False)

    sortie_collissions = pygame.sprite.spritecollide(player, sortie_box, False)

   
    for box_collision in green_ammo_box_collisions:
        player.nbr_green_bullets+=1
        green_ammo.kill()
        green_ammo_destroy=True
        break
    
    for box_collision in blue_ammo_box_collisions:
        player.nbr_blue_bullets+=1
        blue_ammo.kill()
        blue_ammo_destroy=True
        break
    
    for wall_collision in wall_collisions:
        print("Collided")

        # fall back to previous position
        player.rect.x = previous_x
        player.rect.y = previous_y
        break

    for sortie_collision in sortie_collissions:
        pygame.quit()

    # draw
    screen.fill((255,255,255),(0,0,200,screen.get_height()))


    screen.fill(BG_COLOR,(200,0,screen.get_width()-200,screen.get_height()))

    # single sprites are drawn with screen.blit()
   # screen.blit(player.image, (player.rect.x, player.rect.y))

    player.draw(screen)

    # groups of sprites can be drawn with group.draw()
    walls.draw(screen)
    
    
    #screen.blit(sortie.image,sortie.rect)

    display_number([player.nbr_red_bullets,player.nbr_green_bullets,player.nbr_blue_bullets],['R','V','B'],[pygame.Color('red'),pygame.Color('green'),pygame.Color('blue')],0,0)
    if(not green_ammo_destroy):
        screen.blit(green_ammo.image,green_ammo.rect)
    if(not blue_ammo_destroy):  
        screen.blit(blue_ammo.image,blue_ammo.rect)
    
    
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()