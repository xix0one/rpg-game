from colorama import init
from objects import Water, Tree, Flower, Mine, Player
import windowset
import player
import map
import actions

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

heroAction = actions.Actions(mainPlayer, hero)

while (1):
    print('\033[H\033[J', end='', flush=True) # clear

    hero.showStats()
    map.printMap()

    print(' -> ', end='', flush=True)
    key = input()

    if (key == 'd'): heroAction.moveRight()
    elif (key == 'w'): heroAction.moveUp()
    elif (key == 'a'): heroAction.moveLeft()
    elif (key == 's'): heroAction.moveDown()
    elif (key == 'f'): heroAction.use()
    else: 
        break