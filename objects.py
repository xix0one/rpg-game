from colorama import Back, Style, Fore
SAFE_RESET = Style.RESET_ALL + Back.BLACK + Fore.LIGHTWHITE_EX

class Objects:
    def __init__(self, y, x):
        self.y = y
        self.x = x
        self.reserve = 0
    
    def getCoord(self):
        return [self.y, self.x]
    
    def getReserve(self):
        return self.reserve

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
        looks = {
            'left': '<-',
            'right': '->',
            'down': f'{chr(25)}{chr(25)}',
            'up': f'{chr(24)}{chr(24)}'
        }
        print(Back.RED + looks[self.look] + SAFE_RESET, end='', flush=True)

class Water(Objects):
    def __init__(self, y, x):
        super().__init__(y, x)
        self.reserve = 10

    @staticmethod
    def print():
        print(Back.LIGHTBLUE_EX + '~~' + SAFE_RESET, end='', flush=True)

class Tree(Objects):
    def __init__(self, y, x):
        super().__init__(y, x)
        self.reserve = 15

    @staticmethod
    def print():
        print(Back.LIGHTGREEN_EX + 'TT' + SAFE_RESET, end='', flush=True)

    def reductionReserve(self):
        self.reserve -= 3

class Flower(Objects):
    def __init__(self, y, x):
        super().__init__(y, x)
        self.reserve = 10

    @staticmethod
    def print():
        print(Back.MAGENTA + '**' + SAFE_RESET, end='', flush=True)

    def reductionReserve(self):
        self.reserve -= 2

class Mine(Objects):
    def __init__(self, y, x):
        super().__init__(y, x)
        self.reserve = 21

    @staticmethod
    def print():
        print(Back.LIGHTCYAN_EX + '^^' + SAFE_RESET, end='', flush=True)

    def reductionReserve(self):
        self.reserve -= 3

class Shop(Objects):
    def __init__(self, y, x):
        super().__init__(y, x)

    @staticmethod
    def print():
        print(f'{Back.LIGHTYELLOW_EX}{Fore.BLACK}' + '++' + SAFE_RESET, end='', flush=True)