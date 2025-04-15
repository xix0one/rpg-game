from colorama import Back, Style, Fore
SAFE_RESET = Style.RESET_ALL + Back.BLACK + Fore.LIGHTWHITE_EX

class Objects:
    def __init__(self, y, x):
        self.y = y
        self.x = x
    
    def getCoord(self):
        return [self.y, self.x]

    def print(self):
        raise NotImplementedError('the method print must be overridden')
    
class Water(Objects):
    def __init__(self, y, x):
        super().__init__(y, x)

    @staticmethod
    def print():
        print(Back.LIGHTBLUE_EX + '~' + SAFE_RESET, end='')

class Tree(Objects):
    def __init__(self, y, x):
        super().__init__(y, x)

    @staticmethod
    def print():
        print(Back.LIGHTGREEN_EX + 'T' + SAFE_RESET, end='')