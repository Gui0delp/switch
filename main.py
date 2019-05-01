"""Name of the game: switch
"""

#! /usr/bin/env python3
# coding: utf-8

import pygame
import modules.level as lvl
import modules.character as user

def main():
    """The function contains the main code of the game
    """
    w_sprite = 60
    l_sprite = 60
    w_width = 9 * w_sprite
    w_length = 9 * l_sprite
    quit_game = True
    pygame.init() # pylint: disable=no-member
    pygame.display.set_caption("Switch") # pylint: disable=no-member
    window = pygame.display.set_mode((w_width, w_length)) # pylint: disable=no-member
    level = lvl.Level()
    level.generate_lvl()
    player = user.Character(level.game_level)

    while quit_game:

        level.refresh_lvl(window)
        player.move(window, "")

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:    # pylint: disable=no-member
                if event.key == pygame.K_ESCAPE:    # pylint: disable=no-member
                    quit_game = False
                    pygame.quit() # pylint: disable=no-member
                elif event.key == pygame.K_LEFT: # pylint: disable=no-member
                    player.move(window, "LEFT")
                    player.switch()
                elif event.key == pygame.K_RIGHT: # pylint: disable=no-member
                    player.move(window, "RIGHT")
                    player.switch()
                elif event.key == pygame.K_UP: # pylint: disable=no-member
                    player.move(window, "UP")
                    player.switch()
                elif event.key == pygame.K_DOWN: # pylint: disable=no-member
                    player.move(window, "DOWN")
                    player.switch()
                else:
                    pass

        pygame.display.flip()

if __name__ == "__main__":
    #Call the main() function of the game
    main()
