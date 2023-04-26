import pygame
import random

pygame.init()

size = (x, y) = (400, 400)

screen = pygame.display.set_mode(size)

pygame.display.set_caption('Snake')

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK =(0,0,0)

class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 20
        self.radius = 20
        self.elememts = [[x, y]]
        self.direction = "down"
        self.score = 0

    def draw(self):
        # for i in self.elememts:
            pygame.draw.circle(screen, RED, (self.x, self.y), self.radius)
    def eat(self, food):
        if abs(self.x - food.x)<=20 and abs(self.y - food.y)<=20:
            self.score += 1
            food.generate()
            food.draw()
            print(self.score)
    def gameover(self):
        pygame.quit()

    def changeDirection(self, changeDir):
        if changeDir == "right" and self.direction != "left":
            self.direction = "right"
        elif changeDir == "left" and self.direction != "right":
            self.direction = "left"
        elif changeDir == "down" and self.direction != "up":
            self.direction = "down"
        elif changeDir == "up" and self.direction != "down":
            self.direction = "up"

    def move(self):
        if self.direction == 'down':
            if self.y > 365:
                self.gameover()
            else:
                self.y += self.speed
        elif self.direction == 'up':
            if self.y < 25:
                self.gameover()
            else:
                self.y -= self.speed
        elif self.direction == 'right':
            if self.x > 365:
                self.gameover()
            else:
                self.x += self.speed
        elif self.direction == 'left':
            if self.x < 25:
                self.gameover()
            else:
                self.x -= self.speed


class SalamBro:
    def __init__(self):
        self.x = random.randint(0, 400)
        self.y = random.randint(0, 400)

    def draw(self):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, 10, 10))

    def generate(self):
        self.x = random.randint(0, 400)
        self.y = random.randint(0, 400)

s = Snake(20, 20)
f = SalamBro()

done = False

screen.fill(WHITE)
s.draw()
f.draw()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                s.changeDirection("right")
                s.move()
            elif event.key == pygame.K_LEFT:
                s.changeDirection("left")
                s.move()
            elif event.key == pygame.K_DOWN:
                s.changeDirection("down")
                s.move()
            elif event.key == pygame.K_UP:
                s.changeDirection("up")
                s.move()
    pygame.draw.line(screen, BLACK, (1, 1), (399, 1), 2)
    pygame.draw.line(screen, BLACK, (1, 1), (1, 399), 2)
    pygame.draw.line(screen, BLACK, (1, 399), (399, 399), 2)
    pygame.draw.line(screen, BLACK, (399, 1), (399, 399), 2)
    screen.fill(WHITE)
    s.draw()
    f.draw()
    s.eat(f)
    pygame.display.update()
pygame.quit()