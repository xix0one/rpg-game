from player import inv

class Actions():
    def __init__(self, player, hero):
        self.player = player
        self.hero = hero

    def moveRight(self):
        if (self.player.look != 'right'):
            self.player.look = 'right'
        else:
            self.hero.damageHung()
            if ((self.player.x + 1) > 19):
                self.player.x = 0
            else:
                self.player.x += 1

    def moveUp(self):
        if (self.player.look != 'up'):
            self.player.look = 'up'
        else:
            self.hero.damageHung()
            if ((self.player.y - 1) < 0):
                self.player.y = 13
            else:
                self.player.y -= 1

    def moveLeft(self):
        if (self.player.look != 'left'):
            self.player.look = 'left'
        else:
            self.hero.damageHung()
            if ((self.player.x - 1) < 0):
                self.player.x = 19
            else:
                self.player.x -= 1

    def moveDown(self):
        if (self.player.look != 'down'):
            self.player.look = 'down'
        else:
            self.hero.damageHung()
            if ((self.player.y + 1) > 13):
                self.player.y = 0
            else:
                self.player.y += 1

    def use(self):
        inv.addItem()