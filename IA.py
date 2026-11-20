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
import numpy as np

game_active = False
pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, image_name):
        super().__init__() #parent class
        self.image = pygame.transform.scale((pygame.image.load(f'graphics/firefighters/{image_name}').convert_alpha()),(50,50))
        #required attribute for sprite
        self.rect = self.image.get_rect(topleft = (100, 500))
    def set_image(self, image_name): 
        self.image = pygame.transform.scale((pygame.image.load(f'graphics/firefighters/{image_name}').convert_alpha()),(50,50))
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def player_interact(self, obstacle_group):
        for obstacle in obstacle_group:
            if self.rect.colliderect(obstacle.rect):
                if isinstance(obstacle, Fire):
                    global game_active
                    game_active = False

    def update(self):
        self.rect.clamp_ip(player_area_rect.inflate(-100, -100))
        self.player_interact(obstacle_group)
    
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__()
        self.image = pygame.transform.scale((pygame.image.load(image_path).convert()),(50,50))
        self.rect = self.image.get_rect(topleft = (x, y))
   
class Fire(Obstacle):
    def __init__(self, x, y):
        super().__init__(x, y, 'graphics/fire.jpg')

class House(Obstacle):
    def __init__(self, x, y):
        super().__init__(x, y,'graphics/house.png')

def display_score():
    global current_time
    current_time = int(pygame.time.get_ticks() / 1000) - int(start_time) #subtracts start time so subtracting ending time = 0
    score_surf = main_font.render(f'Time: {current_time}', False, (255,255,255))
    score_rect = score_surf.get_rect(center = (300,25))
    screen.blit(score_surf,score_rect)
    return current_time

screen = pygame.display.set_mode((1200, 600))
player_area_rect = pygame.Rect(0, 0, 600, 600) #player is bound to left half
screen_rect = screen.get_rect()
pygame.display.set_caption('Firefighting game')
clock = pygame.time.Clock()
main_font = pygame.font.Font(None, 50)
sub_font = pygame.font.Font(None, 40)
start_time = 0
score = 0
timeLimit = 100

player = pygame.sprite.GroupSingle() #declare player as GroupSingle variable
player.add(Player('default.png'))
base_surface = pygame.transform.scale((pygame.image.load('graphics/base.png').convert()),(600,600)) 

def low_visibility(screen, player_rect):
    px, py = player_rect.topleft
    for x in range(0, 600, 50): #checks every 50 blocks
        for y in range(0, 600, 50):
            distance_x = abs(x - px)
            distance_y = abs(y - py)

            if distance_x > 50 or distance_y > 50: #one block radius
                pygame.draw.rect(screen, (15, 15, 15), (x, y, 50, 50))
                #draws dark gray rgb on x,y top left corner

house_coords = []
fire_coords = []
agent_pos = [50,500]

def generate_obstacle():
    global house_coords, fire_coords, agent_pos
    houseCount = 5
    fireCount = 5

    obstacle_group.empty()
    house_coords.clear()
    fire_coords.clear()

    player_spawn_pos = (50, 500)
    player.sprite.rect.topleft = player_spawn_pos
    agent_pos = player_spawn_pos


    occupied = {player_spawn_pos, (50, 450, (100, 500))}
    reserved_count = len(occupied)

    while len(occupied) < reserved_count + houseCount:
        obstacle_x = (random.randint(1, 10)) * 50
        obstacle_y = (random.randint(1, 10)) * 50
        if (obstacle_x, obstacle_y) not in occupied:
            occupied.add((obstacle_x, obstacle_y))
            house_coords.append((obstacle_x, obstacle_y))
            obstacle_group.add(House(obstacle_x, obstacle_y))

    while len(occupied) < reserved_count + fireCount + houseCount:
        obstacle_x = (random.randint(1, 10)) * 50
        obstacle_y = (random.randint(1, 10)) * 50
        if (obstacle_x, obstacle_y) not in occupied:
            occupied.add((obstacle_x, obstacle_y))
            fire_coords.append((obstacle_x, obstacle_y))
            obstacle_group.add(Fire(obstacle_x,obstacle_y))

