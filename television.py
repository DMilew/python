class Television:
    '''
    These are functions of tv and constant values, not to be changed.
    '''
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        '''
        Method to initialize a tv object
        '''
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        '''
        Method to power the tv on or off
        '''
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        '''
        Method to mute the tv, setting volume to temp 0.
        '''
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True

    def channel_up(self) -> None:
        '''
        Method to increase the tv channel.
        If channel exceeds MAX_CHANNEL, it will be set to MIN_CHANNEL.
        '''
        if self.__status:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = 0

    def channel_down(self) -> None:
        '''
        Method to decrease the tv channel.
        If channel drops below MIN_CHANNEL, it will be set to MAX_CHANNEL.
        '''
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = 3   #think this should set to 3

    def volume_up(self) -> None:
        '''
        Method to increase the tv volume. It will not exceed MAX_VOLUME.
        '''
        if self.__status:
                if self.__volume < Television.MAX_VOLUME:
                    self.__volume += 1
                self.__muted = False

    def volume_down(self) -> None:
        '''
        Method to decrease the tv volume. It will not drop below MIN_VOLUME.
        '''
        if self.__status:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
                self.__muted = False
    def __str__(self) -> str:
        '''
        Method to show the tv status.
        :return: tv status.
        '''
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_CHANNEL}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'