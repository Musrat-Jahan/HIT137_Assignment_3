import pygame
import random
from player import Player
from enemy import Enemy
from projectile import Projectile

# Initialize Pygame
def init_game():
    pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Side-Scrolling Game")

# Colors
WHITE = (255, 255, 255)

# Clock and FPS
clock = pygame.time.Clock()
FPS = 60

# Sprite groups
all_sprites = pygame.sprite.Group()
projectiles = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# Game variables
current_level = 1
max_levels = 3
game_over = False

def reset_game():
    global all_sprites, projectiles, enemies, current_level, game_over
    all_sprites.empty()
    projectiles.empty()
    enemies.empty()
    current_level = 1
    game_over = False
    spawn_enemies()

def spawn_enemies():
    for i in range(current_level * 5):
        enemy = Enemy(random.randint(WIDTH // 2, WIDTH + 500), random.randint(50, HEIGHT - 100))
        all_sprites.add(enemy)
        enemies.add(enemy)

def draw_life(screen, player):
    for i in range(player.lives):
        pygame.draw.rect(screen, (255, 0, 0), (10 + i * 30, 10, 20, 20))

def main_game_loop():
    global current_level, game_over
    player = Player(100, HEIGHT - 100, all_sprites, projectiles)
    all_sprites.add(player)
    spawn_enemies()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and game_over:
                    reset_game()
                elif event.key == pygame.K_q:
                    running = False

        # Handle player input
        keys = pygame.key.get_pressed()
        left = keys[pygame.K_LEFT]
        right = keys[pygame.K_RIGHT]
        jump = keys[pygame.K_SPACE]

        # Move the player
        player.move(left, right, jump)

        if keys[pygame.K_s]:
            player.shoot()

        # Update enemies and projectiles
        enemies.update()
        projectiles.update()

        # Check for collision between projectiles and enemies
        for projectile in projectiles:
            enemy_hit = pygame.sprite.spritecollideany(projectile, enemies)
            if enemy_hit:
                enemy_hit.kill()
                projectile.kill()

        if pygame.sprite.spritecollideany(player, enemies):
            player.take_damage(10)

        # Clear screen
        screen.fill(WHITE)

        # Draw all sprites without camera logic
        for sprite in all_sprites:
            screen.blit(sprite.image, sprite.rect)

        draw_life(screen, player)
        pygame.display.flip()

        if not player.is_alive():
            game_over = True
            break

        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    init_game()
    main_game_loop()
