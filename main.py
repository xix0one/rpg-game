from colorama import init, Back, Style
import windowset
import player
import inventory

init()
windowset.defaultWindow()

name = '--hero 42--'

hero = player.Player(name)
hero.showStats()

inv = inventory.Inventory()
inv.showInv()
inv.buy("tree")
inv.showInv()



# def water():
#     print(Back.BLUE + "~" + Style.RESET_ALL, end='')
