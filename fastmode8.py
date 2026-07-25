import pygame
import random
import time

pygame.init()

# This is how many times the screen updates every second
fps = 60
fpsClock = pygame.time.Clock()


window_width = 1000 # This is the size of the window
window_height = 750
screen = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE | pygame.DOUBLEBUF) #I've made it resizable window.
screen_colour = (20, 20, 20) #Grey colour for the bakground of the window

class Button:
    """this code creates a button blueprint
    
    This code makes a button that can have custom, x and y position, size, what is displayed on it, and what happens when its pressed.
    I will use this code to make buttons for my games menus, which will have lots of different colours, functions and looks.
    I am using this code because it makes the process of making buttons very easy because I don't have to retype all this code everytime I want a new button.

    this code changes
    -The menu screen to the game screen
    -Whether you enter the game or leave the game
    """

    def __init__(self, x, y, image_path, onclickFunction):
        self.image = pygame.image.load(image_path).convert_alpha() # Gets the image
        self.rect = self.image.get_rect(center=(x, y)) # Makes the image
        self.onclickFunction = onclickFunction

    def draw(self, surface):
        surface.blit(self.image, self.rect) # This draws the image you want onto the surface you specify when drawing the image.

    def check_click(self, pos):
        if self.rect.collidepoint(pos): # Checks if mouse is over the button 
            if self.onclickFunction: # Checks whether onclickfunction has been defined in the class blueprint 
                self.onclickFunction() # Then it does the function defined below

# These are the definitions for what function each button can do.
def Game(): # Creates Game loop
    game_screen = True
    global_grid = [[0 for _ in range(20)] for _ in range(15)] # Draws the grid of 0's to the size of the grid defined. 
    # This is where I generate all my random coordinates, then all the obstacle IDs are converted to pixel coordinates later on with images.
    
    Player = Obstacle("motobike.png", False, global_grid, 4, 1) # Draws the obstacle class by generating random position and placing in random position.
    Orb = Obstacle("orb.png", False, global_grid, 3, 5) # I have the name of the obstacle, the image used, 
    Void = Obstacle("void.png", True, global_grid, 2, 50) # whether it needs an orb radius so nothin gis placed around it, 
    Wall = Obstacle("wall.png", True, global_grid, 1, 50) # what grid it goes on (the only one), obstacle ID number, and max number of those obstacles.
    Fastmode = Obstacle("fastmode.png", False, global_grid, 5, 1)
    U_WIN = Obstacle("u_win.png", False, global_grid, 5, 1)

    player_col = 0 #X position
    player_row = 0 #Y position
    
    original_img = Player.image # Gets player image.
    for col, row in enumerate(global_grid): # Gets the player coordinate from the global grid.
        if 4 in row:
            player_row = col
            player_col = row.index(4)
            break

    player_x_change = 0
    player_y_change = 0
    global_grid[player_row][player_col] = 4 # Puts the image where the (motobike/obstacle ID 4) is.
    
    continous_movement = False # This is to make sure the player doesn't start in fastmode

    while game_screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_screen = False
                pygame.quit()     
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    continous_movement = not continous_movement # Toggle switch is space bar for whether motobike is moving non-stop or 1 tile at a time.
                if event.key == pygame.K_LEFT: # Arrow keys for movement will make the motobike move in specific direction and rotate to face that direction.
                    print("going left")
                    player_x_change = -1
                    player_y_change = 0
                    Player.image = pygame.transform.rotate(original_img, 0)
                if event.key == pygame.K_RIGHT:
                    print("going right")
                    player_x_change = 1
                    player_y_change = 0
                    Player.image = pygame.transform.rotate(original_img, 180)
                if event.key == pygame.K_UP:
                    print("going up")
                    player_x_change = 0
                    player_y_change = -1
                    Player.image = pygame.transform.rotate(original_img, -90)
                if event.key == pygame.K_DOWN:
                    print("going down")
                    player_x_change = 0
                    player_y_change = 1
                    Player.image = pygame.transform.rotate(original_img, 90)

        if player_x_change != 0 or player_y_change != 0: # Player movement, pressing one of the keys WASD
            new_col = player_col + player_x_change
            new_row = player_row + player_y_change

            if 0 <= new_col < 20 and 0 <= new_row < 15: # Boundary check: so the motobike can't go outside the window and crash the game.
                if global_grid[new_row][new_col] == 0: # If the tile the motobike is gonna move onto empty it will move. 0 means empty, 3 means orb
                    global_grid[player_row][player_col] = 0 # Sets the current grid position as empty.
                    player_col = new_col
                    player_row = new_row
                    global_grid[new_row][new_col] = 4 # Assigns the new position after moving the grid value of 4, the motobike.
                
                if global_grid[new_row][new_col] == 3:
                    global_grid[player_row][player_col] = 0   
                    player_col = new_col
                    player_row = new_row
                    global_grid[new_row][new_col] = 4

                if global_grid[new_row][new_col] == 2: # Checks if its a void
                    if continous_movement: # If you are in fastmode, it will check the tile beyond the void, to see if its empty, if yes then it will put the player in the space after the void.
                        if 0 <= new_col + player_x_change < 20 and 0 <= new_row + player_y_change < 15:
                            if global_grid[new_row + player_y_change][new_col + player_x_change] == 0:
                                global_grid[player_row][player_col] = 0   
                                player_col = new_col + player_x_change
                                player_row = new_row + player_y_change
                                global_grid[new_row + player_y_change][new_col + player_x_change] = 4
                            else:
                                continous_movement = False # If the space beyond the void is occupied, even by another void, it will make the player exit fastmode.

                if not continous_movement: # Makes motobike move 1 tile at a time. So that the movement isn't non-stop. But it can be toggled on as well by the spacebar if the player wants to go really quickly.
                    player_x_change = 0
                    player_y_change = 0
        
        remaining_orbs = sum(row.count(3) for row in global_grid) # Counts how many orbs left on the map.
        print(remaining_orbs)
        win = False
        if remaining_orbs < 1: # If the count of orbs is 0 then it activates the win condition.
            win = True
            

        # Redraws each of the following things every frame, at (10) frames per second
        screen.fill(screen_colour)
        Player.draw(screen)
        Void.draw(screen)
        Wall.draw(screen)
        Orb.draw(screen)
        if continous_movement: # When in fastmode it shows a border around the edge of the screen to indicate that you are in fastmode.
            Fastmode.effect(screen)
        if win == True: # Shows the win screen when win condition is met.
            U_WIN.effect(screen)
        pygame.display.flip() 
        fpsClock.tick(10)

