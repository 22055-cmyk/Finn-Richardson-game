import sys
import pygame
import random


pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

window_width = 1000
window_height = 750
screen = pygame.display.set_mode((window_width, window_height))
font = pygame.font.Font(None, 36)
screen_colour = (0, 0, 0)

class Button:
    """this code creates a button blueprint
    
    This code makes a button that can have custom, x and y position, size, what is displayed on it, what happens when its pressed and the colours you want to use.
    I will use this code to make buttons for my games menus, which will have lots of different colours, functions and looks.
    I am using this code because it makes the process of making buttons very easy because I don't have to retype all this code everytime I want a new button.

    thus code changes
    -cghdfhdfghdg
    -dgfdfhgfhgfh
    -gfjdf-hgfhdhcgj
    
    """
    # A class attribute dictionary, of the colours available
    colours = {
            'red': '#FF0000',
            'black': '#000000',
            'white': '#FFFFFF',
            'green': '#008000',
            'yellow': '#FFFF00',
            'blue': '#0000FF',
            'purple': '#9D00FF',
            'orange': '#FFA500',
        }
    def __init__(self, x, y, width, height, text, onclickFunction, rect_colour, text_colour):
        #Gets the dimensions for the button size and position
        self.rect = pygame.Rect(x, y, width, height)
        #Text on the button
        self.text = text
        #These lines of code check whether you have defined a colour from the dictionary if so it will set the colour of the rect or text to the definition
        self.rect_colour = self.colours.get(rect_colour)
        self.text_colour = self.colours.get(text_colour)
        self.rect_colour = rect_colour
        self.text_colour = text_colour
        #This defines what will happen when the button is clicked
        self.onclickFunction = onclickFunction
        #Changing shape to either rect or circle

    def draw(self, surface):
        #This line draws the rect using what surface to put it on, defined when in the main loop, the colour and dimensions defined when using the class
        pygame.draw.rect(surface, self.rect_colour, self.rect)
        text_surface = font.render(self.text, True, self.text_colour)
        text_rect = text_surface.get_rect(center = self.rect.center)
        surface.blit(text_surface, text_rect)

    def check_click(self, pos):
        #Checks if mouse is over the button
        if self.rect.collidepoint(pos):
            #Checks whether onclickfunction has been defined in the class blueprint
            if self.onclickFunction:
                #Then it does the function defined below
                self.onclickFunction()

#These are the definitions 
def exit():
    #If you use exit function then the game will exit.
    pygame.quit()
    sys.exit()

def SelectDifficultyMenu():
    selectdifficultymenu_loop = True
    while selectdifficultymenu_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                selectdifficultymenu_loop = False
                pygame.quit()
        #This is to make the screen black, removing the buttons from the start menu.
        if selectdifficultymenu_loop = True:
            screen.fill(screen_colour)
            OrbButton.draw(screen)
            DifficultyOne.draw(screen)
            DifficultyTwo.draw(screen)
            DifficultyThree.draw(screen)
            DifficultyFour.draw(screen)
            DifficultyFive.draw(screen)
            pygame.display.update()
        else:
            

def Game():
    
    game_loop = True
    while game_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_loop = False
                pygame.quit()
        if Button.onclickFunction(DifficultyOne):
            difficulty = 1
            print (f'{difficulty}')
            screen.fill(screen_colour)
            pygame.display.update()


#button_rect = pygame.Rect(((window_width - width)/2, (window_height - height)/2), (width, height))
#button_text = font.render("exit", True, white)
#text_rect = button_text.get_rect(center = button_rect.center)
#button = pygame.draw.rect(screen, red, button_rect)
#screen.blit(button_text, text_rect)



#Setting all the positions to be changable if i chaange the window size of want to quickly change the size of the button themselves
dif_width = 100
dif_height = 60
DifficultyOne = Button((((window_width - dif_width)/2)-(dif_width * 3)), ((window_height - dif_height)/2), dif_width, dif_height, "1 Orb", Game, "yellow", "black")
DifficultyTwo = Button((((window_width - dif_width)/2)-(dif_width * 1.5)), ((window_height - dif_height)/2), dif_width, dif_height, "2 Orbs", None, "yellow", "black")
DifficultyThree = Button(((window_width - dif_width)/2), ((window_height - dif_height)/2), dif_width, dif_height, "3 Orbs", None, "yellow", "black")
DifficultyFour = Button((((window_width - dif_width)/2)+(dif_width * 1.5)), ((window_height - dif_height)/2), dif_width, dif_height, "4 Orbs", None, "yellow", "black")
DifficultyFive = Button((((window_width - dif_width)/2)+(dif_width * 3)), ((window_height - dif_height)/2), dif_width, dif_height, "5 Orbs", None, "yellow", "black")

OrbButton = Button(((window_width - 250)/2), ((window_height - 60)*1/3), 250, 60, 'Choose Difficulty', None, 'yellow', 'black')
ExitButton = Button(((window_width - 100)*1/3), ((window_height - 60)/2), 100, 60, "exit", exit, 'red', 'white')
PlayButton = Button(((window_width - 100)*2/3), ((window_height - 60)/2), 100, 60, 'play', SelectDifficultyMenu, 'green', 'white')

startmenu_loop = True
while startmenu_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            startmenu_loop = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            ExitButton.check_click(event.pos)
            PlayButton.check_click(event.pos)
    ExitButton.draw(screen)
    PlayButton.draw(screen)
    pygame.display.update()
pygame.quit