ff_selection = ['default.png','arial.png','aurora.png', 'giulia.png', 'carly.png']
ff_index = 0
player_present = pygame.transform.scale((pygame.image.load(f'graphics/firefighters/{ff_selection[0]}').convert_alpha()),(300,300)) 
player_present_rect = player_present.get_rect(center = (300, 300))

def player_selection(): #carousel display
    global ff_index, player_present #declare as global
    if not game_active and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #left click
            if left_player_rect.collidepoint(event.pos):
                ff_index = (ff_index - 1) % len(ff_selection)
                player_present = pygame.transform.scale((pygame.image.load(f'graphics/firefighters/{ff_selection[ff_index]}').convert_alpha()),(300,300)) 
   
    if not game_active and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #left click
            if right_player_rect.collidepoint(event.pos):
                ff_index = (ff_index + 1) % len(ff_selection)
                player_present = pygame.transform.scale((pygame.image.load(f'graphics/firefighters/{ff_selection[ff_index]}').convert_alpha()),(300,300)) 

def draw_rl_screen():
    offset_X = 600
    screen.blit(base_surface)


left_player = pygame.transform.scale((pygame.image.load(f'graphics/buttons/left_arrow.png').convert_alpha()),(100,100))
left_player_rect = left_player.get_rect(center = (100, 300))

right_player = pygame.transform.scale((pygame.image.load(f'graphics/buttons/right_arrow.png').convert_alpha()),(100,100))
right_player_rect = right_player.get_rect(center = (500, 300))

game_name = main_font.render('Firefighting game', False, (255,0,0))
game_name_rect = game_name.get_rect(center = (300, 50))

choose_player = sub_font.render('Choose your player', False, (200,0,0))
choose_player_rect = choose_player.get_rect(center=(300, 100))

game_message = main_font.render('Press space to start', False, (255,0,0))
game_message_rect = game_message.get_rect(center = (300,500))

obstacle_group = pygame.sprite.Group() #empty container for sprites

#RUN BEFORE GAME STARTS
generate_obstacle()


while True:
    for event in pygame.event.get(): 
        #existing function that records everything a user does, places actions into event queue
        #then interates through each event one by one to react to each action
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            player.sprite.set_image(ff_selection[ff_index])
            player.sprite.rect.topleft = (50,500)
            game_active = True
            start_time = (pygame.time.get_ticks() / 1000)

        if event.type == pygame.KEYDOWN and game_active:
            if  event.key == pygame.K_RIGHT:
                player.sprite.move(50, 0)
            elif event.key == pygame.K_LEFT:
                player.sprite.move(-50, 0)
            elif event.key == pygame.K_UP: 
                player.sprite.move(0, -50)
            elif event.key == pygame.K_DOWN:
                player.sprite.move(0, 50)
        player_selection()
    
    if game_active: #things that happen continuously
        screen.blit(base_surface,(0,0)) #we place one surface on top of another
       
        #OBSTACLE
        obstacle_group.draw(screen)
        obstacle_group.update()

        #PLAYER
        player.update()
        player.draw(screen)

        low_visibility(screen, player.sprite.rect)

        score = display_score() #surfaces appear based on order
        if score > timeLimit:
            game_active = False

    else:
        screen.fill('Yellow')
        screen.blit(game_name, game_name_rect)
        score_message = main_font.render(f'Your time: {score}', False, (255,0,0))
        score_message_rect = score_message.get_rect(center = (300,400))
        if score > timeLimit: #DOESNT WORK IDK WHY-------------------------------------
            time_limit = main_font.render(f'You ran out of time!', False, (255,0,0))
            time_limit_rect = time_limit.get_rect(center = (300,200))
        
        if score == 0:
            screen.blit(choose_player, choose_player_rect)
            screen.blit(player_present, player_present_rect)
            screen.blit(game_message, game_message_rect)
            screen.blit(left_player, left_player_rect)
            screen.blit(right_player, right_player_rect)

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

