import pygame

def game_over_screen():
    font = pygame.font.SysFont(None, 74)
    text_surface = font.render('Game Over', True, (255, 255, 255))
    screen = pygame.display.get_surface()
    screen.blit(text_surface, (400 - 100, 300 - 50))

    restart_text = "Press R to Restart"
    restart_surface = font.render(restart_text, True, (255, 255, 255))
    screen.blit(restart_surface, (400 - 150, 300 + 50))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False
