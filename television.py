


class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(selfself):
        pass

    def mute(self):
        pass

    def channel_up(self):
        pass

    def channel_down(self):
        '''
        Method to decrease the tv channel
        '''
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel += 1

    def volume_up(self):
        pass

    def volume_down(self):
        pass

    def __str__(self) -> str:
        '''
        Method to show the tv status.
        :return: tv status.
        '''
        if self.__muted:
            return f'Volume = {Television.MIN_VOLUME}'
        else:
            return f'xxx'