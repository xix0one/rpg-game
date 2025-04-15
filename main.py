from colorama import init
from objects import Water, Tree, Flower
import windowset
import player
import map

init()
windowset.defaultWindow()

name = '--hero 42--'

hero = player.PlayerInfo(name)
hero.showStats()

map.addPlayer(1, 4, 'right')
map.addObj(5, Tree)
map.addObj(3, Water)
map.addObj(7, Flower)

map.printMap()