class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    
    def __init__(self) -> None:
        """
        Method to set default values of Television object.
        """
        self.__statue = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        
    def power(self):
        """
        Method to turn the tv on and of
        """
        self.__statue = not self.__statue
        
    def mute(self):
        """
        Method to mute and unmute the tv
        """
        if self.__statue:
            self.__muted = not self.__muted
        
    def channel_up(self):
        """
        Method to turn up the channel
        """
        if self.__statue:
            self.__channel = self.__channel+1 if self.__channel != Television.MAX_CHANNEL else Television.MIN_CHANNEL
            
    def channel_down(self):
        """
        Method to turn down the channel
        """
        if self.__statue:
            self.__channel = self.__channel-1 if self.__channel != Television.MIN_CHANNEL else Television.MAX_CHANNEL
            
    def volume_up(self):
        """
        Method to turn up the volume
        """
        if self.__statue:
            self.__muted = False
            
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
            
    def volume_down(self):
        """
        Method to turn down the volume
        """
        if self.__statue:
            self.__muted = False
            
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
    
    def __str__(self) -> str:
        """
        Method to show the TV statue
        :retun: tv statue
        """
        return f'Power = {self.__statue}, Channel = {self.__channel}, Volume = {self.__volume if not self.__muted else Television.MIN_VOLUME}'