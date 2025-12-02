import pygame
import random
from data import BOARD_HEIGTH, BOARD_WIDTH, SIZE


class Apple:
    def __init__(self, snake):
        self.rect = pygame.Rect(0, 0, SIZE, SIZE)
        self.spawn(snake)

    def spawn(self, snake):
        x = snake.head.rect.x
        y = snake.head.rect.y
        while snake.point_in_snake(x, y):
            print("Oh No")
            print(x, y)
            x = random.randint(0, BOARD_WIDTH-SIZE)
            y = random.randint(0, BOARD_HEIGTH-SIZE)
            x -= x % SIZE
            y -= y % SIZE
            print(x, y)

        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.rect.center, SIZE // 2)
