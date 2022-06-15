import pygame
from math import sqrt
from time import sleep
from random import choice

pygame.init()

FPS = 60

class MAIN:
    def __init__(self):
        self.width = 600
        self.height = 600
        self.window = pygame.display.set_mode((self.width, self.height))
        self.w = 20
        self.h = 20
        self.default_body_length = 2
        self.body_length = self.default_body_length
        self.body = []
        self.random = [[i*20,i*20] for i in range(30)]
        self.random_picked = choice(self.random)
        self.facing = 'up'
        self.score = 0
        self.font = pygame.font.Font("freesansbold.ttf",32)
        self.text = self.font.render(f'Score: {self.score}',False,(0,0,0))

    def create(self):                
        for i in range(self.body_length):
            self.body.insert(0, pygame.Rect(20, 20+(sqrt(20*20)),self.w, self.h))
        

    def display(self):
        if self.body_length > len(self.body):
            for i in range(self.body_length-len(self.body)):
                self.body.insert(0, pygame.Rect(self.width*2, self.height*2, self.w, self.h))

        for i in self.body:
            pygame.draw.rect(self.window, (79,121,66), i)

        self.window.blit(self.text, (self.width/2-60, 0))

    def move_right(self):
        if not self.facing == 'left':
            head = self.body[len(self.body)-1]

            new_head = pygame.Rect(head.x+(sqrt(head.width*head.height)), head.y, head.width, head.height)

            self.body.pop(0)
            self.body.append(new_head)
            
            self.facing = 'right'

    def move_left(self):
        if not self.facing == 'right':
            head = self.body[len(self.body)-1]

            new_head = pygame.Rect(head.x-(sqrt(head.width*head.height)), head.y, head.width, head.height)

            self.body.pop(0)
            self.body.append(new_head)

            self.facing = 'left'

    def move_up(self):
        if not self.facing == 'down':
            head = self.body[len(self.body)-1]

            new_head = pygame.Rect(head.x, head.y-sqrt(head.width*head.height), head.width, head.height)

            self.body.pop(0)
            self.body.append(new_head)

            self.facing = 'up'

    def move_down(self):
        if not self.facing == 'up':
            head = self.body[len(self.body)-1]

            new_head = pygame.Rect(head.x, head.y+(sqrt(head.width*head.height)), head.width, head.height)

            self.body.pop(0)
            self.body.append(new_head)       

            self.facing = 'down'

    def collision_check(self):
        head = self.body[len(self.body)-1]

        for i in self.body:
            if head.colliderect(i) and i is not head:
                self.restart()

        if head.x > self.width or head.x < 0:
            self.restart()
        if head.y > self.height or head.y < 0:
            self.restart()
            

        if head.colliderect(i) and i is not head:
            self.body_length += 1
            self.score += 1

            self.text = self.font.render(f'Score: {self.score}',False,(0,0,0))

            self.random_picked = choice(self.random)
            self.spawn_food()

    def restart(self):
        self.body = []
        self.score = 0

        self.text = self.font.render(f'Score: {self.score}',False,(0,0,0))
        
        self.body_length = self.default_body_length
        
        self.create()

    def spawn_food(self):
        
   
        self.food = pygame.Rect(self.random_picked[0],self.random_picked[1],20,20)

        pygame.draw.rect(self.window, (255,0,0), self.food)

main = MAIN()
main.create()

while True:
    ()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        

        main.window.fill((255,255,255))

        main.spawn_food()

        if event.type == pygame.KEYDOWN:
            if event.unicode == 'd' or event.key == pygame.K_RIGHT:
                main.move_right()
            if event.unicode == 'w' or event.key == pygame.K_UP:
                main.move_up()
            if event.unicode == 's' or event.key == pygame.K_DOWN:
                main.move_down()
            if event.unicode == 'a' or event.key == pygame.K_LEFT:
                main.move_left()


        main.collision_check()
        main.display()
        pygame.display.update()

        sleep(1/FPS)
