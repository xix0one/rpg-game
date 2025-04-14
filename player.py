from colorama import Back, Style, Fore
SAFE_RESET = Style.RESET_ALL + Back.BLACK + Fore.WHITE
import inventory
inv = inventory.Inventory()

class Player:
    def __init__(self, name):
        self.name = name
        self.life = 7
        self.food = 9

    def showStats(self):
        print()
        if (len(self.name) > 17):
            self.name = self.name[:15] + "..."

        maxWidthWindow = 27
        print(' info' + '*' * (maxWidthWindow - 4) + '   inventory' + '*' * 48)

        maxLife = 10
        maxFood = 10
        emptyLife = '-' * (maxLife - self.life) 
        emptyFood = '-' * (maxFood - self.food) 
        lifeBar = '-' * self.life
        foodBar = '-' * self.food

        print((f' | name: {self.name}').ljust(maxWidthWindow) + '|   |', end='')
        inv.showInv()
        print(f' | life: [{Back.RED}{lifeBar}{SAFE_RESET}{emptyLife}] {self.life}/{maxLife} |')
        print(f' | food: [{Back.GREEN}{foodBar}{SAFE_RESET}{emptyFood}] {self.food}/{maxFood} |')

        print(' ' + '*' * maxWidthWindow)

    def takeDamage(self):
        if (self.life > -1):
            self.life -= 1

    def takeHealth(self):
        if (self.life < 11):
            self.life += 1

    def takeFood(self):
        if (self.food < 11):
            self.food += 1