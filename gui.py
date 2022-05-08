import pygame
from omok import omok
import numpy as np

pygame.init()
pygame.display.set_caption("Pymok")
screen = pygame.display.set_mode((800, 800))
fps = pygame.time.Clock()
run = True
count = 2

board_img = pygame.image.load("data/img/board.png")
white_img = pygame.image.load("data/img/white.png")
black_img = pygame.image.load("data/img/black.png")
screen.blit(board_img, (0, 0))
om = omok()
while run:
    fps.tick(10)

    stone = 1 if count % 2 else 2
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = list(pygame.mouse.get_pos())[0]
            y = list(pygame.mouse.get_pos())[1]
            
            posList = []
            for i in range(1, 10):
                for v in range(1, 10):
                    posList.append([v, i])
            
            for pos in posList:
                if pos[0]*80 - 15 <= x and pos[0]*80 + 15 >= x:
                    if pos[1]*80 - 15 <= y and pos[1]*80 + 15 >= y:
                        _event = om.put(pos[0]-1, pos[1]-1, stone)
                        print(om.board)
                        if not _event:
                            count += 1

                            if stone == 1:
                                screen.blit(white_img, (pos[0]*80 - 30, pos[1]*80 - 30))
                            else:
                                screen.blit(black_img, (pos[0]*80 - 30, pos[1]*80 - 30))
                        elif _event == "end":
                            run = False
                            
                            
                            






            

    pygame.display.update()
    
