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

def display_score():
    current_time = pygame.time.get_ticks() - int(start_time) #subtracts start time so subtracting ending time = 0
    score_surf = test_font.render(f'{current_time}', False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)
    print(current_time)
pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Firefighting game')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
game_active = True
start_time = 0
                                                                                                   #resized image
player_surf = pygame.transform.scale((pygame.image.load('graphics/firefighter/ff1.png').convert_alpha()),(50,50))
player_rect = player_surf.get_rect(midbottom=(250,250))
#controlling the points in the image, e.g. controlling the placement of midleft point
#draws a rectange around surface, e.g. hitbox

base_surface = pygame.transform.scale((pygame.image.load('graphics/base.png').convert()),(800,400)) #image is new surface

boundary_surface = pygame.Surface((800,100))
boundary_surface.fill('Brown')
boundary_rect = boundary_surface.get_rect(midbottom=(400,450))

fire_surface = pygame.transform.scale((pygame.image.load('graphics/fire.jpg').convert()),(100,100))
fire_rect = fire_surface.get_rect(midbottom=(600,250))



firefighter_x_pos = 600


#test_surface.fill('Red')

while True:
    for event in pygame.event.get(): 
        #existing function that records everything a user does, places actions into event queue
        #then interates through each event one by one to react to each action
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_active:
            if event.type == pygame.MOUSEMOTION:
                if player_rect.collidepoint(event.pos): #mouse collides with player at whatever event
                    print('collision')

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    print("right")
                    player_rect.x += 50
                if event.key == pygame.K_LEFT:
                    print("left")
                    player_rect.x -= 50
                if event.key == pygame.K_UP:
                    print("up")
                    player_rect.y -= 50
                if event.key == pygame.K_DOWN:
                    print("down")
                    player_rect.y += 50
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = pygame.time.get_ticks()
        
    if game_active: 
        screen.blit(base_surface,(0,0)) #we place one surface on top of another
        screen.blit(fire_surface,fire_rect)
        screen.blit(boundary_surface, boundary_rect)
        display_score()
        #pygame.draw.line(screen,'Gold',(0,0),pygame.mouse.get_pos(),10)
                                    #top diagonal
        #firefighter_x_pos -= 1

        if player_rect.right >= 800:
            player_rect.left = 0

        if player_rect.bottom >= boundary_rect.top:
            player_rect.bottom = boundary_rect.top
        
        #player_gravity += 1
        #player_rect.y += player_gravity #changes the y axis
        #if player_rect.bottom >= 300:
        #    player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        # collision
        if fire_rect.colliderect(player_rect):
            game_active = False

    else:
        screen.fill('Yellow')
        
        #keys = pygame.key.get_pressed()
        #if keys[pygame.K_UP]:
        #    print('jump')

        mouse_pos = pygame.mouse.get_pos()
        #if player_rect.collidepoint(mouse_pos):
        #   print('collision')
        #  print(pygame.mouse.get_pressed())
        
    pygame.display.update()
    clock.tick(100) 
    

#NOTES
#using classes and there are specific controls within that specific class
#--> pygame.mouse and pygame.keys

