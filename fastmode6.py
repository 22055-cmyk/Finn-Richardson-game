import pygame
import random
import time

pygame.init()

# This is how many times the screen updates every second
fps = 60
fpsClock = pygame.time.Clock()

window_width = 1000
window_height = 750
screen = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE | pygame.DOUBLEBUF)
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
        
        # Gets the image
        self.image = pygame.image.load(image_path).convert_alpha()
        # Makes the image 
        self.rect = self.image.get_rect(center=(x, y))
        self.onclickFunction = onclickFunction

    def draw(self, surface):
        # This draws the image you want onto the surface you specify when drawing the image.
        
        surface.blit(self.image, self.rect)

    def check_click(self, pos):
        # Checks if mouse is over the button
        if self.rect.collidepoint(pos):
            # Checks whether onclickfunction has been defined in the class blueprint
            if self.onclickFunction:
                # Then it does the function defined below
                self.onclickFunction()

# These are the definitions 
def Game(): # Creates Game loop
    game_screen = True
    global_grid = [[0 for _ in range(20)] for _ in range(15)] # Draws the grid of 0's to the size of the grid defined.

    # Draws the obstacle class by generating random position and placing in random position.
    Player = Obstacle("motobike.png", False, global_grid, 4, 1)
    Orb = Obstacle("orb.png", False, global_grid, 3, 5)
    Void = Obstacle("void.png", True, global_grid, 2, 50)
    Wall = Obstacle("wall.png", True, global_grid, 1, 50)
    
    while game_screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_screen = False
                pygame.quit()     
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_LEFT:
                    player_x_change = -50
                    player_y_change = 0
                if event.type == pygame.K_RIGHT:
                    player_x_change = 50
                    player_y_change = 0
                if event.type == pygame.K_UP:
                    player_x_change = 0
                    player_y_change = -50
                if event.type == pygame.K_DOWN:
                    player_x_change = 0
                    player_y_change = 50

        player_x += player_x_change
        player_y += player_y_change
        
        screen.fill(screen_colour)
        
        Player.draw(screen)
        Void.draw(screen)
        Wall.draw(screen)
        Orb.draw(screen)
        
        pygame.display.flip() 

        fpsClock.tick(60)



def Exit():  # If you use exit function then the game will exit.
    print("exit")
    pygame.quit()

# Setting all the positions to be changable if i chaange the window size of want to quickly change the size of the button themselves
# (x, y, width, height, text, difficulty, onclickFunction, rect_colour, text_colour)
ExitButton = Button(((window_width * 1)/3), (window_height/2), 'exitbutton.png', Exit)
PlayButton = Button(((window_width * 2)/3), (window_height/2), 'playbutton.png', Game)

class Obstacle:
    """THis code creates a grid of 1's and 0's and will randomly place a wall in one of the grid segments
    This class is
    """
    def __init__ (self, image_path, random_adjacent, game_grid, obstacle_id, max_cells):
        self.image = pygame.image.load(image_path).convert_alpha() # Gets the image 
        self.random_adjacent = random_adjacent
        self.cell_size = 50 # Defines the size of each cell / 0 to take up. There is 50 pixel distance between each 0 when drawn on the window.
        self.window_grid_x = 0
        self.window_grid_y = 0
        self.game_grid = game_grid
        self.obstacle_id = obstacle_id
        self.max_cells = max_cells # Maximum cells I want to be placed.

        grid_width = len(game_grid[0]) #  20
        grid_height = len(game_grid)   #  15
        
        placed_cells = 0  # Number of cells at the moment.

        while placed_cells < max_cells:  # If there is too many 1s it will stop the loop
            # generates random value for the x and y coordinate
            center_x = random.randint(0, grid_width - 1)
            center_y = random.randint(0, grid_height - 1)
            
            # If its empty it places the obstacle
            if self.game_grid[center_y][center_x] == 0:

                self.orb_radius(center_x, center_y, grid_width, grid_height)
                if obstacle_id != 3 and obstacle_id != 4 and self.orb_aura == True:
                    continue # restarts while loop

                self.game_grid[center_y][center_x] = obstacle_id
                placed_cells += 1  # Adds 1 to placed_cells for every time this while loops
            
            elif self.random_adjacent:
                # Adds the values of the cardinal directions to the coordinates, so i get 4 new coordinates that are on all different sides of the original
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
                placed_adjacent = False

                for direction_x, direction_y in directions:
                    adjacent_x, adjacent_y = center_x + direction_x, center_y + direction_y

                    if 0 <= adjacent_x < grid_width and 0 <= adjacent_y < grid_height:
                        if self.game_grid[adjacent_y][adjacent_x] == 0:

                            self.orb_radius(center_x, center_y, grid_width, grid_height)
                            if obstacle_id != 3 and obstacle_id != 4 and self.orb_aura == True:
                                continue # restarts while loop

                            self.game_grid[adjacent_y][adjacent_x] = obstacle_id
                            placed_cells += 1
                            placed_adjacent = True
                            break

                    if not placed_adjacent:
                        print(f"panic!!! ({center_x}, {center_y}) are completely trapped")

                else:
                    print(f"space ({center_x}, {center_y}) occupied, random_adjacent is False.")

        # below are some very helpful debugging tools to tell what is going on :)
        # how many walls and voids have been placed
        total_walls = sum(row.count(1) for row in self.game_grid)
        total_voids = sum(row.count(2) for row in self.game_grid)
        total_orbs = sum(row.count(3) for row in self.game_grid)

        print(f"Walls: {total_walls} | Voids: {total_voids} | Orbs: {total_orbs}")

        # this code makes the grid look nice by removing all the brackets and ensuring each line is below the next so its not all in one big line :)    
        for row in self.game_grid:
            print(*row, sep=" ")    

    def orb_radius(self, center_x, center_y, grid_width, grid_height):

        self.orb_aura = False
        
        if self.game_grid[center_y][center_x] >= 3:
            self.orb_aura = True

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for direction_x, direction_y in directions:
            adjacent_x, adjacent_y = center_x + direction_x, center_y + direction_y

            if 0 <= adjacent_x < grid_width and 0 <= adjacent_y < grid_height:
                if self.game_grid[adjacent_y][adjacent_x] >= 3:
                    self.orb_aura = True
        
        if self.orb_aura == True:
            pass

    def draw(self, surface):
        """
        this code checks every cell in the game grid whether it has a cell value or not.
        it does this by using enumerate, for y, row in enumerate(self.game_grid): basically
        means the y is the index of the enumerator, so it keeps track of the y position, and 
        the row which has its own enumerate. if i had a dictionary of colours, i could enumerate
        it to tell me what the index is? (the number on the list going down) and the colour.
        EG: for index, colour in enumerate(colours):
        print(f"Index:{index} ,Colour:{colour}")
        """
        for y, row in enumerate(self.game_grid):
            for x, cell_value in enumerate(row):
                if cell_value == self.obstacle_id:
                    self.window_grid_x = x * self.cell_size + (self.cell_size / 2)
                    self.window_grid_y = y * self.cell_size + (self.cell_size / 2)
        
                    # Makes the image in the coordinates defined earlier, window_grid_x/y is the grid width multiplied by the cell size to make it fit on the window.
                    self.rect = self.image.get_rect(center=(self.window_grid_x, self.window_grid_y))
                
                    # Puts image in dimensions of the image rect and places image rect on the screen
                    surface.blit(self.image, self.rect)


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