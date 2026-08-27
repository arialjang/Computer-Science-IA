#/opt/miniconda3/lib/python3.13/site-packages (2.6.1)
#/opt/miniconda3/envs/comsciIA
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

base_surface = pygame.Surface((100,200))
base_surface = pygame.image.load('graphics/base.png')#image is new surface
fire_surface = pygame.image.load('graphics/fire.jpg')
text_surface = test_font.render('My game', False)
#test_surface.fill('Red')

while True:
    for event in pygame.event.get(): 
        #existing function that records everything a user does, places actions into event queue
        #then interates through each event one by one to react to each action
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(base_surface,(0,0)) #we place one surface on top of another
    screen.blit(fire_surface,(0,100))
    pygame.display.update()
    clock.tick(60)