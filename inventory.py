from colorama import Back, Style, Fore
SAFE_RESET = Style.RESET_ALL + Back.BLACK + Fore.WHITE

class Inventory:
    def __init__(self):
        self.money = 1000
        self.wood = 15
        self.tree = 1000
        self.flowers = 100
        self.flowerSeeds = 3
        self.water = 0
        self.freshFish = 0
        self.cookedFish = 0
        self.coal = 0
        self.coalMine = 0
        self.diamond = 0
        self.diamondMine = 0
        self.gold = 0
        self.goldMine = 0
        self.food = 0

    def showInv(self):
        print((f' money: {self.money}').ljust(13) + '| ', end='')
        print((f'wood: {self.wood}').ljust(11) + '| ', end='')
        print((f'tree: {self.tree}').ljust(11) + '| ', end='')
        print((f'flowers: {self.flowers}').ljust(14) + '|')

    def buy(self, item):
        if (item == 'tree'):
            if (self.money > 5):
                self.money -= 5
                self.tree += 1
                return True
        return False
    
    def sell(self, item):
        maxMoney = 9999