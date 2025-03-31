class Settings():
    ''' Initialize game's settings '''

    def __init__(self) -> None:
        # screen settings
        self.__screen_width = 1500
        self.__sceen_height = 750
        self.__bg_color = (0, 0, 0)
        
        self.bar_speed_factor = 1.5

        # margin between the bars and the screen
        self.bar_margin = 30
    @property
    def bg_color(self):
        return self.__bg_color

    @property
    def screen_dimensions(self):
        ''' Return a tuple containing width and height screen dimensions '''
        return (self.__screen_width, self.__sceen_height)