import pygame

#CONTANTS
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
SPACE = 4
W = 5

class player:
    def __init__(self):
        
      #player varibles
      self.xpos = 400
      self.ypos = 415
      self.vx = 0
      self.vy = 0
      self.direction = RIGHT
      
    def draw(self,screen):
        pygame.draw.rect(screen, (255, 0, 255), (self.xpos, self.ypos, 30, 30))
       
    def move(self, keys, map):
        #LEFT MOVEMENT
        if keys[LEFT] == True:
            self.vx = -3
          
        #RIGHT MOVEMENT
        elif keys[RIGHT] == True:
            self.vx = 3
        #turn off x velocity
        else:
            self.vx = 0
        
        #copy/paste the above if-else statements here, change to up/down, talk about y, not x
            
        if keys[UP] == True:
            self.vy = -3
           
        #RIGHT MOVEMENT
        elif keys[DOWN] == True:
            self.vy = 3
        #turn off y velocity
        else:
            self.vy = 0
            
           
        #COLLISION
        #left collision
        if map[int((self.ypos- 10) / 50)][int((self.xpos - 10) / 50)] == 2:
            self.xpos+=3
           
        #right collison
        if map[int((self.ypos) / 50)][int((self.xpos +30 + 5) / 50)] == 2:
            self.xpos-=3
        
        #add collision for up/down here
            
        if map[int((self.ypos- 10) / 50)][int((self.ypos - 10) / 50)] == 2:
            self.ypos+=3
           
    
        if map[int((self.ypos) / 50)][int((self.ypos +30 + 5) / 50)] == 2:
            self.ypos-=3
           
        self.xpos+=self.vx #update player xpos
        #update player y pos
        self.ypos+=self.vy
