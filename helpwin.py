from colorama import Back, Style, Fore
SAFE_RESET = Style.RESET_ALL + Back.BLACK + Fore.LIGHTWHITE_EX

def printBegin():
    print(f'   {Back.LIGHTBLUE_EX}help{SAFE_RESET}' + '*' * 37, flush=True)

def printFirst():
    print((f' | {Back.RED}  {SAFE_RESET}: you, move: wasd, use: f, put: e').ljust(58, ' ') + '|', flush=True)

def printPos():
    print((f' | (<-) between {Back.LIGHTBLUE_EX}map{SAFE_RESET} and {Back.LIGHTBLUE_EX}help{SAFE_RESET} - your').ljust(79, ' ') + '|', flush=True)
def printPosinAnotherLine():
    print((f' | position').ljust(39, ' ') + '|', flush=True)

def printArrow():
    print((f' | <-, ->, {chr(25)}, {chr(24)} in {Back.RED}  {SAFE_RESET} - your look').ljust(58, ' ') + '|', flush=True)

def printDescriptionObj():
    print((f' | {Back.LIGHTBLUE_EX}~{SAFE_RESET}: water, {Back.LIGHTGREEN_EX}T{SAFE_RESET}: tree, {Back.MAGENTA}*{SAFE_RESET}: flower,').ljust(98, ' ') + '|', flush=True)
def printAnotherLineDescription():
    print((f' | {Back.LIGHTCYAN_EX}^{SAFE_RESET}: mine, {Back.LIGHTYELLOW_EX}{Fore.BLACK}+{SAFE_RESET}: shop, {Back.YELLOW}"{SAFE_RESET}: bonfire').ljust(103, ' ') + '|', flush=True)

def printAbbr():
    print((f' | {Fore.LIGHTCYAN_EX}flowerS{SAFE_RESET}: flower seed,').ljust(58, ' ') + '|', flush=True)
def printNextAbbr():
    print((f' | {Fore.LIGHTMAGENTA_EX}fishC{SAFE_RESET}: fish cooked').ljust(58, ' ') + '|', flush=True)

def printLine():
    print((f' | ').ljust(39, ' ') + '|', flush=True)

def printEnd():
    print('*' * 39, flush=True)
