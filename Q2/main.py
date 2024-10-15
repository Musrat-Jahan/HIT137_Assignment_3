import pygame
import random
from player import Player
from enemy import Enemy
from projectile import Projectile

# Initialize Pygame
def init_game():
    try:
        pygame.init()
    except Exception as e:
        print(f"Error initializing pygame: {e}")

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Side-Scrolling Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font for level and game over text
try:
    pygame.font.init()
    font = pygame.font.SysFont(None, 50)
except Exception as e:
    print(f"Error initializing font: {e}")

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
    """ Reset the game and start from level 1 """
    global all_sprites, projectiles, enemies, current_level, game_over
    try:
        all_sprites.empty()
        projectiles.empty()
        enemies.empty()
        current_level = 1
        game_over = False
        spawn_enemies()
    except Exception as e:
        print(f"Error resetting the game: {e}")

def spawn_enemies():
    """ Spawn enemies based on the current level, ensuring they don't spawn near or overlap the player """
    try:
        for i in range(current_level * 5):
            while True:
                x_position = random.randint(200, WIDTH - 100)  # Avoid the left where player spawns
                y_position = random.randint(50, HEIGHT - 150)
                
                # Ensure enemy doesn't overlap with player
                if abs(x_position - player.rect.x) > 100:  # Ensure at least 100px distance from player
                    break  # If valid position, exit loop

            enemy = Enemy(x_position, y_position)
            all_sprites.add(enemy)
            enemies.add(enemy)
    except Exception as e:
        print(f"Error spawning enemies: {e}")

def display_level(screen, current_level):
    """ Display the current level on the screen """
    try:
        level_text = font.render(f"Level: {current_level}", True, BLACK)
        screen.blit(level_text, (WIDTH // 2 - 100, 20))
    except Exception as e:
        print(f"Error displaying level: {e}")

def display_game_over(screen):
    """ Display the game over message on the screen """
    try:
        game_over_text = font.render("Game Over! Press R to Restart or Q to Quit", True, BLACK)
        screen.blit(game_over_text, (WIDTH // 2 - 300, HEIGHT // 2))
    except Exception as e:
        print(f"Error displaying game over screen: {e}")

def draw_life(screen, player):
    """ Draw the player's remaining lives on the screen """
    try:
        for i in range(player.lives):
            pygame.draw.rect(screen, (255, 0, 0), (10 + i * 30, 10, 20, 20))
    except Exception as e:
        print(f"Error drawing lives: {e}")

def advance_level():
    """ Advance to the next level or end the game if max levels are reached """
    global current_level, game_over, player
    try:
        if current_level < max_levels:
            current_level += 1
            print(f"Advancing to level {current_level}")
            
            all_sprites.empty()  # Clear all sprites
            projectiles.empty()  # Clear projectiles
            enemies.empty()  # Clear enemies
            
            # Reinitialize player
            player = Player(100, HEIGHT - 100, all_sprites, projectiles)  # Reset player position and health
            all_sprites.add(player)  # Add player back to sprite group
            
            spawn_enemies()  # Spawn enemies for the new level
        else:
            game_over = True
            print("Game Over!")
    except Exception as e:
        print(f"Error advancing level: {e}")

def main_game_loop():
    global current_level, game_over, player
    try:
        player = Player(100, HEIGHT - 100, all_sprites, projectiles)
        all_sprites.add(player)
        spawn_enemies()

        running = True
        while running:
            try:
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

                player.move(left, right, jump)

                if keys[pygame.K_s]:
                    player.shoot()

                enemies.update()
                projectiles.update()

                # Check for collision between projectiles and enemies
                for projectile in projectiles:
                    enemy_hit = pygame.sprite.spritecollideany(projectile, enemies)
                    if enemy_hit:
                        print("Enemy hit and killed!")
                        enemy_hit.kill()
                        projectile.kill()

                # If all enemies are killed, advance to the next level
                if len(enemies) == 0 and not game_over:
                    print("All enemies killed, advancing to the next level.")
                    advance_level()

                # Check if player collides with any visible enemies
                if pygame.sprite.spritecollideany(player, enemies):
                    print("Player collided with an enemy!")
                    player.take_damage(10)

                screen.fill(WHITE)

                # Display current level
                display_level(screen, current_level)

                # Draw all sprites
                for sprite in all_sprites:
                    screen.blit(sprite.image, sprite.rect)

                if game_over:
                    display_game_over(screen)

                draw_life(screen, player)
                pygame.display.flip()

                if not player.is_alive():
                    print("Player has died. Game Over!")
                    game_over = True

                clock.tick(FPS)

            except Exception as e:
                print(f"Error in game loop: {e}")
    except Exception as e:
        print(f"Error initializing game loop: {e}")
    finally:
        pygame.quit()

if __name__ == "__main__":
    init_game()
    main_game_loop()
