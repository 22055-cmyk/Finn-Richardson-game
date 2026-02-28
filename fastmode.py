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
white = (255, 255, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
purple = (128, 0, 128)
orange = (255, 165, 0)
screen = pygame.display.set_mode((window_width, window_height))
font = pygame.font.Font(None, 36)

class Button:
    def __init__(self, x, y, width, height, text, rect_colour=None, text_colour=None, onclickFunction=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.rect_colour = rect_colour
        self.text_colour = text_colour
        self.onclickFunction = onclickFunction

    def draw(self, surface):
        pygame.draw.rect(surface, self.rect_colour, self.rect)
        text_surface = font.render(self.text, True, self.text_colour)
        text_rect = text_surface.get_rect(center = self.rect.center)
        surface.blit(text_surface, text_rect)

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            if self.onclickFunction:
                self.onclickFunction()

def exit():
    pygame.quit()
    sys.exit()

def play():
    gameloop = True
    while gameloop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameloop = False
        screen.fill(black)
        pygame.display.update()
    pygame.quit()






#button_rect = pygame.Rect(((window_width - width)/2, (window_height - height)/2), (width, height))
#button_text = font.render("exit", True, white)
#text_rect = button_text.get_rect(center = button_rect.center)
#button = pygame.draw.rect(screen, red, button_rect)
#screen.blit(button_text, text_rect)


ExitButton = Button(100, 100, 100, 100, "exit", exit)
PlayButton = Button(300, 300, 100, 100, 'play', play, green)

startmenu = True
while startmenu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            startmenu = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            ExitButton.check_click(event.pos)
            PlayButton.check_click(event.pos)
    ExitButton.draw(screen)
    PlayButton.draw(screen)
    pygame.display.update()
pygame.quit