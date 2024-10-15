import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 0, 0))  # Enemy color: Red
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed_x = random.choice([-2, 2])  # Move randomly left or right

    def update(self):
        self.rect.x += self.speed_x

        # Bounce off the edges of the screen instead of being removed
        if self.rect.left <= 0 or self.rect.right >= 800:  # Screen width is 800
            print("Enemy bounced off the edge of the screen.")
            self.speed_x *= -1  # Reverse direction (bounce)

