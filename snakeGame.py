import time, os, random
import pygame, sys
from pygame.locals import *

meJPG="me2.jpg"
png ="me3.png"

snake_speed = 15

# Window size
window_x = 720
window_y = 480

################################# Colors
eggplantColor = (88,24,69)
burgundyColor = (144, 12, 63)
autumnColor = (199, 0, 57)
pumpkinColor = (255, 87, 51)
squashColor = (255, 195, 15)
############################################### Colors


####################################################################################################################################
#initialising pygame
pygame.init()

#defining font attributes
myFont = pygame.font.SysFont("Segoe UI", 90)
welcome = "Greetings Player!"

#defining size of game window
window = pygame.display.set_mode((window_x, window_y))
window.fill(squashColor)
pygame.display.set_caption("Danger Noodle Game!")
# pygame.draw.rect(windowsSize, burgundyColor, (200, 260, 200, 200))
# pygame.draw.rect(windowsSize, autumnColor, (150, 260, 200, 200))

# clock variable holds value of time
clock = pygame.time.Clock()

# defining snake default position
snake_position = [100, 50]

# defining first 4 blocks of snake
# body
snake_body = [  [100, 50],
                [90, 50],
                [80, 50],
                [70, 50]
            ]
#background image
backgroundfile = pygame.image.load("me3.png").convert()
window.blit(backgroundfile, (0, 0))
##################
x1 = 10
y1 = 10

x1_change = 0  
y1_change = 0

snake_speed = 15
#draws rectangle that represents burgundy snake
pygame.draw.rect(window, burgundyColor, [x1, y1, 40, 40])
# setting default snake direction
# towards right
direction = 'RIGHT'
change_to = direction
snake_block = 10

# fruit position
fruitX = round(random.randrange(0, window_x - snake_block) / 10.0) * 10.0
fruitY = round(random.randrange(0, window_y - snake_block) / 10.0) * 10.0
fruit_spawn = True
fruit_amount = round(random.randrange(1, 8))

# initial score
score = 0
#running the game is true
running = True

def message(msg,color):
    mesg = myFont.render(msg, True, color)
    window.blit(mesg, [window_x/2, window_y/2])

# displaying Score function
def show_score(choice, eggplantColor, myfont, size):

    # creating font object score_font
    score_font = pygame.font.SysFont(myfont, size)
    
    # create the display surface object
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, eggplantColor)
    
    # create a rectangular object for the
    # text surface object
    score_rect = score_surface.get_rect()
    
    # displaying text
    window.blit(score_surface, score_rect)

#########################################################################################

while running:
    pygame.display.update()
    #################################################################
    for event in pygame.event.get():
        # the escape sequence for the game window
        ###############################################
        if event.type == KEYDOWN:
            if event.key == K_UP:
                y1_change =- 10
                x1_change = 0
            if event.key == K_DOWN:
                y1_change =+ 10
                x1_change = 0
            if event.key == K_LEFT:
                x1_change =- 10
                y1_change = 0
            if event.key == K_RIGHT:
                x1_change =+ 10
                y1_change = 0
            if event.key == K_ESCAPE:
                running = False
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        ################################################ key controls end here
        x1 += x1_change
        y1 += y1_change
        window.blit(backgroundfile, (0, 0))
        pygame.draw.rect(window, burgundyColor, [x1, y1, 40, 40])

        pygame.draw.rect(window, pumpkinColor, [fruitX, fruitY, 20, 20])
        snake_Head = []
        pygame.display.update()
        clock.tick(30)
    ################################################################## checks for events

############################################################################################

message("You lost", squashColor)
pygame.display.update()
time.sleep(2)

#####################################################################################################################################