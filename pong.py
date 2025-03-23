import pygame
from settings import Settings
import game_functions as gf
from user_bar import UserBar

def run_game():
    ''' Initialize game '''

    pygame.init()
    pong_settings = Settings()
    screen = pygame.display.set_mode(pong_settings.screen_dimensions)
    pygame.display.set_caption("Pong")

    user_bar = UserBar(pong_settings, screen)
    
    # main loop
    while True:
        gf.check_events()
        gf.update_screen(pong_settings, screen, user_bar)

run_game()