from colorama import init
from objects import Water, Tree, Flower, Mine, Player, Bonfire
import windowset
import player
import map
import actions
import actionwin
import setItemChooseWin
import shopWinBuy

init()
windowset.defaultWindow()

print("*** enter name *** -> ", end='')
n = input()
hero = player.PlayerInfo(n)

def loop():
    mainPlayer = Player(0, 18, 'right')

    map.addPlayer(mainPlayer)
    map.addShop(actions.shop)
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
    shopWin = False

    while (f and hero.getHealth()):
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
                elif (k == 'f'): 
                    heroAction.use()
                    if (actions.shop.getChoose()):
                        mainWin = False
                        shopWin = True
                        break
                elif (k == 'r'): heroAction.eat()
                elif (k == 'e'):
                    mainWin = False
                    chooseItems = True
                    break
                elif (k == 'q'):
                    f = False 
                    break
                else:
                    actTextWin.setText("unknown command")
                    actTextWin.printAction()
        elif (chooseItems):
            setItemChooseWin.printItems()
            print('  -> ', end='', flush=True)
            key = input()
            for k in key:
                if k == 'q':
                    mainWin = True
                    chooseItems = False
                    setItemChooseWin.arrow.setPos(0)
                    break
                if k == 'w':
                    setItemChooseWin.arrow.arrowUp()
                if k == 's':
                    setItemChooseWin.arrow.arrowDown()
                if k == 'e':
                    setItemChooseWin.fakeplayer.setCoord(mainPlayer.getCoord())
                    setItemChooseWin.fakeplayer.setlook(mainPlayer.getLook())
                    if (setItemChooseWin.setObj() == False):
                        actTextWin.setText('you cant do it')
                        actTextWin.printAction()
                    else:
                        actTextWin.setText('item put')
                        actTextWin.printAction()
                    mainWin = True
                    chooseItems = False
                    setItemChooseWin.arrow.setPos(0)
                    break
        elif (shopWin):
            shopWinBuy.printShop()
            print('  -> ', end='', flush=True)
            key = input()
            for k in key:
                if k == 'q':
                    actions.shop.setChoose(False)
                    mainWin = True
                    shopWin = False
                    shopWinBuy.textInfo = 'choose item; w or s - move arrow; e - buy/sell item; q - exit'
                    setItemChooseWin.arrow.setPos(0)
                    break
                if k == 'w':
                    setItemChooseWin.arrow.arrowUp()
                if k == 's':
                    setItemChooseWin.arrow.arrowDown()
                if k == 'e':
                    shopWinBuy.buySellItem()

loop()

print('\033[H\033[J', end='', flush=True) # clear
hero.showStats()
map.printMap()
if (hero.getHealth() < 1):
    print("\t*** you lose ***")
