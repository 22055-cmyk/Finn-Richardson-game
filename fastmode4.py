
import pygame
import random
import time


pygame.init()

#This is how many times the screen updates every second
fps = 60
fpsClock = pygame.time.Clock()

window_width = 1000
window_height = 750
screen = pygame.display.set_mode((window_width, window_height))
screen_colour = (20, 20, 20)

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
    screen.fill(screen_colour)
    #Draws the obstacle class by generating random position and placing in random position.
    Wall = Obstacle("wall.png", screen, True)
    Void = Obstacle("void.png", screen, True)
    pygame.display.update() 
    
    while game_screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_screen = False
                pygame.quit()
               
        
def Exit():
    #If you use exit function then the game will exit.
    print("exit")
    pygame.quit()




#Setting all the positions to be changable if i chaange the window size of want to quickly change the size of the button themselves
#(x, y, width, height, text, difficulty, onclickFunction, rect_colour, text_colour)
ExitButton = Button(((window_width * 1)/3), (window_height/2), 'exitbutton.png', Exit)
PlayButton = Button(((window_width * 2)/3), (window_height/2), 'playbutton.png', Game)

class Obstacle:
    """THis code creates a grid of 1's and 0's and will randomly place a wall in one of the grid segments
    This class is
    """
    def __init__ (self, image_path, surface, random_adjacent):
        
        self.random_adjacent = random_adjacent
        #Defines the size of each cell / 0 to take up. There is 50 pixel distance between each 0 when drawn on the window.
        cell_size = 50
        window_grid_x = 0
        window_grid_y = 0

        #Defines the size of the grid, the dimensions of the window divided by 50.
        grid_width = 20
        grid_height = 15
        #Draws the grid of 0's to the size of the grid defined.
        grid = [[0 for _ in range(grid_width)] for _ in range(grid_height)]
        
        #Number of cells at the moment.
        no_cells = 0
        #Maximum cells I want to be placed.
        max_cells = 50
    
        #If there is too many 1s it will stop the loop
        while no_cells < max_cells:

            #the coordinates are generated randomly as sets of (x,y)
            coordinates = (random.randint(0, grid_width - 1), random.randint(0, grid_height - 1))


            #Adds the values of the cardinal directions to the coordinates, so i get 4 new coordinates that are on all different sides of the original
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            coords_up = tuple(a + b for a, b in zip(coordinates, directions[3]))
            coords_down = tuple(a + b for a, b in zip(coordinates, directions[2]))
            coords_left = tuple(a + b for a, b in zip(coordinates, directions[0]))
            coords_right = tuple(a + b for a, b in zip(coordinates, directions[1]))
    
    
            #coordinates are converted to the position on the grid list, because you can't assign the value (x,y) 1 or 0, in a list it can do this.
            x = (coordinates[0], coords_up[0], coords_down[0], coords_right[0], coords_left[0])
            y = (coordinates[1], coords_up[1], coords_down[1], coords_right[1], coords_left[1])
    
            #Adds 1 to no_cells for every time this while loops
            no_cells += 1
    
    
            """If where the 1 wants to place is occupied then it will not place and instead generate a new random set of coordinates.
            x and y have multiple values based on whether you want the center or cardinal directions, 0 for center (original coordinates), 1 for up, 2 for down, 3 for right, 4 for left.
            """
            if grid[y[0]][x[0]] == 1:
                
                print(f"{coordinates}: space occupied")
        
                if random_adjacent == True:
            
                    print("random_adjacent = True")
                    
                    if grid[y[1]][x[1]] == 0:
                        grid[y[1]][x[1]] = 1
                        print(f"placed up: {x[1], y[1]}")
                        random_adjacent = False

                    elif grid[y[2]][x[2]] == 0:
                        grid[y[2]][x[2]] = 1
                        print("placed down, position up occupied")
                        random_adjacent = False

                    elif grid[y[3]][x[3]] == 0:
                        grid[y[3]][x[3]] = 1
                        print("placed east, positions up and down occupied")
                        random_adjacent = False

                    elif grid[y[4]][x[4]] == 0:
                        grid[y[4]][x[4]] = 1
                        print("placed left, all other positions occupied")
                        random_adjacent = False
                    else:
                        print("panic!!!")

                else:
                    print("failed")
                    coordinates = (random.randint(0, grid_width - 1), random.randint(0, grid_height - 1))
            
                    grid[y[0]][x[0]] = 1
                    print (f"new coords: {coordinates}")
                
            #If its empty it places the obstacle
            elif grid[y[0]][x[0]] == 0:
                
                grid[y[0]][x[0]] = 1
                print (f"placed 1 here: {coordinates}")
                #
                window_grid_x = x[0] * cell_size
                window_grid_y = y[0] * cell_size
                
                #Gets the image 
                self.image = pygame.image.load(image_path).convert_alpha()
                
                #Makes the image in the coordinates defined earlier, window_grid_x/y is the grid width multiplied by the cell size to make it fit on the window.
                self.rect = self.image.get_rect(center=(window_grid_x + (cell_size / 2), window_grid_y + (cell_size / 2)))
                
                #Puts image in dimensions of the image rect and places image rect on the screen
                surface.blit(self.image, self.rect)

                #Adds a delay between placing obstacles
                time.sleep(0.01)
                pygame.display.update()
            
        for row in grid:
            print(*row, sep=" ")

                

    #def special(self):


class Wall(Obstacle):
    def __init__ (self, image_path, surface):

        super().__init__



    



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
    screen.fill(screen_colour)
    ExitButton.draw(screen)
    PlayButton.draw(screen)
    pygame.display.update()
