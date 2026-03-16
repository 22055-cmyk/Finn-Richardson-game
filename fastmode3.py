import sys
import pygame
import random


pygame.init()

#This is how many times the screen updates every second
fps = 60
fpsClock = pygame.time.Clock()

window_width = 1000
window_height = 750
screen = pygame.display.set_mode((window_width, window_height))
font = pygame.font.Font(None, 36)
screen_colour = (0, 0, 0)

class Buttons:
    """this code creates a button blueprint
    
    This code makes a button that can have custom, x and y position, size, what is displayed on it, what happens when its pressed and the colours you want to use.
    I will use this code to make buttons for my games menus, which will have lots of different colours, functions and looks.
    I am using this code because it makes the process of making buttons very easy because I don't have to retype all this code everytime I want a new button.

    this code changes
    -The menu screen to the game screen
    -Whether you enter the game or leave the game
    """

    def __init__(self, x, y, onclickFunction):
        #Gets the position of button
        
        self.onclickFunction = onclickFunction

    def draw(self, surface):
        #This line draws the rect using what surface to put it on, defined when in the main loop, the colour and dimensions defined when using the class
        pygame.image.load('exit button pixel.png').convert_alpha()
        
        image_rect = my_image.get_rect()
        image_rect.center = 
        surface.blit(my_)
        
        

    def check_click(self, pos):
        #Checks if mouse is over the button
        if self.rect.collidepoint(pos):
            #Checks whether onclickfunction has been defined in the class blueprint
            if self.onclickFunction:
                #Then it does the function defined below
                self.onclickFunction()

#These are the definitions 
def Exit():
    #If you use exit function then the game will exit.
    pygame.quit()
    sys.exit()
    
def Game():
    
    game_screen = True
    while game_screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_screen = False
                pygame.quit()
        screen.fill(screen_colour)
        pygame.display.update()    


#Setting all the positions to be changable if i chaange the window size of want to quickly change the size of the button themselves
#(x, y, width, height, text, difficulty, onclickFunction, rect_colour, text_colour)
ExitButton = Button(((window_width - 100)*1/3), ((window_height - 60)/2), 100, 60, "exit", Exit, 'red', 'white')
PlayButton = Button(((window_width - 100)*2/3), ((window_height - 60)/2), 100, 60, 'play', Game, 'green', 'white')



game_loop = True
while game_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            ExitButton.check_click(event.pos)
            PlayButton.check_click(event.pos)
    ExitButton.draw(screen)
    PlayButton.draw(screen)
    pygame.display.update()
