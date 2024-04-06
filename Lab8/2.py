import pygame, sys
from color_palette import *
import random, time

pygame.init()

WIDTH = 600
HEIGHT = 600

screen_border = pygame.Rect(0, 0, WIDTH, HEIGHT) 

SCORE = 0 #number of food

CELL = 30

#fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, colorBLACK)

#screen background
def draw_grid():
    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]
    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

screen = pygame.display.set_mode((HEIGHT, WIDTH))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)] #input position
        self.dx = 1
        self.dy = 0
        self.rect = pygame.draw.rect(screen, colorRED, (0, 0, CELL, CELL))

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        head = self.body[0]
        self.rect = pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_borders(self): #if snake goes out of borders, game over
        if not pygame.Rect.contains(screen_border, self.rect) :                  
            screen.fill(colorRED)
            screen.blit(game_over, (120, 250))
            pygame.display.update()
            time.sleep(0.2)
            pygame.quit()
            sys.exit()      

    def check_collision(self, food):
        global SCORE
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            print("Got food!")
            self.body.append(Point(head.x, head.y))
            food.change_pos(snake)
            SCORE += 1


class Food:
    def __init__(self):
        self.pos = Point(9, 9) #input position

    def change_pos(self, snake):
        self.pos = Point(random.randint(1, 18), random.randint(1, 18)) #random position
        for i in range(len(snake.body)): #check if the food in the same position as the snake
            if self.pos.x == snake.body[i].x or self.pos.y == snake.body[i].y:
                self.pos = Point(random.randint(1, 18), random.randint(1, 18))

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))


clock = pygame.time.Clock()

snake = Snake()
food = Food()

done = False
while not done:
    FPS = 3 * len(snake.body) // 3 #when snake receives 3 food, speed increases
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -1

    draw_grid_chess()

    snake.move()
    snake.check_borders()
    snake.check_collision(food)

    snake.draw()
    food.draw()
    # score and lvl output
    lvls = font_small.render(f"LVL{str(len(snake.body) // 3)}", True, colorBLACK)
    screen.blit(lvls, (10, 10))
    score = font_small.render(f"SCORE: {str(SCORE)}", True, colorBLACK)
    screen.blit(score, (480, 10))

    pygame.display.flip()
    clock.tick(FPS)