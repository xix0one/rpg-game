from setItemChooseWin import actTextWin, arrow
from player import inv
from colorama import Back, Style, Fore
SAFE_RESET = Style.RESET_ALL + Back.BLACK + Fore.LIGHTWHITE_EX

itemsBuy = {}

def updateItems():
    global itemsBuy
    itemsBuy = {
        'flower'    : inv.getTotal('flower'),
        'wood'      : inv.getTotal('wood'),
        'iron'      : inv.getTotal('iron'),
        'gold'      : inv.getTotal('gold'),
        'fish'      : inv.getTotal('fish'),
        'cookedFish': inv.getTotal('cookedFish'),

        'tree'       : inv.getCost("tree"),
        'water'      : inv.getCost("water"),  
        'mine'       : inv.getCost("mine"),
        'flowerSeed' : inv.getCost("flowerSeed"),
        'bonfire'    : inv.getCost("bonfire"),
        'food'       : inv.getCost("food")
    }

textInfo = 'choose item; w or s - move arrow; e - buy/sell item; q - exit'

def printShop():
    actTextWin.setText(textInfo)
    actTextWin.printAction()
    updateItems()

    arrow.setCountObj(len(itemsBuy) - 1)

    print(('\t' + f'{Back.LIGHTBLUE_EX}sell{SAFE_RESET}' + '-' * 26))
    print('\t| item        | inv   | cost |')
    print('\t' + '-' * 30)

    for i, (item_name, item_cost) in enumerate(itemsBuy.items()):
        if (i < 6):
            if (i == arrow.getPos()):
                print('\t|' + (f' {item_name}').ljust(12, ' ') + (f' | {item_cost}').ljust(8, ' ') + (f' | {inv.getCost(item_name)}').ljust(8) + '| <-')
            else:
                print('\t|' + (f' {item_name}').ljust(12, ' ') + (f' | {item_cost}').ljust(8, ' ') + (f' | {inv.getCost(item_name)}').ljust(8) + '|')
        elif (i == 6):
            print('\t' + '-' * 30)
            print('\t' + f'{Back.LIGHTBLUE_EX}buy{SAFE_RESET}' + '-' * 19)
            print('\t| item        | cost |')
            print('\t' + '-' * 22)
            if (i == arrow.getPos()):
                print('\t|' + (f' {item_name}').ljust(12, ' ') + (f' | {item_cost}').ljust(8, ' ') + '| <-')
            else:
                print('\t|' + (f' {item_name}').ljust(12, ' ') + (f' | {item_cost}').ljust(8, ' ') + '|')
        else:
            if (i == arrow.getPos()):
                print('\t|' + (f' {item_name}').ljust(12, ' ') + (f' | {item_cost}').ljust(8, ' ') + '| <-')
            else:
                print('\t|' + (f' {item_name}').ljust(12, ' ') + (f' | {item_cost}').ljust(8, ' ') + '|')
        
    print('\t' + '-' * 22)

def buySellItem():
    global textInfo
    updateItems()
    selectedKey = list(itemsBuy.keys())[arrow.getPos()]
    if (arrow.getPos() < 6):
        if (inv.getTotal(selectedKey) > 0):
            inv.sell(selectedKey)
            inv.reduceTotal(selectedKey)
            textInfo = f'you sell {selectedKey}'
        else:
            textInfo = f'you cant do it'
    else:
        if (inv.buy(selectedKey)):
            textInfo = f'you buy {selectedKey}'
        else:
            textInfo = f'need more money'