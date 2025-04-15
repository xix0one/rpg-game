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

class Player(Objects):
    def __init__(self, y, x, look='left'):
        super().__init__(y, x)
        self.look = look

    def changeLook(self, look):
        self.look = look

    def changeCoord(self, y, x):
        self.y = y
        self.x = x

    def print(self):
        currentlook = 0
        if (self.look == 'left'):
            currentlook = '<-'
        if (self.look == 'right'):
            currentlook = '->'
        if (self.look == 'down'):
            currentlook = f'{chr(25)}{chr(25)}'
        if (self.look == 'up'):
            currentlook = f'{chr(24)}{chr(24)}'
        print(Back.RED + f'{currentlook}' + SAFE_RESET, end='')

class Water(Objects):
    def __init__(self, y, x):
        super().__init__(y, x)

    @staticmethod
    def print():
        print(Back.LIGHTBLUE_EX + '~~' + SAFE_RESET, end='')

class Tree(Objects):
    def __init__(self, y, x):
        super().__init__(y, x)

    @staticmethod
    def print():
        print(Back.LIGHTGREEN_EX + 'TT' + SAFE_RESET, end='')

class Flower(Objects):
    def __init__(self, y, x):
        super().__init__(y, x)

    @staticmethod
    def print():
        print(Back.MAGENTA + '**' + SAFE_RESET, end='')