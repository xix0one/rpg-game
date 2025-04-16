from colorama import init
from objects import Water, Tree, Flower, Mine, Player
import windowset
import player
import map
import actions
import actionwin

init()
windowset.defaultWindow()

n = '--hero 42--'

hero = player.PlayerInfo(n)
mainPlayer = Player(1, 10, 'right')

map.addPlayer(mainPlayer)
map.addShop(0, 19)
map.addObj(2, Tree)
map.addObj(1, Water)
map.addObj(3, Flower)
map.addObj(1, Mine)

actTextWin = actionwin.TextAction('')
heroAction = actions.Actions(mainPlayer, hero, actTextWin)

# fix flower !!!

f = True
while (f):
    print('\033[H\033[J', end='', flush=True) # clear

    hero.showStats()
    actTextWin.printAction()
    map.printMap()

    print(' -> ', end='', flush=True)
    key = input()

    for k in key:
        if (k == 'd'): heroAction.moveRight()
        elif (k == 'w'): heroAction.moveUp()
        elif (k == 'a'): heroAction.moveLeft()
        elif (k == 's'): heroAction.moveDown()
        elif (k == 'f'): heroAction.use()
        else:
            f = False 
            break
