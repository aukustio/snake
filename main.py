import random as rd
import pygame as pg
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pg.init()

SCREEN_W = 400
SCREEN_H = 400

screen = pg.display.set_mode((SCREEN_W, SCREEN_H))


x = rd.randint(100, 300) 
y = rd.randint(100, 300)

x_ = 0 # change of direction
y_ = 0

snake_block = 10

foodx = round(rd.randrange(0, SCREEN_W - snake_block) / 10.0) * 10.0
foody = round(rd.randrange(0, SCREEN_H - snake_block) / 10.0) * 10.0

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue=(0,0,255)


time = pg.time.Clock()

running = True

font_style = pg.font.SysFont(None, 50)

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [SCREEN_W/2, SCREEN_H/2])

direction = "up" # default starting direction

while running:
    for event in pg.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
                if running == False:
                    quit
            if event.key == K_LEFT and direction != "right": # "and direction !="" prevents from going to opposite direction
                direction = "left"
                x_ = -10
                y_ = 0
            elif event.key == K_RIGHT and direction != "left":
                direction = "right"
                x_ = 10
                y_ = 0
            elif event.key == K_UP and direction != "down":
                direction = "up"
                x_ = 0
                y_ = -10                
            elif event.key == K_DOWN and direction != "up":
                direction = "down"
                x_ = 0
                y_ = 10

    if x > SCREEN_W or x < 0 or y > SCREEN_H or y < 0: # collision with borders
        running = False
    
    x += x_
    y += y_ 
    screen.fill(white)
    pg.draw.rect(screen, black, [x, y, 20, 20])
    pg.draw.rect(screen, blue, [foodx, foody, snake_block, snake_block])
    pg.draw.rect(screen, black, [x, y, snake_block, snake_block])

    if x == foodx and y == foody:

    pg.display.update()
    time.tick(20)
