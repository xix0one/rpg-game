import random

from colorama import Back, Style, Fore
SAFE_RESET = Style.RESET_ALL + Back.BLACK + Fore.LIGHTWHITE_EX

class Inventory:
    def __init__(self):
        self.money = 50
        self.wood = 2
        self.tree = 3
        self.flower = 2
        self.flowerSeed = 3
        self.water = 1
        self.freshFish = 0
        self.cookedFish = 0
        self.iron = 0
        self.gold = 0
        self.mine = 0
        self.food = 0
        self.bonfire = 1

    def showInvFirstLine(self):
        print((f' {Fore.LIGHTYELLOW_EX}money:   {self.money}{SAFE_RESET}').ljust(34) + '| ', end='')
        print((f'{Fore.LIGHTGREEN_EX}food:    {self.food}{SAFE_RESET}').ljust(33) + '| ', end='')
        print((f'{Fore.LIGHTCYAN_EX}wood: {self.wood}{SAFE_RESET}').ljust(31) + '| ', end='')
        print((f'{Fore.LIGHTBLUE_EX}water: {self.water}{SAFE_RESET}').ljust(30) + ' |')

    def showInvSecondLine(self):
        print((f'{Fore.LIGHTMAGENTA_EX}flower:  {self.flower}{SAFE_RESET}').ljust(33) + '| ', end='')
        print((f'{Fore.LIGHTCYAN_EX}flowerS: {self.flowerSeed}{SAFE_RESET}').ljust(33) + '| ', end='')
        print((f'{Fore.LIGHTRED_EX}fish: {self.freshFish}{SAFE_RESET}').ljust(31) + '| ', end='')
        print((f'{Fore.LIGHTMAGENTA_EX}fishC: {self.cookedFish}{SAFE_RESET}').ljust(30) + ' |')
        

    def showInvThirdLine(self):
        print((f'{Fore.LIGHTGREEN_EX}tree:    {self.tree}{SAFE_RESET}').ljust(33) + '| ', end='')
        print((f'{Fore.LIGHTBLUE_EX}mine:    {self.mine}{SAFE_RESET}').ljust(33) + '| ', end='')
        print((f'iron: {self.iron}').ljust(12) + '| ', end='')
        print((f'{Fore.LIGHTYELLOW_EX}gold:  {self.gold}{SAFE_RESET}').ljust(30) + ' | ')

    def showInvFourthLine(self):
        print((f'{Fore.YELLOW}bonfire: {self.bonfire}{SAFE_RESET}').ljust(32) + ' | ', end='')
        print((f'').ljust(14) + '| ', end='')
        print((f'').ljust(12) + '| ', end='')
        print((f'').ljust(12) + '| ')

    def addflowerSeed(self):
        if random.random() < 0.15:
            if (self.flowerSeed < 9999):
                self.flowerSeed += 1
            return True
        return False
    
    def addFlower(self):
        if (self.flower < 9997):
            self.flower += 2

    def addWood(self):
        if (self.wood < 9996):
            self.wood += 3

    def addIron(self):
        if (self.iron < 9999):
            self.iron += 1

    def addGold(self):
        if random.random() < 0.15:
            if (self.gold < 9999):
                self.gold += 1
            return True
        return False
    
    def addFish(self):
        if random.random() < 0.5:
            if (self.freshFish < 9999):
                self.freshFish += 1
            return True
        return False

    def getTotal(self, obj):
        objs = {
            'flower': self.flower,
            'flowerSeed': self.flowerSeed,
            'wood': self.wood,
            'iron': self.iron,
            'gold': self.gold,
            'fish': self.freshFish,
            'tree': self.tree,
            'water': self.water,
            'mine': self.mine,
            'bonfire': self.bonfire
        }
        return objs[obj]

    # def buy(self, item):
    #     if (item == 'tree'):
    #         if (self.money > 5):
    #             self.money -= 5
    #             self.tree += 1
    #             return True
    #     return False
    
    def sell(self, item):
        maxMoney = 9999