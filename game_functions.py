import pygame
import sys

def check_keydown_events(event):
    ''' Respond to key presses '''
    if event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event):
    ''' Respond to key releases '''
    pass

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event)

def update_screen(settings, screen):
    ''' Update images on the screen and flip to the new screen '''
    
    # redraw the screen through the loop
    screen.fill(settings.bg_color)

    pygame.display.flip()