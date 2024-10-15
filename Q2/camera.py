class Camera:
    def __init__(self, player):
        self.player = player
        self.offset_x = 0

    def update(self):
        self.offset_x = self.player.rect.x - 400

    def apply(self, sprite):
        sprite.rect.x -= self.offset_x
