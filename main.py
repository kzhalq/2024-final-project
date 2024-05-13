import pygame
from player import player
from fireball import fireball
pygame.init()
pygame.display.set_caption("top down grid game") # sets window title
screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock() #set up clock
gameover = False #varibles to run our game loop

#instantiate player and fireball
p1 = player()
ball = fireball()

#CONSTANTS
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
SPACE = 4
W = 5
keys = [False, False, False, False, False] #this list holds whether each key has been pressed

#mouse input
xpos = 0
ypos = 0
mousePos = (xpos, ypos)
mouseDown = False

#game state variable
state = 1 #1 is menu, 2 is playing, 3 is credits
button1 = False
#add more buttons here!
quitGame = False

map = [[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [3,3,3,1,1,1,3,3,3,3,1,1,1,1,1,1,1,1,1,2],
       [3,3,3,3,3,3,3,3,3,3,3,3,1,1,1,1,1,1,1,2],
       [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,1,1,2],
       [2,1,3,3,3,3,1,1,1,1,3,3,3,3,3,3,3,3,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,3,3,3,3,3,3,3,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]
       

brick = pygame.image.load('brick.png')
grass = pygame.image.load('grass.png')
dirt = pygame.image.load('dirt.png')
sand = pygame.image.load('sand.png')

while not gameover:#GAME LOOP====================================================================================================
    clock.tick(60) #FPS
    #input section----------------------------------------------------------------
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        #keeps track of mouse position
        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos
        #keeps track of mouse button
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouseDown = False
        if event.type == pygame.QUIT:
            gameover = True
            
        if event.type == pygame.KEYDOWN: #keybord input
            if event.key == pygame.K_LEFT:
                keys[LEFT] = True
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = True
            elif event.key == pygame.K_q:
                quitGame = True
            elif event.key == pygame.K_UP:
                keys[UP] = True
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = True
            elif event.key == pygame.K_SPACE:
                keys[SPACE] = True
          
                
            #add up/down here, also q
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT] = False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = False
            elif event.key == pygame.K_q:
                quitGame = False
            elif event.key == pygame.K_UP:
                keys[UP] = False
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = False
            elif event.key == pygame.K_SPACE:
                keys[SPACE] = False
            #add up/down here
                
   
    #physics section------------------------------------------------------------------------
    print(mousePos)#uncomment for testing
    if state == 1 and mousePos[0]>100 and mousePos[0]<300 and mousePos[1]>400 and mousePos[1]<550:
        button1 = True
        
    else:
        button1 = False
            
    if state == 1 and button1 == True and mouseDown == True:
        state = 2
    #state 2: playing state!---------------------------
    if state == 2 and quitGame == True: #pressing quit takes you back to menu
        state = 1
        
    p1.move(keys, map)
    ball.move()
    
      #check space for shooting
    if keys[SPACE] == True:
        ball.shoot(p1.xpos, p1.ypos, p1.direction)
        
                                                                
#render section-------------------------------------------------------------------------------------
            
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
    
    
    
    #menu state-------------------------------
    if state == 1:
        screen.fill((230,100,100))# Clear the screen pink
        if button1 == False:
            pygame.draw.rect(screen, (100, 230, 100), (100, 400, 200, 150))
        else:
            pygame.draw.rect(screen, (200, 250, 200), (100, 400, 200, 150))
        pygame.draw.rect(screen, (100, 230, 100), (400, 400, 200, 150))
        pygame.draw.rect(screen, (100, 230, 100), (700, 400, 200, 150))
        
     #game state-------------------------------
    if state == 2:
        screen.fill((80,150,100))# Clear the screen green
        #more game stuff would be drawn here
        
        #draw map
        for i in range(16):
            for j in range(20):
                if map[i][j] == 1:
                    screen.blit(grass, (j * 50, i * 50), (0, 0, 50, 50))
                if map[i][j] == 2:
                    screen.blit(brick, (j * 50, i * 50), (0, 0, 50, 50))
                if map[i][j] == 3:
                    screen.blit(dirt, (j * 50, i * 50), (0, 0, 50, 50))
                if map[i][j] == 4:
                    screen.blit(sand, (j * 50, i * 50), (0, 0, 50, 50))
                
        p1.draw(screen)
        
    #draw fireball
    if ball.isAlive == True:
        ball.draw(screen)
                
    pygame.display.flip()#this actually puts the pixel on the screen
    
# end of game loop=====================================================================================================================
pygame.quit()
