import pygame
from time import sleep
from random import randint as rand

FPS = 60

class MAIN:
    def __init__(self):
        self.width = 600
        self.height = 600
        self.window = pygame.display.set_mode((self.width, self.height))
        self.w = 25
        self.h = 25
        self.rand_width = rand(40, self.width-40)
        self.rand_height = rand(40, self.height-40)
        self.random = [self.rand_width, self.rand_height]
        self.distance = 1
        self.default_body_length = 5
        self.body_length = self.default_body_length
        self.body = []
        self.facing = 'up'

    def create(self):
        for i in range(self.body_length):
            self.body.insert(0, pygame.Rect(self.width/2-50, self.height/2-50+((self.distance + self.h)*i),self.w, self.h))
        

    def display(self):
        if self.body_length > len(self.body):
            for i in range(self.body_length-len(self.body)):
                self.body.insert(0, pygame.Rect(self.body[0].x*2, self.body[0].y*2, self.w, self.h))

        for i in self.body:
            pygame.draw.rect(self.window, (0,0,0), i)

    def move_right(self):
        if not self.facing == 'left':
            head = self.body[len(self.body)-1]

            new_head = pygame.Rect(head.x+(self.w + self.distance), head.y, head.width, head.height)

            self.body.pop(0)
            self.body.append(new_head)
            
            self.facing = 'right'

    def move_left(self):
        if not self.facing == 'right':
            head = self.body[len(self.body)-1]

            new_head = pygame.Rect(head.x-(self.w + self.distance), head.y, head.width, head.height)

            self.body.pop(0)
            self.body.append(new_head)

            self.facing = 'left'

    def move_up(self):
        if not self.facing == 'down':
            head = self.body[len(self.body)-1]

            new_head = pygame.Rect(head.x, head.y-(self.h + self.distance), head.width, head.height)

            self.body.pop(0)
            self.body.append(new_head)

            self.facing = 'up'

    def move_down(self):
        if not self.facing == 'up':
            head = self.body[len(self.body)-1]

            new_head = pygame.Rect(head.x, head.y+(self.h + self.distance), head.width, head.height)

            self.body.pop(0)
            self.body.append(new_head)       

            self.facing = 'down'

    def collision_check(self):
        head = self.body[len(self.body)-1]

        for i in self.body:
            if head.colliderect(i) and i is not head:
                self.restart()

        if head.x >= self.width or head.x <= 0:
            self.restart()
        if head.y >= self.height or head.y <= 0:
            self.restart()
            

        if (head.x >= self.food.x and head.x <= self.food.x + self.food.width) and (head.y >= self.food.y and head.y <= self.food.y + self.food.height):
            self.body_length += 1
            
            self.rand_width = rand(40, self.width-40)
            self.rand_height = rand(40, self.height-40)
            self.random = [self.rand_width, self.rand_height]

            self.spawn_food()

    def restart(self):
        self.body = []
        self.body_length = self.default_body_length
        
        self.create()

    def spawn_food(self):
        self.food = pygame.Rect(self.random[0], self.random[1], 40, 40)
        pygame.draw.rect(self.window, (0,0,0), self.food)

main = MAIN()
main.create()

main.spawn_food()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        main.window.fill((255,255,255))

        main.spawn_food()

        if event.type == pygame.KEYDOWN:
            if event.unicode == 'd':
                main.move_right()
            if event.unicode == 'w':
                main.move_up()
            if event.unicode == 's':
                main.move_down()
            if event.unicode == 'a':
                main.move_left()


        main.collision_check()
        main.display()
        pygame.display.update()

        sleep(1/FPS)
