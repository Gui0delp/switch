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
        self.x_case = 0
        self.y_case = 0
        self.font = pygame.font.SysFont("Arial", 16)

    def move(self, screen, direction):
        """This function permit to move the player
        screen type: Object
        direction type: string
        """
        size_sprite = 60
        player = pygame.image.load("resources/sprites/user.png").convert_alpha()
        self.x_case = self.x_user
        self.y_case = self.y_user

        if direction == "LEFT":
            self.x_user -= 1
            if self.x_user < 0:
                self.x_user = 0
            if self.lvl[self.y_user][self.x_user] == "W":
                self.x_user += 1
        elif direction == "RIGHT":
            self.x_user += 1
            if self.x_user > 8:
                self.x_user = 8
            if self.lvl[self.y_user][self.x_user] == "W":
                self.x_user -= 1
        elif direction == "UP":
            self.y_user -= 1
            if self.y_user < 0:
                self.y_user = 0
            if self.lvl[self.y_user][self.x_user] == "W":
                self.y_user += 1
        elif direction == "DOWN":
            self.y_user += 1
            if self.y_user > 8:
                self.y_user = 8
            if self.lvl[self.y_user][self.x_user] == "W":
                self.y_user -= 1

        screen.blit(player, (self.x_user * size_sprite, self.y_user * size_sprite))

    def switch(self):
        """This function permit to switch the case 0 and 1
        """
        if self.lvl[self.y_user][self.x_user] == 0 and self.y_user != self.y_case:
            self.lvl[self.y_user][self.x_user] = 1
        elif self.lvl[self.y_user][self.x_user] == 0 and self.x_user != self.x_case:
            self.lvl[self.y_user][self.x_user] = 1
        elif self.lvl[self.y_user][self.x_user] == 1 and self.y_user != self.y_case:
            self.lvl[self.y_user][self.x_user] = 0
        elif self.lvl[self.y_user][self.x_user] == 1 and self.x_user != self.x_case:
            self.lvl[self.y_user][self.x_user] = 0

    def user_interface(self, screen, statut):
        """This function permit to upgrade the user interface
        screen type: object
        statut type: integer
        """
        #user win
        if statut == 1:
            win_message = self.font.render("Great work you win!", True, (255, 255, 255))
            info_message = self.font.render("PRESS ESC TO QUIT", True, (255, 255, 255))
            screen.blit(win_message, (320, 505))
            screen.blit(info_message, (210, 260))
        #nothing
        else:
            info_message2 = self.font.render("Press [r] to restart", True, (255, 255, 255))
            screen.blit(info_message2, (405, 0))
