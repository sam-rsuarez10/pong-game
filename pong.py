import pygame
from settings import Settings

def run_game():
    ''' Initialize game '''

    pygame.init()
    pong_settings = Settings()
    pygame.display.set_mode(pong_settings.screen_dimensions)
    pygame.display.set_caption("Pong")

    # main loop
    while True:
        pass

run_game()