import pygame

class Ball():
    ''' Class that represents the ball '''

    def __init__(self, settings, screen):
        ''' Initialize the game ball and its starting position '''
        self.screen = screen
        self.settings = settings

        self.color = (255, 255, 255)

        self.radious = 15
        self.diameter = self.radious * 2

        self.screen_rect = screen.get_rect()
        self.rect = pygame.Rect(0, 0, self.diameter, self.diameter)

        # Position the ball at the center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.x = float(self.rect.centerx)
        self.y = float(self.rect.centery)

    def draw(self):
        ''' Draw the ball '''
        pygame.draw.circle(self.screen, self.color,
                            (self.rect.centerx, self.rect.centery),
                            self.radious)