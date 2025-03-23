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
        
        # position bar
        self.rect.left = 20
        self.rect.centery = self.settings.screen_dimensions[1] // 2

        self.y = float(self.rect.y)
    
    def draw(self):
        ''' Draw the user bar '''
        pygame.draw.rect(self.screen, self.color, self.rect)