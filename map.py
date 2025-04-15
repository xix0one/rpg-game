import random
import objects
from objects import Water, Tree
from colorama import Back, Style, Fore
SAFE_RESET = Style.RESET_ALL + Back.BLACK + Fore.LIGHTWHITE_EX

map = []
height = 20
width = 60

objArr = []

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

addObj(2, Tree)
addObj(4, Water)
    

for y in range(height):
    arr = []
    for x in range(width):
        arr.append(' ')
    map.append(arr)

def printMap():
    print(f' {Back.LIGHTBLUE_EX}map{SAFE_RESET}' + '*' * (width - 1))
    for y in range(len(map)):
        print(' |', end='')
        for x in range(len(map[y])):
            for i in range(len(objArr)):
                coord = objArr[i].getCoord()
                if (y == coord[0] and x == coord[1]):
                    objArr[i].print()
                    break
            else:
                print(map[y][x], end='')
        print('|')
    print(' ' + '*' * (width + 2))
