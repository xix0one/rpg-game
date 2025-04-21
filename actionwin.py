from colorama import Back, Style, Fore
SAFE_RESET = Style.RESET_ALL + Back.BLACK + Fore.LIGHTWHITE_EX

class TextAction():
    def __init__(self, text, width=94):
        self.text = text
        self.width = width

    def setText(self, text, width=94):
        self.text = text
        self.width = width

    def printAction(self):
        print()
        print(f' {Back.LIGHTBLUE_EX}history{SAFE_RESET}' + '*' * 87)
        print((f' | {self.text}').ljust(self.width) + '|')
        print(' ' + '*' * 94)
        print()
        