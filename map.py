import random
import helpwin
from objects import Water, Tree, Flower, Player
from colorama import Back, Style, Fore
SAFE_RESET = Style.RESET_ALL + Back.BLACK + Fore.LIGHTWHITE_EX

map = []
height = 20
width = 25

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

def addPlayer(y, x, look):
    p = Player(y, x, look)
    objArr.append(p)

def printMap():
    p_in_map = False
    print(f' {Back.LIGHTBLUE_EX}map{SAFE_RESET}' + '*' * ((width * 2) - 1), end='')
    helpwin.printBegin()

    for y in range(len(map)):
        print(' |', end='')
        for x in range(len(map[y])):
            for i in range(len(objArr)):
                coord = objArr[i].getCoord()

                if (y == coord[0] and x == coord[1]):
                    if isinstance(objArr[i], Player):
                        p_in_map = True
                    objArr[i].print()
                    break

            else:
                print(map[y][x], end='')
        if p_in_map:
            print('|(<-)', end='')
            p_in_map = False
        else:
            print('|    ', end='')

        if (y == 1):
            helpwin.printFirst()
        elif (y == 3):
            helpwin.printArrow()
        elif (y == 5):
            helpwin.printPos()
        elif (y == 6):
            helpwin.printPosinAnotherLine()
        elif (y == 8):
            helpwin.printDescriptionObj()
            
        else:
            helpwin.printLine()

    print(' ' + '*' * ((width * 2) + 2), end='     ')
    helpwin.printEnd()