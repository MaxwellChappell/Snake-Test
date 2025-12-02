
from snakepart import SnakePart
from data import SIZE


class Snake:
    def __init__(self, x, y):
        self.head = SnakePart(x, y)
        self.length = 1
        self.tail = self.head
        self.direction = "right"
        self.body = []

    def add_tail(self, x, y):
        self.tail.new_follower(SnakePart(x, y, leader=self.tail))
        self.tail = self.tail.follower
        self.body.append(self.tail)
        self.length += 1

    def move(self, grow=False):
        if grow:
            new_piece = (self.tail.rect.x, self.tail.rect.y)
        if self.direction == "right":
            self.head.lead(SIZE, 0)
        elif self.direction == "left":
            self.head.lead(-SIZE, 0)
        elif self.direction == "up":
            self.head.lead(0, -SIZE)
        elif self.direction == "down":
            self.head.lead(0, SIZE)
        if grow:
            self.add_tail(new_piece[0], new_piece[1])
        return not (self.head in self.body or self.head.out_of_board())

    def debug(self):
        piece = self.head
        for i in range(self.length):
            print(piece.rect.x, piece.rect.y, end=", ")
            piece = piece.follower
        print()

    def turn(self, direction):
        self.direction = direction

    def draw(self, screen):
        self.head.draw(screen)

    def point_in_snake(self, x, y):
        if self.head.rect.x == x and self.head.rect.y == y:
            print("head")
            return True
        for part in self.body:
            if part.rect.x == x and part.rect.y == y:
                print("body")
                return True
        return False
            
        
