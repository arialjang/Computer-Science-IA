#/opt/miniconda3/lib/python3.13/site-packages (2.6.1)
#/opt/miniconda3/envs/comsciIA
#conda activate comsciIA
#python3 IA.py
#git status
#git add .
#git commit -m "message"
#git push origin main
import pygame
import random
from sys import exit

game_active = False

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() #parent class
        self.image = pygame.transform.scale((pygame.image.load('graphics/firefighter/ff1.png').convert_alpha()),(50,50))
        self.rect = self.image.get_rect(midbottom = (200,300))
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.x += 50
        if keys[pygame.K_LEFT]:
            self.rect.x -= 50
        if keys[pygame.K_UP]:
            self.rect.y -= 50
        if keys[pygame.K_DOWN]:
            self.rect.y += 50
    def player_interact(self, obstacle_group):
        for obstacle in obstacle_group:
            if self.rect.colliderect(obstacle.rect):
                global game_active
                game_active = False
    def update(self):
        self.rect.clamp_ip(screen_rect)
        self.player_input()
        self.player_interact(obstacle_group)
    
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__()
        self.image = pygame.transform.scale((pygame.image.load(image_path).convert()),(100,100))
        self.rect = self.image.get_rect(midbottom = (x, y))
   

class Fire(Obstacle):
    def __init__(self, x, y):
        super().__init__(x, y, 'graphics/fire.jpg')

class Rock(Obstacle):
    def __init__(self, x, y):
        super().__init__(x, y,'graphics/rock.png')


def display_score():
    global current_time
    current_time = int(pygame.time.get_ticks() / 1000) - int(start_time) #subtracts start time so subtracting ending time = 0
    score_surf = test_font.render(f'Time: {current_time}', False, (255,255,255))
    score_rect = score_surf.get_rect(center = (300,50))
    screen.blit(score_surf,score_rect)
    return current_time

pygame.init()

screen = pygame.display.set_mode((600, 600))
screen_rect = screen.get_rect()
pygame.display.set_caption('Firefighting game')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
start_time = 0
score = 0

player = pygame.sprite.GroupSingle() #declare player as GroupSingle variable
player.add(Player())
base_surface = pygame.transform.scale((pygame.image.load('graphics/base.png').convert()),(600,600)) #image is new surface

#boundary_surface = pygame.Surface((800,100))
#boundary_surface.fill('Brown')
#boundary_rect = boundary_surface.get_rect(midbottom=(400,450))

game_name = test_font.render('Firefighting game', False, (111,196,169))
game_name_rect = game_name.get_rect(center = (300, 200))

game_message = test_font.render('Press space to start', False, (111,196,169))
game_message_rect = game_message.get_rect(center = (300,400))

while True:
    for event in pygame.event.get(): 
        
        #existing function that records everything a user does, places actions into event queue
        #then interates through each event one by one to react to each action
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            player.sprite.rect.midbottom = (200,300)
            game_active = True
            start_time = (pygame.time.get_ticks() / 1000)

    if game_active: 
        screen.blit(base_surface,(0,0)) #we place one surface on top of another
        
        #screen.blit(boundary_surface, boundary_rect)
        score = display_score()
        #pygame.draw.line(screen,'Gold',(0,0),pygame.mouse.get_pos(),10)
                                    #top diagonal
        
        #player_rect.y += player_gravity #changes the y axis
        #if player_rect.bottom >= 300:
        #    player_rect.bottom = 300
        obstacle_group = pygame.sprite.Group()
        obstacle_group.add(Fire(100,100))
        obstacle_group.add(Fire(300,300))
        obstacle_group.add(Rock(150,150))
        obstacle_group.add(Rock(50,50))

        player.draw(screen)
        player.update()
        obstacle_group.draw(screen)
        obstacle_group.update()
    else:
        screen.fill('Yellow')
        screen.blit(game_name, game_name_rect)
        score_message = test_font.render(f'Your time: {score}', False, (111,196,169))
        score_message_rect = score_message.get_rect(center = (300,400))
        
        if score == 0:
            screen.blit(game_message, game_message_rect)
        else: 
            screen.blit(score_message, score_message_rect)

        mouse_pos = pygame.mouse.get_pos()
        #if player_rect.collidepoint(mouse_pos):
        #   print('collision')
        
    pygame.display.update()
    clock.tick(100) 
    

#NOTES
#using classes and there are specific controls within that specific class
#--> pygame.mouse and pygame.keys

