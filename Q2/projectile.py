import pygame

PROJECTILE_SPEED = 10

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 5))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.x += PROJECTILE_SPEED
        if self.rect.left > 800:
            self.kill()
