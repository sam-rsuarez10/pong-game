import pygame
import sys

def check_keydown_events(event, user_bar):
    ''' Respond to key presses '''
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_UP or event.key == pygame.K_w:
        user_bar.moving_up = True
    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        user_bar.moving_down = True

def check_keyup_events(event, user_bar):
    ''' Respond to key releases '''
    if event.key == pygame.K_UP or event.key == pygame.K_w:
        user_bar.moving_up = False
    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        user_bar.moving_down = False

def check_events(user_bar):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, user_bar)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, user_bar)

def update_screen(settings, screen, user_bar, computer_bar):
    ''' Update images on the screen and flip to the new screen '''
    
    # redraw the screen through the loop
    screen.fill(settings.bg_color)
    user_bar.draw()
    computer_bar.draw()

    pygame.display.flip()