class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    
    def __init__(self) -> None:
        self.__statue = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        
    def power(self):
        self.__statue = not self.__statue
        
    def mute(self):
        if self.__statue:
            self.__muted = not self.__muted
        
    def channel_up(self):
        if self.__statue:
            self.__channel = self.__channel+1 if self.__channel != Television.MAX_CHANNEL else Television.MIN_CHANNEL
            
    def channel_down(self):
        if self.__statue:
            self.__channel = self.__channel-1 if self.__channel != Television.MIN_CHANNEL else Television.MAX_CHANNEL
            
    def volume_up(self):
        if self.__statue:
            self.__muted = False
            
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
            
    def volume_down(self):
        if self.__statue:
            self.__muted = False
            
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
    
    def __str__(self) -> str:
        return f'Power = {self.__statue}, Channel = {self.__channel}, Volume = {self.__volume if not self.__muted else Television.MIN_VOLUME}'