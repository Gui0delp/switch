"""Contains all the function for the level
"""

import random
import pygame

class Level(object):
    """the class permited to generate the game lvl and refresh it
    """

    def __init__(self):

        self.game_level = []
        self.size_sprite = 60

    def generate_lvl(self):
        """Permit to generate the level
        """

        lvl_structure = []
        line = []
        cells = 0
        y_case = 0

        #This part permit to generate the grid
        while y_case < 9:

            x_case = 0
            while x_case < 9:
                #Generate a random number between 0 and 1 for each cells
                cells = random.randint(0, 1)
                line.append(cells)
                x_case += 1
            #Save the line into the structure
            lvl_structure.append(line)
            line = []
            y_case += 1

        #Save the structure of the grid into the game level
        self.game_level = lvl_structure
        self.game_level[0][0] = "E"
        self.game_level[8][8] = "S"

    def refresh_lvl(self, screen):
        """Permit to refresh the level
        screen type: Object
        """
        path_l = pygame.image.load("resources/sprites/path_L.png").convert_alpha()    #1
        path_d = pygame.image.load("resources/sprites/path_D.png").convert_alpha()    #0
        start = pygame.image.load("resources/sprites/start.png").convert_alpha()    #S
        end = pygame.image.load("resources/sprites/end.png").convert_alpha()    #E

        num_line = 0

        for line in self.game_level:

            num_column = 0
            #We read all the sprite in line
            for sprite in line:

                x_grid = num_column * self.size_sprite
                y_grid = num_line * self.size_sprite
                #Show hte differents sprite in the level
                if sprite == 1:
                    screen.blit(path_l, (x_grid, y_grid))
                elif sprite == 0:
                    screen.blit(path_d, (x_grid, y_grid))
                elif sprite == "E":
                    screen.blit(start, (x_grid, y_grid))
                elif sprite == "S":
                    screen.blit(end, (x_grid, y_grid))

                num_column += 1

            num_line += 1
