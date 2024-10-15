import pygame
import random

ENEMY_SPEED = 3  # Enemy speed

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        try:
            self.image = pygame.Surface((50, 50))
            self.image.fill((255, 0, 0))  # Red for enemies
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
            self.direction = random.choice([-1, 1])  # Random left or right movement direction
        except Exception as e:
            print(f"Error initializing enemy: {e}")

    def update(self):
        try:
            # Independent enemy movement
            self.rect.x += self.direction * ENEMY_SPEED

            # Reverse direction if hitting screen edges
            if self.rect.right >= 800 or self.rect.left <= 0:
                self.direction *= -1  # Reverse direction
        except Exception as e:
            print(f"Error moving enemy: {e}")
