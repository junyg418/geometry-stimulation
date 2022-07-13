import sys
import pygame
import math
from pygame.locals import *


pygame.init()

FPS = 100
FramePerSec = pygame.time.Clock()

WHITE = (255,255,255)
BLACK = (0,0,0)
SKYBLUE = (184,233,248)
YELLO = (255,212,0)

size = (600,600)
GameDisplay = pygame.display.set_mode(size)
pygame.display.set_caption("정사영 시뮬레이션")
GameDisplay.fill(WHITE)

font = pygame.font.SysFont('malgungothicsemilight', 20)
text = font.render('그림자', True, BLACK)


seta = 0
def stimulationStart():
    global seta
    draw()
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    seta -= 0.1
                    GameDisplay.fill(WHITE)
                    draw()
                elif event.key == K_RIGHT:
                    seta += 0.1
                    GameDisplay.fill(WHITE)
                    draw()
        
        
        # FramePerSec(FPS)


def draw():
    global seta
    focus = (300, 300)
    circle_r = 150

    sin = math.sin(seta)
    cos = math.cos(seta)
    up_right_point = (300+int(cos*circle_r), 300+int(sin*circle_r))
    up_left_point = (300-int(cos*circle_r), 300-int(sin*circle_r))

    pygame.draw.line(GameDisplay, BLACK, up_left_point, up_right_point, 3)


    # 정사영 그림자 코드-----

    down_right_x = int(150*cos)+300
    down_right_point = (down_right_x, 500)
    
    down_left_x = 300-int(150*cos)
    down_left_point = (down_left_x, 500)

    pygame.draw.line(GameDisplay, BLACK, down_right_point, down_left_point, 3)

    pygame.draw.circle(GameDisplay, YELLO, (300,50), 30)
    GameDisplay.blit(text, (20, 485))
# def draw():
#     focus = (300, 500)
#     circle_r = 150

#     sin = math.sin(seta)
#     cos = math.cos(seta)
#     down_right_point = (300+int(cos*circle_r), 500+int(sin*circle_r))
#     down_left_point = (300-int(cos*circle_r), 500-int(sin*circle_r))

#     # def quadratic_formula(a, b, c):
#     #     '''
#     #     근의 공식
#     #     '''
#     #     return ((-b+math.sqrt(b**2-4*a*c))/2*a, (-b-math.sqrt(b**2-4*a*c))/2*a)

    
#     # try:
#     #     a = (cos*circle_r)**2/(sin*circle_r)**2+1
#     # except:
#     #     a = 0
#     # try:
#     #     b = 2*(circle_r**2)*(cos*circle_r)/(sin*circle_r)**2
#     # except:
#     #     b = 0
#     # try:
#     #     c = circle_r**4/(sin*circle_r)**2 - 2*circle_r**2 + (cos*circle_r)**2
#     # except:
#     #     c = 0
#     # top_left_x = int(quadratic_formula(a, b, c)[0])+300
#     # try:
#     #     top_left_y = int(circle_r**2-top_left_x*cos/sin)+500
#     # except:
#     #     top_left_y = 0
#     # top_left_point = (top_left_x, top_left_y)

#     pygame.draw.line(GameDisplay, BLACK, down_left_point, down_right_point)
#     # pygame.draw.line(GameDisplay, BLACK, down_left_point, top_left_point)


stimulationStart()