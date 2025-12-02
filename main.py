import pygame
from snake import Snake
from apple import Apple
from data import BOARD_HEIGTH, BOARD_WIDTH, FRAMES, MOVES_PER_SECOND, score

pygame.init()
pygame.font.init()

font = pygame.font.SysFont("comicsans", 30)

screen = pygame.display.set_mode((BOARD_WIDTH + 200, BOARD_HEIGTH))
clock = pygame.time.Clock()
running = True

snake = Snake(BOARD_WIDTH//2, BOARD_HEIGTH//2)
apple = Apple(snake)

max_speed = FRAMES // MOVES_PER_SECOND
tick = 0
game_state = "open"

while running:
    tick += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if game_state == "play":
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            snake.turn("up")
        elif keys[pygame.K_DOWN]:
            snake.turn("down")
        elif keys[pygame.K_RIGHT]:
            snake.turn("right")
        elif keys[pygame.K_LEFT]:
            snake.turn("left")

        if tick >= max_speed:
            tick = 0
            if snake.head.rect.colliderect(apple):
                success = snake.move(True)
                if success:
                    score += 1
                apple.spawn(snake)
            else:
                success = snake.move()
            if not success:
                game_state = "death"

            screen.fill("black")
            pygame.draw.rect(screen, "blue", (0, 0, BOARD_WIDTH, BOARD_HEIGTH))
            score_text = font.render(f"Score: {score}", True, "white")
            screen.blit(score_text, (BOARD_WIDTH, 0))
            snake_direction = font.render(
                f"Direction: {snake.direction}", True, "white")
            screen.blit(snake_direction, (BOARD_WIDTH, 40))
            apple.draw(screen)
            snake.draw(screen)
    elif game_state == "open":
        screen.fill("black")
        pygame.draw.rect(screen, "blue", (0, 0, BOARD_WIDTH, BOARD_HEIGTH))
        apple.draw(screen)
        snake.draw(screen)
        welcome_text = font.render("Press arrow", True, "white")
        screen.blit(welcome_text, (BOARD_WIDTH, 0))
        welcome_text = font.render("keys to start", True, "white")
        screen.blit(welcome_text, (BOARD_WIDTH, 30))
        keys = pygame.key.get_pressed()
        if any([keys[pygame.K_DOWN], keys[pygame.K_LEFT], keys[pygame.K_RIGHT], keys[pygame.K_UP]]):
            game_state = "play"
    elif game_state == "death":
        screen.fill("black")
        pygame.draw.rect(screen, "blue", (0, 0, BOARD_WIDTH, BOARD_HEIGTH))
        apple.draw(screen)
        snake.draw(screen)
        welcome_text = font.render(f"You died", True, "white")
        screen.blit(welcome_text, (BOARD_WIDTH, 0))
        welcome_text = font.render(f"Score: {score}", True, "white")
        screen.blit(welcome_text, (BOARD_WIDTH, 30))
        welcome_text = font.render(f"use arrow keys", True, "white")
        screen.blit(welcome_text, (BOARD_WIDTH, 60))
        welcome_text = font.render(f"to try again", True, "white")
        screen.blit(welcome_text, (BOARD_WIDTH, 90))
        keys = pygame.key.get_pressed()
        if any([keys[pygame.K_DOWN], keys[pygame.K_LEFT], keys[pygame.K_RIGHT], keys[pygame.K_UP]]):
            score = 0
            snake = Snake(BOARD_WIDTH // 2, BOARD_HEIGTH // 2)
            game_state = "play"
    pygame.display.update()
    clock.tick(FRAMES)

pygame.quit()
