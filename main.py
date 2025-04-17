from colorama import init
from objects import Water, Tree, Flower, Mine, Player, Bonfire
import windowset
import player
import map
import actions
import actionwin
import setItemChooseWin

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
map.addObj(1, Bonfire)

actTextWin = actionwin.TextAction('')
heroAction = actions.Actions(mainPlayer, hero, actTextWin)

f = True
mainWin = True
chooseItems = False
while (f):
    print('\033[H\033[J', end='', flush=True) # clear

    hero.showStats()

    if (mainWin):
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
            elif (k == 'e'):
                mainWin = False
                chooseItems = True
                break
            else:
                f = False 
                break
    else:
        if (chooseItems):
            setItemChooseWin.printItems()
            print('  -> ', end='', flush=True)
            key = input()
            for k in key:
                if k == 'q':
                    mainWin = True
                    chooseItems = False
                    break
                if k == 'w':
                    setItemChooseWin.arrow.arrowUp()
                if k == 's':
                    setItemChooseWin.arrow.arrowDown()
                if k == 'e':
                    setItemChooseWin.fakeplayer.setCoord(mainPlayer.getCoord())
                    setItemChooseWin.fakeplayer.setlook(mainPlayer.getLook())

                    if (setItemChooseWin.setObj() == False):
                        actTextWin.setText('nope')
                        actTextWin.printAction()
                    else:
                        actTextWin.setText('put')
                        actTextWin.printAction()
                    mainWin = True
                    chooseItems = False
                    break 