import pygame
from data import SIZE, BOARD_HEIGTH, BOARD_WIDTH

class SnakePart:
    def __init__(self, x, y, leader = None, follower = None):
        self.rect = pygame.Rect(x, y, SIZE, SIZE)
        self.follower = follower
        self.leader = leader

    def follow(self):
        if self.follower:
            self.follower.follow()
        self.rect.x = self.leader.rect.x
        self.rect.y = self.leader.rect.y


    def lead(self, dx, dy):
        if self.follower:
            self.follower.follow()
        self.rect.x += dx
        self.rect.y += dy


    def new_follower(self, follower):
        self.follower = follower

    def new_leader(self, leader):
        self.leader = leader

    def draw(self, screen):
        pygame.draw.circle(screen, "green", self.rect.center, SIZE//2)
        if self.follower:
            self.follower.draw(screen)

    def __eq__(self, other):
        return (self.rect == other.rect)
    
    def __str__(self):
        return str(self.rect.x) + ", " + str(self.rect.y)
    
    def out_of_board(self):
        return self.rect.x >= BOARD_WIDTH or self.rect.y > BOARD_HEIGTH or self.rect.y < 0 or self.rect.x < 0


    