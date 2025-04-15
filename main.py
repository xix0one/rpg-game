from colorama import init, Back, Style
import windowset
import player
import map

init()
windowset.defaultWindow()

name = '--hero 42--'

hero = player.Player(name)
hero.showStats()
map.printMap()

