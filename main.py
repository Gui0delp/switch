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
    game = True
    quit_game = True
    statut = 0
    pygame.init() # pylint: disable=no-member
    pygame.display.set_caption("Switch") # pylint: disable=no-member
    window = pygame.display.set_mode((w_width, w_length)) # pylint: disable=no-member

    level = lvl.Level()
    level.generate_lvl()
    player = user.Character(level.game_level)

    while game:

        level.refresh_lvl(window)
        player.move(window, "")
        #Permit to know if the player win or... not
        if level.case_1 == 68 and level.game_level[player.y_user][player.x_user] == "E":
            statut = 1
            game = False
            main()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:    # pylint: disable=no-member
                if event.key == pygame.K_ESCAPE:    # pylint: disable=no-member
                    game = False
                elif event.key == pygame.K_r:    # pylint: disable=no-member
                    main()
                elif event.key == pygame.K_LEFT: # pylint: disable=no-member
                    player.move(window, "LEFT")
                    player.switch()
                elif event.key == pygame.K_RIGHT:  # pylint: disable=no-member
                    player.move(window, "RIGHT")
                    player.switch()
                elif event.key == pygame.K_UP:  # pylint: disable=no-member
                    player.move(window, "UP")
                    player.switch()
                elif event.key == pygame.K_DOWN:  # pylint: disable=no-member
                    player.move(window, "DOWN")
                    player.switch()

        player.user_interface(window, statut)
        pygame.display.flip()

    while quit_game:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:    # pylint: disable=no-member
                if event.key == pygame.K_ESCAPE:    # pylint: disable=no-member
                    quit_game = False

    pygame.quit() # pylint: disable=no-member

if __name__ == "__main__":
    #Call the main() function of the game
    main()
