import pygame

class UserBar():
    ''' Class that represents the user bar '''

    def __init__(self, settings, screen):
        ''' Initialize the user bar ans starting position '''
        self.screen = screen
        self.settings = settings

        # dimensions
        self.width = 15
        self.height = 90
        self.color = (255, 255, 255)
        
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        
        # position bar at the left side of the screen
        self.rect.left = self.settings.bar_margin
        self.rect.centery = self.settings.screen_dimensions[1] // 2

        self.y = float(self.rect.centery)

        self.moving_up = False
        self.moving_down = False

        self.screen_rect = screen.get_rect()
    
    def draw(self):
        ''' Draw the user bar '''
        pygame.draw.rect(self.screen, self.color, self.rect)
    
    def update(self):
        ''' Update the user bar position based on the movement flag '''

        if self.moving_up and self.rect.top >  0:
            self.y -= self.settings.bar_speed_factor
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.bar_speed_factor
        
        self.rect.centery = self.y