def Exit():  # If you use exit function then the game will exit.
    print("exit")
    pygame.quit()

# Setting all the positions to be changable if i chaange the window size of want to quickly change the size of the button themselves
# (x, y, width, height, text, difficulty, onclickFunction, rect_colour, text_colour)
ExitButton = Button(((window_width * 1)/3), (window_height/2), 'exitbutton.png', Exit)
PlayButton = Button(((window_width * 2)/3), (window_height/2), 'playbutton.png', Game)

class Obstacle:
    """This code creates a grid of 1's and 0's and will randomly place a wall in one of the grid segments
    
    This code changes the window of the game to include obstacles that the motobike cannot move through and objectives.
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

        grid_width = len(game_grid[0]) # Width of the global grid: 20
        grid_height = len(game_grid)   # Height of the global grid: 15
        
        placed_cells = 0  # Number of cells at the moment.

        while placed_cells < max_cells:  # If there is too many obstacles it will stop the loop
            # generates random value for the x and y coordinate
            center_x = random.randint(0, grid_width - 1)
            center_y = random.randint(0, grid_height - 1)
            
            # Checks random grid coordinate generated is empty of all obstacles.
            if self.game_grid[center_y][center_x] == 0:

                self.orb_radius(center_x, center_y, grid_width, grid_height) # Skips placing walls or voids if they are within the radius of the player or orbs.
                if obstacle_id != 3 and obstacle_id != 4 and self.orb_aura == True:
                    continue # restarts while loop.

                self.game_grid[center_y][center_x] = obstacle_id
                placed_cells += 1  # Adds 1 to placed_cells for every time this while loops
            
            # This is the fallback if the coordinate can't be placed, it tries to place in an adjacent coordinate.
            elif self.random_adjacent:
                # Adds the values of the cardinal directions to the coordinates, so i get 4 new coordinates that are on all different sides of the original.
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
                placed_adjacent = False

                for direction_x, direction_y in directions: 
                    adjacent_x, adjacent_y = center_x + direction_x, center_y + direction_y # Adds the direction coordinates from the list of directions, with the current coordinate position of the obstacle. 
                    # To get the position of the obstacle if it were moved to the adjacent spot.

                    if 0 <= adjacent_x < grid_width and 0 <= adjacent_y < grid_height: # Checks the adjacent coordinate hasn't gone outside the global grid boundary.
                        if self.game_grid[adjacent_y][adjacent_x] == 0: 

                            self.orb_radius(center_x, center_y, grid_width, grid_height)
                            if obstacle_id != 3 and obstacle_id != 4 and self.orb_aura == True:
                                continue # restarts while loop

                            self.game_grid[adjacent_y][adjacent_x] = obstacle_id
                            placed_cells += 1
                            placed_adjacent = True
                            break

                    if not placed_adjacent: # Fallback if everything else fails, and the obstacle can't be placed so the whole program doesn't crash. And useful for debugging.
                        print(f"panic!!! ({center_x}, {center_y}) are completely trapped")

                else:
                    print(f"space ({center_x}, {center_y}) occupied, random_adjacent is False.")

        # below are some very helpful debugging tools to tell what is going on :)
        # how many walls and voids have been placed
        total_walls = sum(row.count(1) for row in self.game_grid)
        total_voids = sum(row.count(2) for row in self.game_grid)
        total_orbs = sum(row.count(3) for row in self.game_grid)

        print((center_x, center_y)) #These are the coordinates of the placed number, loops to include numbers 1, 2, 3 and 4

        print(f"Walls: {total_walls} | Voids: {total_voids} | Orbs: {total_orbs}")

        # this code makes the grid look nice by removing all the brackets and ensuring each line is below the next so its not all in one big line :)    
        for row in self.game_grid:
            print(*row, sep=" ")    

    # Used to check if all the spaces around the orbs and player are empty
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
        This code checks every cell in the game grid whether it has a cell value or not.
        it does this by using enumerate, for y, row in enumerate(self.game_grid): basically
        means the y is the index of the enumerator, so it keeps track of the y position, and 
        the row which has its own enumerate. if i had a dictionary of colours, i could enumerate
        it to tell me what the index is? (the number on the list going down) and the colour.
        EG: for index, colour in enumerate(colours):
        print(f"Index:{index} ,Colour:{colour}")
        """
        for y, row in enumerate(self.game_grid): # This code goes through every coordinate in the grid.
            for x, cell_value in enumerate(row):
                if cell_value == self.obstacle_id:
                    self.window_grid_x = x * self.cell_size + (self.cell_size / 2) # Here it converts coordinates on the grid if there is an obstacle there, to a pixel coordinate on the window.
                    self.window_grid_y = y * self.cell_size + (self.cell_size / 2)
        
                    # Makes the image in the coordinates defined earlier, window_grid_x/y is the grid width multiplied by the cell size to make it fit on the window.
                    self.rect = self.image.get_rect(center=(self.window_grid_x, self.window_grid_y))
                
                    # Puts image in dimensions of the image rect and places image rect on the screen
                    surface.blit(self.image, self.rect)
    def effect(self, surface):
        self.rect = self.image.get_rect(center=(500, 375))
        surface.blit(self.image, self.rect)

fpsClock.tick(60)

# This is the MAIN MENU.
game_loop = True
while game_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN: # Checks if player has pressed a button when in the main menu.
            ExitButton.check_click(event.pos)
            PlayButton.check_click(event.pos)
    screen.fill(screen_colour)
    ExitButton.draw(screen)
    PlayButton.draw(screen)
    pygame.display.update()