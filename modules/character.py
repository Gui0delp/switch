"""Contains all the function for the character
"""
import pygame

class Character(object):
    """This class contains a function move for move the player into the grid
    """

    def __init__(self, lvl):
        self.x_user = 0
        self.y_user = 0
        self.lvl = lvl

    def move(self, screen, direction):
        """This function permit to move the player
        screen type: Object
        direction type: string
        """
        size_sprite = 60
        player = pygame.image.load("resources/sprites/user.png").convert_alpha()

        if direction == "LEFT":
            self.x_user -= 1
            if self.x_user < 0:
                self.x_user = 0
        elif direction == "RIGHT":
            self.x_user += 1
            if self.x_user > 8:
                self.x_user = 8
        elif direction == "UP":
            self.y_user -= 1
            if self.y_user < 0:
                self.y_user = 0
        elif direction == "DOWN":
            self.y_user += 1
            if self.y_user > 8:
                self.y_user = 8

        screen.blit(player, (self.x_user * size_sprite, self.y_user * size_sprite))

    def switch(self):
        """This function permit to switch the case 0 and 1
        """
        if self.lvl[self.y_user][self.x_user] == 0:
            self.lvl[self.y_user][self.x_user] = 1
        elif self.lvl[self.y_user][self.x_user] == 1:
            self.lvl[self.y_user][self.x_user] = 0
