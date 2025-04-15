from colorama import Back, Style, Fore
SAFE_RESET = Style.RESET_ALL + Back.BLACK + Fore.LIGHTWHITE_EX

def printBegin():
    print(f'   {Back.LIGHTBLUE_EX}help{SAFE_RESET}' + '*' * 32)

def printFirst():
    print((f' | {Back.RED}  {SAFE_RESET} - you').ljust(53, ' ') + '|')

def printPos():
    print((f' | (<-) between {Back.LIGHTBLUE_EX}map{SAFE_RESET} and {Back.LIGHTBLUE_EX}help{SAFE_RESET} - ').ljust(74, ' ') + '|')
def printPosinAnotherLine():
    print((f' | your position').ljust(34, ' ') + '|')

def printArrow():
    print((f' | <-, ->, {chr(25)}, {chr(24)} in {Back.RED}  {SAFE_RESET} - you look').ljust(53, ' ') + '|')

def printDescriptionObj():
    print((f' | {Back.LIGHTBLUE_EX}~{SAFE_RESET}: water, {Back.LIGHTGREEN_EX}T{SAFE_RESET}: tree, {Back.MAGENTA}*{SAFE_RESET}: flower').ljust(93, ' ') + '|')

def printLine():
    print((f' | ').ljust(34, ' ') + '|')

def printEnd():
    print('*' * 34)
