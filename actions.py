from player import inv
from map import objArr
from objects import Flower, Tree, Mine, Water

from colorama import Back, Style, Fore
SAFE_RESET = Style.RESET_ALL + Back.BLACK + Fore.LIGHTWHITE_EX

class Actions():
    def __init__(self, player, hero, textAction):
        self.player = player
        self.hero = hero
        self.textAction = textAction

    def moveRight(self):
        if (self.player.look != 'right'):
            self.player.look = 'right'
            self.textAction.setText('turn right')
        else:
            self.hero.damageHung()
            self.textAction.setText('move right, damage from hungry: 1')
            if ((self.player.x + 1) > 19):
                self.player.x = 0
            else:
                self.player.x += 1

    def moveUp(self):
        if (self.player.look != 'up'):
            self.player.look = 'up'
            self.textAction.setText('turn up')
        else:
            self.hero.damageHung()
            self.textAction.setText('move up, damage from hungry: 1')
            if ((self.player.y - 1) < 0):
                self.player.y = 13
            else:
                self.player.y -= 1

    def moveLeft(self):
        if (self.player.look != 'left'):
            self.player.look = 'left'
            self.textAction.setText('turn left')
        else:
            self.hero.damageHung()
            self.textAction.setText('move left, damage from hungry: 1')
            if ((self.player.x - 1) < 0):
                self.player.x = 19
            else:
                self.player.x -= 1

    def moveDown(self):
        if (self.player.look != 'down'):
            self.player.look = 'down'
            self.textAction.setText('turn down')
        else:
            self.hero.damageHung()
            self.textAction.setText('move down, damage from hungry: 1')
            if ((self.player.y + 1) > 13):
                self.player.y = 0
            else:
                self.player.y += 1

    def use(self):
        coords = self.player.getCoord()
        if (self.player.look == 'right'): coords[1] += 1
        if (self.player.look == 'left'): coords[1] -= 1
        if (self.player.look == 'up'): coords[0] -= 1
        if (self.player.look == 'down'): coords[0] += 1

        for i in range(len(objArr)):
            if (objArr[i].getCoord() == coords):

                if isinstance(objArr[i], Flower):
                    inv.addFlower()
                    objArr[i].reductionReserve()
                    if inv.addflowerSeed():
                        if (objArr[i].getReserve() == 0):
                            self.textAction.setText(f'take flower + 2 and {Fore.LIGHTCYAN_EX}+ 1 flower seed!{SAFE_RESET}; total flower: {inv.getTotal("flower")}, flower seed: {inv.getTotal("flowerSeed")}; flower destroyed!', 112)
                            objArr.pop(i)
                        else:
                            self.textAction.setText(f'take flower + 2 and {Fore.LIGHTCYAN_EX}+ 1 flower seed!{SAFE_RESET}; total flower: {inv.getTotal("flower")}, flower seed: {inv.getTotal("flowerSeed")}; reserve: {objArr[i].getReserve()}', 112)
                    else:
                        if (objArr[i].getReserve() == 0):
                            self.textAction.setText(f'take flower + 2; total: {inv.getTotal("flower")}; flower destroyed')
                            objArr.pop(i)
                        else:
                            self.textAction.setText(f'take flower + 2; total: {inv.getTotal("flower")}; reserve: {objArr[i].getReserve()}')

                    break

                if isinstance(objArr[i], Tree):
                    inv.addWood()
                    objArr[i].reductionReserve()
                    if (objArr[i].getReserve() == 0):
                        self.textAction.setText(f'take wood + 3; total: {inv.getTotal("wood")}; tree destroyed!')
                        objArr.pop(i)
                    else:
                        self.textAction.setText(f'take wood + 3; total: {inv.getTotal("wood")}; reserve: {objArr[i].getReserve()}')
                    break

                if isinstance(objArr[i], Water):
                    objArr[i].reductionReserve()
                    if (objArr[i].getReserve() == 0):
                        if (inv.addFish()):
                            self.textAction.setText(f'take fish + 1; total fish: {inv.getTotal("fish")}; water destroyed!')
                            objArr.pop(i)
                        else:
                            self.textAction.setText(f'didnt catch; total fish: {inv.getTotal("fish")}; water destroyed!')
                            objArr.pop(i)
                    else:
                        if (inv.addFish()):
                            self.textAction.setText(f'take fish + 1; total fish: {inv.getTotal("fish")}; reserve: {objArr[i].getReserve()}')
                        else:
                            self.textAction.setText(f'didnt catch; total fish: {inv.getTotal("fish")}; reserve: {objArr[i].getReserve()}')
                    break

                if isinstance(objArr[i], Mine):
                    inv.addIron()
                    objArr[i].reductionReserve()
                    if inv.addGold():
                        if (objArr[i].getReserve() == 0):
                            self.textAction.setText(f'take iron + 1 and {Fore.YELLOW}+ 1 gold!{SAFE_RESET}; total iron: {inv.getTotal("iron")}, gold: {inv.getTotal("gold")}; mine destroyed!', 112)
                            objArr.pop(i)
                        else:
                            self.textAction.setText(f'take iron + 1 and {Fore.YELLOW}+ 1 gold!{SAFE_RESET}; total iron: {inv.getTotal("iron")}, gold: {inv.getTotal("gold")}; reserve: {objArr[i].getReserve()}', 112)
                    else:
                        if (objArr[i].getReserve() == 0):
                            self.textAction.setText(f'take iron + 1; total: {inv.getTotal("iron")}; mine destroyed!')
                            objArr.pop(i)
                        else:
                            self.textAction.setText(f'take iron + 1; total: {inv.getTotal("iron")}; reserve: {objArr[i].getReserve()}')
                    break
                    
                
        