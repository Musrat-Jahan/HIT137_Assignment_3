import pygame
import random
from enemy import Enemy
from collectible import Collectible

class Level:
    def __init__(self, level_num):
        self.level_num = level_num
        self.enemies = pygame.sprite.Group()
        self.collectibles = pygame.sprite.Group()
        self.spawn_enemies()

    def spawn_enemies(self):
        for i in range(self.level_num * 5):
            enemy = Enemy(random.randint(800, 1000), random.randint(50, 550))
            self.enemies.add(enemy)

    def spawn_collectibles(self):
        for i in range(self.level_num * 3):
            collectible = Collectible(random.randint(100, 700), random.randint(50, 550), random.choice(['health', 'life']))
            self.collectibles.add(collectible)
