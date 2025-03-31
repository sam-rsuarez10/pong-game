import pygame
from settings import Settings
import game_functions as gf
from user_bar import UserBar
from computer_bar import ComputerBar

def run_game():
    ''' Initialize game '''

    pygame.init()
    pong_settings = Settings()
    screen = pygame.display.set_mode(pong_settings.screen_dimensions)
    pygame.display.set_caption("Pong")

    user_bar = UserBar(pong_settings, screen)
    computer_bar = ComputerBar(pong_settings, screen)

    # main loop
    while True:
        user_bar.update()
        gf.check_events(user_bar)
        gf.update_screen(pong_settings, screen, user_bar, computer_bar)

run_game()