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
screen_colour = (0, 0, 0)

class Button:
    """this code creates a button blueprint
    
    This code makes a button that can have custom, x and y position, size, what is displayed on it, what happens when its pressed and the colours you want to use.
    I will use this code to make buttons for my games menus, which will have lots of different colours, functions and looks.
    I am using this code because it makes the process of making buttons very easy because I don't have to retype all this code everytime I want a new button.

    this code changes
    -The menu screen to the game screen
    -Whether you enter the game or leave the game
    """

    def __init__(self, x, y, image_path, onclickFunction):
        
        #Gets the image
        self.image = pygame.image.load(image_path).convert_alpha()
        #Makes the image 
        self.rect = self.image.get_rect(center=(x, y))
        self.onclickFunction = onclickFunction

    def draw(self, surface):
        #This draws the image you want onto the surface you specify when drawing the image.
        
        surface.blit(self.image, self.rect)

    def check_click(self, pos):
        #Checks if mouse is over the button
        if self.rect.collidepoint(pos):
            #Checks whether onclickfunction has been defined in the class blueprint
            if self.onclickFunction:
                #Then it does the function defined below
                self.onclickFunction()

#These are the definitions 
def Game():
    #Creates Game loop
    game_screen = True
    while game_screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_screen = False
                pygame.quit()
        screen.fill(screen_colour)
        pygame.display.update()    

def Exit():
    #If you use exit function then the game will exit.
    print("exit")
    pygame.quit()




#Setting all the positions to be changable if i chaange the window size of want to quickly change the size of the button themselves
#(x, y, width, height, text, difficulty, onclickFunction, rect_colour, text_colour)
ExitButton = Button(((window_width * 1)/3), (window_height/2), 'exitbutton.png', Exit)
PlayButton = Button(((window_width * 2)/3), (window_height/2), 'playbutton.png', Game)

class Obstacle:
    """This code places the obstacles
    
    This code checks the size of the window and chooses a random space inside the window to place a specific obstacle type
    """
    def __init__(self, obstacle):
        #This calls 
        self.obstacle = obstacle
        self.rand_x = rand_x
        self.rand_y = rand_y
        rand_x = random.randit(0, (window_width / 50))
        rand_y = random.randit(0, (window_height / 50))
    def Place(self, surface):
        surface.blit(self.obstacle, center=(self.rand_x, self.rand_y))
        if self.obstacle:
            self.obstacle()

def Wall():
    place_walls_loop = True
    while place_walls_loop:
        number_of_walls = 0
        max_walls = 25
        if number_of_walls < max_walls:
            print("can place walls")
            place_walls_loop = False
        else:
            place_walls_loop = False

def Void():
    place_void_loop = True
    while place_void_loop:
        number_of_void = 0
        max_void = 25
        if number_of_void < max_void:
            print("can place void")
            place_void_loop = False
        else:
            place_void_loop = False

def Star():
    place_stars_loop = True
    while place_stars_loop:
        number_of_stars = 0
        max_stars = 25
        if number_of_stars < max_stars:
            print("can place stars")
            place_stars_loop = False
        else:
            place_stars_loop = False



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
