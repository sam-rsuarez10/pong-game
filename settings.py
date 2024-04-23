class Settings():
    ''' Initialize game's settings '''
    
    def __init__(self) -> None:
        # screen settings
        self.__screen_width = 1500
        self.__sceen_height = 750

    @property
    def screen_dimensions(self):
        ''' Return a tuple containing width and height screen dimensions '''
        return (self.__screen_width, self.__sceen_height)