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
        #Draws the obstacle class by generating random position and placing in random position.
        Wall.draw(screen)
        pygame.display.update()        
        
def Exit():
    #If you use exit function then the game will exit.
    print("exit")
    pygame.quit()




#Setting all the positions to be changable if i chaange the window size of want to quickly change the size of the button themselves
#(x, y, width, height, text, difficulty, onclickFunction, rect_colour, text_colour)
ExitButton = Button(((window_width * 1)/3), (window_height/2), 'exitbutton.png', Exit)
PlayButton = Button(((window_width * 2)/3), (window_height/2), 'playbutton.png', Game)

class Obstacles:
    """THis code creates a grid of 1's and 0's and will randomly place a wall in one of the grid segments
    This class is
    """
    def __init__ (self, type, image_path):
        #Checks what type of obstacle i will be placing.
        self.type = type
        
        #Defines the size of the grid, the dimensions of the window divided by 50.
        grid_width = 20
        grid_height = 15
        
        #Draws the grid of 0's to the size of the gri defined.
        grid = [[0 for _ in range(grid_width)] for _ in range(grid_height)]
        
        #Generates a random position to place a 1 in the grid.
        x = random.randint(0, grid_width - 1)
        y = random.randint(0, grid_height - 1)
        
        #Defines the size of each cell / 0 to take up. There is 50 pixel distance between each 0 when drawn on the window.
        cell_size = 50

        #Defines the rect size of the image I will be using for the placed obstacle.
        #It gets the x and y coordinate and multiplies by 50 (the size of the cell) so the cell is placed in the spot on the window if each cell were 50 in size.
        window_grid_x = x*cell_size
        window_grid_y = y*cell_size
        
        #Number of cells at the moment.
        no_cells = 0
        #Maximum cells I want to be placed.
        max_cells = 20
        
        #The loop for checking if space is empty or occupied, if empty it should place, and places a maximum of how many cells I want by defining in the max_cells.
        loop = True
        
        while loop:
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    loop = False
            
            if no_cells >= max_cells:
                loop = False
            
            no_cells += 1
            
            
            if grid[x][y] == 0:
                print("empty")

            else:
                x
                y
            
        loop = False
        
        #Gets the image 
        self.image = pygame.image.load(image_path).convert_alpha()
        #Makes the image in the coordinates defined earlier
        self.rect = self.image.get_rect(center=(window_grid_x, window_grid_y))

    def draw (self, surface):
        surface.blit(self.image, self.rect)

Wall = Obstacles(None, "wall.png")

fpsClock.tick(60)

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
