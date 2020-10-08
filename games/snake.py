import pygame
import time
import random

pygame.init()
clock=pygame.time.Clock()
width=800
height=500
dspl=pygame.display.set_mode((width,height))
pygame.display.set_caption('Snake Game')
pygame.display.update()

snake_block=10
snake_speed=25
snake_pos=[]
def snake(snake_block,snake_pos):
    for i in snake_pos:
        snakeclr=(30,255,random.randint(150,200))
        pygame.draw.rect(dspl,snakeclr,[i[0],i[1],snake_block,snake_block])

def game():
    ingame = True
    game_end=False
    x=width/2
    y=height/2
    x_change = 0
    y_change = 0
    snake_list=[]
    snake_length=1
    foodx=round(random.randrange(0,width-snake_block)/10.0)*10.0
    foody=round(random.randrange(0,height-snake_block)/10.0)*10.0
    while ingame:
        while game_end==True:
            dspl.fill((10,200,30))
            font=pygame.font.SysFont("comicsansns",35)
            msg=font.render("You lost.. If you wan to play again Press P. ",True,(20,100,30))
            dspl.blit(msg,[width/5,height/2])
            score=snake_length-1
            score_font=pygame.font.SysFont("comicsansns",35)
            value=score_font.render("Your Score: "+str(score),True,(35,60,200))
            dspl.blit(value,[width/5,height/5])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key== pygame.K_p:
                        game()
                if event.type == pygame.QUIT:
                    ingame = False
                    game_end=False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ingame = False
            if event.type==pygame.KEYDOWN:
                if event.key== pygame.K_LEFT:
                    x_change=-snake_block
                    y_change=0
                if event.key== pygame.K_RIGHT:
                    x_change=snake_block
                    y_change=0
                if event.key== pygame.K_UP:
                    x_change=0
                    y_change=-snake_block
                if event.key== pygame.K_DOWN:
                    x_change=0
                    y_change=snake_block
        if(x<0 or x>=width) or(y<0 or y>+height):
           game_end=True
        x += x_change
        y += y_change
        foodcolor=(22,100,120)
        dspl.fill((0,0,0))
        pygame.draw.rect(dspl,foodcolor,[foodx,foody,snake_block,snake_block])
        snake_head=[]
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list)>snake_length:
            del snake_list[0]
        for i in snake_list[:-1]:
            if i==snake_head:
                game_end=True
        snake(snake_block,snake_list)

        pygame.display.update()
        if (x==foodx and y==foody):
            foodx=round(random.randrange(0,width-snake_block)/10.0)*10.0
            foody=round(random.randrange(0,height-snake_block)/10.0)*10.0
            snake_length+=1
        clock.tick(snake_speed)
    pygame.quit()
    quit
game()
