import pygame
import random

#CONTANTS
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

class enemy:
    def __init__(self):
        
      #player varibles
      self.xpos = 400
      self.ypos = 200
      self.direction = RIGHT
        
        
    def draw(self,screen):
        pygame.draw.rect(screen, (51, 51, 255), (self.xpos, self.ypos, 30, 30))
        
    def move(map, ticker, px, py):
        #randomly wander:
        if ticker % 40 == 0: #mess with this number to make him change direction more or less often!
            num = random.randrange(0, 4)
            if num == 0:
                self.direction = RIGHT
            elif num = 1:
                self.direction = LEFT
            elif num = 2:
                self.
        
