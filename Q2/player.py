import pygame
from projectile import Projectile

# Player constants
PLAYER_SPEED = 7  # Increased speed for faster left/right movement
JUMP_STRENGTH = 32  # Increased jump strength for higher jumps
GRAVITY = 1  # Gravity that pulls the player down smoothly

# Screen dimensions
WIDTH = 800
HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, all_sprites, projectiles):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))  # Green for player
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.vel_y = 0
        self.on_ground = True  # Tracks whether the player is on the ground
        self.all_sprites = all_sprites
        self.projectiles = projectiles
        self.lives = 3
        self.health = 100

    def move(self, left, right, jumping):
        # Apply gravity every frame
        self.vel_y += GRAVITY

        # Allow horizontal movement
        if left and self.rect.left > 0:
            self.rect.x -= PLAYER_SPEED
        if right and self.rect.right < WIDTH:
            self.rect.x += PLAYER_SPEED

        # Jumping logic
        if jumping and self.on_ground:
            self.vel_y = -JUMP_STRENGTH  # Apply upward velocity for higher jump
            self.on_ground = False

        # Apply velocity to the player's position (both gravity and jump effect)
        self.rect.y += self.vel_y

        # Ensure player doesn't fall below ground level
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.vel_y = 0
            self.on_ground = True  # Player is grounded again

    def shoot(self):
        projectile = Projectile(self.rect.centerx, self.rect.centery)
        self.all_sprites.add(projectile)
        self.projectiles.add(projectile)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.lives -= 1
            self.health = 100

    def is_alive(self):
        return self.lives > 0
