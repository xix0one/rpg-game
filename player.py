from colorama import Back, Style, Fore
SAFE_RESET = Style.RESET_ALL + Back.BLACK + Fore.LIGHTWHITE_EX
import inventory
inv = inventory.Inventory()

class PlayerInfo:
    def __init__(self, name):
        self.name = name
        self.life = 10
        self.hung = 6

    def showStats(self):
        print()
        if (len(self.name) > 17):
            self.name = self.name[:15] + "..."

        maxWidthWindow = 28
        print(f' {Back.LIGHTBLUE_EX}info{SAFE_RESET}' + '*' * (maxWidthWindow - 4) + f'     {Back.LIGHTBLUE_EX}inventory{SAFE_RESET}' + '*' * 52, flush=True)

        maxLife = 10
        maxHung = 10
        emptyLife = '-' * (maxLife - self.life) 
        emptyHung = '-' * (maxHung - self.hung) 
        lifeBar = '-' * self.life
        HungBar = '-' * self.hung

        print((f' | NAME: {self.name} ').ljust(maxWidthWindow) + '|', end='', flush=True)
        inv.showInvFirstLine()
        print((f' | LIFE: [{Back.RED}{lifeBar}{SAFE_RESET}{emptyLife}] {self.life}/{maxLife}').ljust(47) + '|', end='', flush=True)
        inv.showInvSecondLine()
        print((f' | HUNG: [{Back.GREEN}{HungBar}{SAFE_RESET}{emptyHung}] {self.hung}/{maxHung}').ljust(47) + '|', end='', flush=True)
        inv.showInvThirdLine()
        print(' ' + '*' * maxWidthWindow + '     | ', end='', flush=True)
        inv.showInvFourthLine()
        print(' '.ljust(34) + ('*' * 61))

    def takeHealth(self):
        if (self.life < 10):
            self.life += 1
        if (self.hung < 10):
            self.hung += 1

    def damageHung(self):
        if (self.hung > 0):
            self.hung -= 1
        else:
            if (self.life > 0):
                self.life -= 1

    def getHealth(self):
        return self.life
            