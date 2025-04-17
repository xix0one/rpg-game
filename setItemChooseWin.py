from player import inv
import actionwin
import map
from objects import Water, Tree, Flower, Mine, Player, Bonfire

from colorama import Back, Style, Fore
SAFE_RESET = Style.RESET_ALL + Back.BLACK + Fore.LIGHTWHITE_EX

actTextWin = actionwin.TextAction('')

class Arrow():
    def __init__(self):
        self.pos = 0

    def arrowUp(self):
        if (self.pos > 0):
            self.pos -= 1
        else:
            self.pos = 4

    def arrowDown(self):
        if (self.pos < 4):
            self.pos += 1
        else:
            self.pos = 0

    def getPos(self):
        return self.pos
    
arrow = Arrow()

def printItems():
    items =  [f' tree        | {inv.getTotal("tree")}', f' water       | {inv.getTotal("water")}', 
              f' mine        | {inv.getTotal("mine")}', f' flower seed | {inv.getTotal("flowerSeed")}',
              f' bonfire     | {inv.getTotal("bonfire")}']
    
    actTextWin.setText('choose item; w or s - move arrow; e - set item; q - exit')
    actTextWin.printAction()

    print('\t' + '-' * 23)
    print('\t| item        | count |')
    print('\t' + '-' * 23)
    for i in range(len(items)):
        if (i == arrow.getPos()):
            print(('\t|' + items[i]).ljust(23, ' ') + '| <-')
        else:
            print(('\t|' + items[i]).ljust(23, ' ') + '|')
    print('\t' + '-' * 23)

class Fakeplayer():
    def __init__(self):
        self.y = 1
        self.x = 1
        self.look = ''

    def setCoord(self, coord):
        self.y = coord[0]
        self.x = coord[1]

    def setlook(self, look):
        self.look = look

    def getLook(self):
        return self.look
    
    def getCoord(self):
        return [self.y, self.x]
    
fakeplayer = Fakeplayer()

def setObj():
    coordPlayer = fakeplayer.getCoord()
    if (fakeplayer.getLook() == 'left'):
        coordPlayer[1] -= 1
    elif (fakeplayer.getLook() == 'up'):
        coordPlayer[0] -= 1
    elif (fakeplayer.getLook() == 'down'):
        coordPlayer[0] += 1
    elif (fakeplayer.getLook() == 'right'):
        coordPlayer[1] += 1

    if (arrow.getPos() == 0):
        if (inv.getTotal('tree')):
            tree = Tree(coordPlayer[0], coordPlayer[1])
            f = map.setObj(tree)
            if (f): inv.reduceTotal('tree')
        else: f = False

    elif (arrow.getPos() == 1):
        if (inv.getTotal('water')):
            water = Water(coordPlayer[0], coordPlayer[1])
            f = map.setObj(water)
            if (f): inv.reduceTotal('water')
        else: f = False

    elif (arrow.getPos() == 2):
        if (inv.getTotal('mine')):
            mine = Mine(coordPlayer[0], coordPlayer[1])
            f = map.setObj(mine)
            if (f): inv.reduceTotal('mine')
        else: f = False

    elif (arrow.getPos() == 3):
        if (inv.getTotal('flowerSeed')):
            flower = Flower(coordPlayer[0], coordPlayer[1])
            f = map.setObj(flower)
            if (f): inv.reduceTotal('flowerSeed')
        else: f = False

    elif (arrow.getPos() == 4):
        if (inv.getTotal('bonfire')):
            bonfire = Bonfire(coordPlayer[0], coordPlayer[1])
            f = map.setObj(bonfire)
            if (f): inv.reduceTotal('flowerSeed')
            inv.reduceTotal('bonfire')
        else: f = False

    return f