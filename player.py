from colorama import Back, Style, Fore
SAFE_RESET = Style.RESET_ALL + Back.BLACK + Fore.LIGHTWHITE_EX
import inventory
inv = inventory.Inventory()

class Player:
    def __init__(self, name):
        self.name = name
        self.life = 7
        self.hung = 9

    def showStats(self):
        print()
        if (len(self.name) > 17):
            self.name = self.name[:15] + "..."

        maxWidthWindow = 27
        print(f' {Back.LIGHTBLUE_EX}info{SAFE_RESET}' + '*' * (maxWidthWindow - 4) + f'   {Back.LIGHTBLUE_EX}inventory{SAFE_RESET}' + '*' * 51)

        maxLife = 10
        maxHung = 10
        emptyLife = '-' * (maxLife - self.life) 
        emptyHung = '-' * (maxHung - self.hung) 
        lifeBar = '-' * self.life
        HungBar = '-' * self.hung

        print((f' | NAME: {self.name}').ljust(maxWidthWindow) + '|   |', end='')
        inv.showInvFirstLine()
        print(f' | LIFE: [{Back.RED}{lifeBar}{SAFE_RESET}{emptyLife}] {self.life}/{maxLife} |   | ', end='')
        inv.showInvSecondLine()
        print(f' | HUNG: [{Back.GREEN}{HungBar}{SAFE_RESET}{emptyHung}] {self.hung}/{maxHung} |   | ', end='')
        inv.showInvThirdLine()
        print(' ' + '*' * maxWidthWindow + '   ', end='')
        print('*' * 60)

    def takeDamage(self):
        if (self.life > -1):
            self.life -= 1

    def takeHealth(self):
        if (self.life < 11):
            self.life += 1

    def takeFood(self):
        if (self.hung < 11):
            self.hung += 1