import pygame
import random

pygame.init()

width, height = dimensions = (500, 500)
window = pygame.display.set_mode(dimensions)
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

BACKGROUND_COLOR = (150, 150, 150)
SNAKE_COLOR = (120,190,33)
FOOD_COLOR = (199, 55, 47)
TEXT_COLOR = (0, 0, 0)
TEXT_SIZE = 50

SNAKE_SIZE = 20
FPS = 15

font = pygame.font.SysFont("fixedsys500c", TEXT_SIZE)

class Game:
    def __init__(self):
        self.places = [[x,y] for y in range(0, height, SNAKE_SIZE) for x in range(0, width, SNAKE_SIZE)]
        
        self.start()

    def display(self):
        window.fill(BACKGROUND_COLOR)

        head = self.snake[-1]

        if head.x == self.food.x and head.y == self.food.y:
            self.generate_food()
            self.extend_snake()
            self.score += 1

        for i in self.snake:
            pygame.draw.rect(window, SNAKE_COLOR, i)
            
        pygame.draw.rect(window, FOOD_COLOR, self.food)

        text = font.render(f"Score: {self.score}", False, TEXT_COLOR)
        window.blit(text, (width//2-TEXT_SIZE-15, 0))

    def extend_snake(self):
        x, y = self.snake[-1].x, self.snake[-1].y

        self.snake.append(pygame.Rect(x+self.direction[0]*SNAKE_SIZE, y+self.direction[1]*SNAKE_SIZE, SNAKE_SIZE, SNAKE_SIZE))

    def move(self):
        self.extend_snake()
        self.snake.pop(0)

    def generate_food(self):
        self.food = pygame.Rect(*random.choice(self.places), SNAKE_SIZE, SNAKE_SIZE)

    def collision_check(self):
        head = self.snake[-1]

        if (head.x > width or head.x < 0) or (head.y > height or head.y < 0):
            self.start()

        for part in game.snake:
            if part.colliderect(head) and part is not head:
                self.start()

    def start(self):
        self.score = 0
        self.snake = [pygame.Rect(300, 0, SNAKE_SIZE, SNAKE_SIZE)]
        self.direction = [0, 1]
        self.generate_food()
        
        for _ in range(1):
            self.extend_snake()

game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            char = [event.unicode.lower(), event.key]
            
            if (char[0] == "w" or char[1] == pygame.K_UP) and game.direction != [0, 1]:
                game.direction = [0, -1]
            elif (char[0] == "s" or char[1] == pygame.K_DOWN) and game.direction != [0, -1]:
                game.direction = [0, 1]
            elif (char[0] == "a" or char[1] == pygame.K_LEFT) and game.direction != [1, 0]:
                game.direction = [-1, 0]
            elif (char[0] == "d" or char[1] == pygame.K_RIGHT) and game.direction != [-1, 0]:
                game.direction = [1, 0]
    
    game.collision_check()
    game.move()
    game.display()
    clock.tick(FPS)
    pygame.display.flip()
