import pygame

class Collectible(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        if type == 'health':
            self.image.fill((0, 255, 0))
        elif type == 'life':
            self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.type = type

    def apply(self, player):
        if self.type == 'health':
            player.health += 20
        elif self.type == 'life':
            player.lives += 1
        self.kill()
