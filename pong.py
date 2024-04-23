import pygame
from settings import Settings
import game_functions as gf

def run_game():
    ''' Initialize game '''

    pygame.init()
    pong_settings = Settings()
    screen = pygame.display.set_mode(pong_settings.screen_dimensions)
    pygame.display.set_caption("Pong")

    # main loop
    while True:
        gf.check_events()
        gf.update_screen(pong_settings, screen)

run_game()