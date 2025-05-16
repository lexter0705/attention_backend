class IdCreator:
    def __init__(self):
        self.__count = 0

    @property
    def id(self):
        self.__count += 1
        return self.__count