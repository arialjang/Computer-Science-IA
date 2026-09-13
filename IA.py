#/opt/miniconda3/lib/python3.13/site-packages (2.6.1)
#/opt/miniconda3/envs/comsciIA
#conda activate comsciIA
#python3 IA.py
#git status
#git add .
#git commit -m "message"
#git push origin main
import pygame
from sys import exit
pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Firefighting game')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
                                                                                                       #resized image
player_surf = pygame.transform.scale((pygame.image.load('graphics/firefighter/ff1.png').convert_alpha()),(50,50))
player_rect = player_surf.get_rect(midbottom=(250,250))
#controlling the points in the image, e.g. controlling the placement of midleft point
#draws a rectange around surface, e.g. hitbox

base_surface = pygame.transform.scale((pygame.image.load('graphics/base.png').convert()),(800,400)) #image is new surface

fire_surface = pygame.transform.scale((pygame.image.load('graphics/fire.jpg').convert()),(100,100))
fire_rect = fire_surface.get_rect(midbottom=(600,250))

text_surface = test_font.render('My game', False, 'Black')

firefighter_x_pos = 600


#test_surface.fill('Red')

while True:
    for event in pygame.event.get(): 
        #existing function that records everything a user does, places actions into event queue
        #then interates through each event one by one to react to each action
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(base_surface,(0,0)) #we place one surface on top of another
    screen.blit(fire_surface,fire_rect)
    screen.blit(text_surface,(300,50))
    #firefighter_x_pos -= 1
    #if firefighter_x_pos < 0:
    #    firefighter_x_pos = 600

    player_rect.left += 1 #always move rect that contains surface NOT surface.
    screen.blit(player_surf, player_rect)
    

    pygame.display.update()
    clock.tick(100)