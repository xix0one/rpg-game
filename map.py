import random
import helpwin
from objects import Water, Tree, Flower, Player, Shop
from colorama import Back, Style, Fore
SAFE_RESET = Style.RESET_ALL + Back.BLACK + Fore.LIGHTWHITE_EX

map = []
height = 14
width = 20

objArr = []

for y in range(height):
    arr = []
    for x in range(width):
        arr.append('  ')
    map.append(arr)

def addObj(count, objClass):
    for i in range(count):
        f = True
        while(f):
            f = False
            coordY = random.randint(0, height - 1)
            coordX = random.randint(0, width - 1)

            for i in range(len(objArr)):
                coords = objArr[i].getCoord()
                if (coords[0] == coordY and coords[1] == coordX):
                    f = True
                    break

            newObj = objClass(coordY, coordX)
            objArr.append(newObj)

def setObj(o):
    
    coordNewObj = o.getCoord()
    f = True

    if (coordNewObj[0] < 0 or coordNewObj[0] > height - 1 or
        coordNewObj[1] < 0 or coordNewObj[1] > width - 1):
        f = False
    else:
        for i in range(len(objArr)):
            coords = objArr[i].getCoord()
            if (coordNewObj[0] == coords[0] and coordNewObj[1] == coords[1]):
                f = False
                break
    
    if (f):
        objArr.append(o)
        return True
    return False

def addPlayer(p):
    objArr.append(p)

def addShop(s):
    objArr.append(s)

def printMap():
    p_in_map = False
    print(f'    {Back.LIGHTBLUE_EX}map{SAFE_RESET}' + '*' * ((width * 2) - 1), end='', flush=True)
    helpwin.printBegin()

    for y in range(len(map)):
        print('    |', end='')
        for x in range(len(map[y])):
            for i in range(len(objArr)):
                coord = objArr[i].getCoord()

                if (y == coord[0] and x == coord[1]):
                    if isinstance(objArr[i], Player):
                        p_in_map = True
                    objArr[i].print()
                    break

            else:
                print(map[y][x], end='', flush=True)
        if p_in_map:
            print('|(<-)', end='', flush=True)
            p_in_map = False
        else:
            print('|    ', end='', flush=True)

        if (y == 1):
            helpwin.printFirst()
        elif (y == 2):
            helpwin.printFirstContinue()
        elif (y == 4):
            helpwin.printArrow()
        elif (y == 6):
            helpwin.printPos()
        elif (y == 7):
            helpwin.printPosinAnotherLine()
        elif (y == 9):
            helpwin.printDescriptionObj()
        elif (y == 10):
            helpwin.printAnotherLineDescription()
        elif (y == 12):
            helpwin.printAbbr()
        elif (y == 13):
            helpwin.printNextAbbr()
        else:
            helpwin.printLine()

    print('    ' + '*' * ((width * 2) + 2), end='     ', flush=True)
    helpwin.printEnd()