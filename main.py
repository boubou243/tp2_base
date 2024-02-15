import pygame
import sys
from src.coloredWall import ColoredWall
from src.player import Player
from src.wall import Wall

pygame.init()

# Define colors
BG_COLOR = (153, 178, 178)

# Initialize Pygame
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Create entities
player = Player()
walls = pygame.sprite.Group()

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

blue1 = ColoredWall(200,200,100,100,"Blue")
blue2 = ColoredWall(300,200,100,100,"Blue")

green = ColoredWall(200,400,100,100,"Green")

walls.add(wall1,wall2,red1,red2,blue1,blue2,green)


        
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

    # check for collisions between player and walls
    wall_collisions = pygame.sprite.spritecollide(player, walls, False)
    for wall_collision in wall_collisions:
        print("Collided")

        # fall back to previous position
        player.rect.x = previous_x
        player.rect.y = previous_y
        break

    # draw
    screen.fill((255,255,255),(0,0,200,screen.get_height()))
    screen.fill(BG_COLOR,(200,0,screen.get_width()-200,screen.get_height()))

    # single sprites are drawn with screen.blit()
    screen.blit(player.image, (player.rect.x, player.rect.y))

    # groups of sprites can be drawn with group.draw()
    walls.draw(screen)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()