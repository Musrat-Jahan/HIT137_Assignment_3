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
        self.image.fill((0, 255, 0))  # Green color for player
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.vel_y = 0
        self.health = 100  # Reset health at the start of each level
        self.lives = 3  # Player starts with 3 lives
        self.all_sprites = all_sprites
        self.projectiles = projectiles
        self.on_ground = True

    def move(self, left, right, jumping):
        # Horizontal movement
        if left and self.rect.left > 0:
            self.rect.x -= PLAYER_SPEED
        if right and self.rect.right < WIDTH:
            self.rect.x += PLAYER_SPEED

        # Apply gravity
        self.vel_y += GRAVITY

        # Jump if on the ground
        if jumping and self.on_ground:
            self.vel_y = -JUMP_STRENGTH
            self.on_ground = False

        # Update position
        self.rect.y += self.vel_y

        # Ground collision (simple check)
        if self.rect.bottom >= 600:  # Assume the ground is at y = 600
            self.rect.bottom = 600
            self.on_ground = True
            self.vel_y = 0

    def shoot(self):
        """Player shooting logic"""
        projectile = Projectile(self.rect.centerx, self.rect.centery)
        self.all_sprites.add(projectile)
        self.projectiles.add(projectile)

    def take_damage(self, damage):
        """Player takes damage and loses health"""
        self.health -= damage
        print(f"Player took {damage} damage. Health remaining: {self.health}")
        if self.health <= 0:
            self.lives -= 1
            self.health = 100  # Reset health for the next life
            print(f"Player lost a life. Lives remaining: {self.lives}")
        if self.lives <= 0:
            print("Player is dead!")

    def is_alive(self):
        return self.lives > 0
