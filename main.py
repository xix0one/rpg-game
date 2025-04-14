from colorama import init, Back, Style
import windowset
import player

init()
windowset.defaultWindow()

name = '--hero 42--'

hero = player.Player(name)

hero.showStats()

# def water():
#     print(Back.BLUE + "~" + Style.RESET_ALL, end='')
