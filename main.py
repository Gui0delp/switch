"""Name of the game: switch
"""

#! /usr/bin/env python3
# coding: utf-8

import pygame
import modules.level as lvl

def main():
    """The function contains the main code of the game
    """
    w_sprite = 60
    l_sprite = 60
    w_width = 9 * w_sprite
    w_length = 9 * l_sprite
    quit_game = True
    pygame.init() # pylint: disable=no-member
    pygame.display.set_caption("Macgyver maze") # pylint: disable=no-member
    window = pygame.display.set_mode((w_width, w_length)) # pylint: disable=no-member
    level = lvl.Level()
    level.generate_lvl()

    while quit_game:

        level.refresh_lvl(window)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:    # pylint: disable=no-member
                if event.key == pygame.K_ESCAPE:    # pylint: disable=no-member
                    quit_game = False
                    pygame.quit() # pylint: disable=no-member


    input()

if __name__ == "__main__":
    #Call the main() function of the game
    main()
