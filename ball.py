import pygame
from settings import BallDirection

class Ball():
    ''' Class that represents the ball '''

    def __init__(self, settings, screen):
        ''' Initialize the game ball and its starting position '''
        self.screen = screen
        self.settings = settings

        self.color = (255, 255, 255)

        self.radius = 15
        self.diameter = self.radius * 2

        self.screen_rect = screen.get_rect()
        self.rect = pygame.Rect(0, 0, self.diameter, self.diameter)

        # Position the ball at the center of the screen
        self.rect.x = self.screen_rect.centerx
        self.rect.y = self.screen_rect.centery

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.x_velocity = -settings.speed_factor if settings.ball_direction == BallDirection.LEFT else settings.speed_factor

    def draw(self):
        ''' Draw the ball '''
        pygame.draw.circle(self.screen, self.color,
                            (self.rect.x, self.rect.y),
                            self.radius)
    
    def update(self):
        ''' Update ball position '''

        self.x += self.x_velocity
        
        self.rect.x = self.x
        self.rect.y = self.y
