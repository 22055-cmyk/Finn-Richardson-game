import sys
import pygame
import random


pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

window_width = 1000
window_height = 750
red = (255, 0, 0)
black = (0, 0, 0)
width = 100
height = 100


screen = pygame.display.set_mode((window_width, window_height))
screen.fill(black)
font = pygame.font.SysFont('Arial', 40)
button_onscreen = pygame.Rect(((window_width - width)/2, (window_height - height)/2), (width, height))



gameloop = True
while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if button.collidepoint(pos):
                print('hit')
                gameloop = False
            else:
                print('no hit')
    button = pygame.draw.rect(screen, red, button_onscreen)
    pygame.display.update()


pygame.quit