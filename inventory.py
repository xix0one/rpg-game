from colorama import Back, Style, Fore
SAFE_RESET = Style.RESET_ALL + Back.BLACK + Fore.WHITE

class Inventory:
    def __init__(self):
        self.money = 100
        self.wood = 15
        self.tree = 3
        self.flowers = 15
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
        print(self.tree)

    def buy(self, item):
        if (item == "tree"):
            if (self.money > 5):
                self.money -= 5
                self.tree += 1
                return True
        return False