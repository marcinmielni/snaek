import pygame
import random
from Obj.objects import Snake, Food


BACKGROUND_COLOR = (0, 0, 0)        #color theme
WHITE = (255, 255, 255)
BLUE = (0, 0, 200)


def msg(surface, str, x, y, fontSize = 64):
    font = pygame.font.Font(None, fontSize)
    text = font.render(str, True, WHITE, BACKGROUND_COLOR)
    textRect = text.get_rect()
    textRect.center = (x, y)
    surface.blit(text, textRect)

def main(size = 50, resolution = 1000):
    pygame.init()

    cubeSize = resolution // size

    dis = pygame.display.set_mode((resolution, resolution))         # window opening
    pygame.display.set_caption('S N A E K')
    pygame.display.update()

    game_over = True
    game_close = False

    clock = pygame.time.Clock()
    clockTick = 5
    
    while not game_close:                                               #game loop
        msg(dis, "Press Enter to play", resolution//2, resolution//2, 64)
        msg(dis, "Press Esc to quit", resolution//2, 3 * resolution//4, 32)
        pygame.display.update()
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    game_over = True
                    game_close = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_over = False
                        snk = Snake(resolution // 2, resolution // 2, cubeSize)             #initializing snake
                        fd = Food(cubeSize, resolution)                                     #initializing food
                        direction = (0, 0)
        while not game_over:                                            #playing loop
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    game_over = True
                    game_close = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        direction = (-cubeSize, 0)
                    elif event.key == pygame.K_RIGHT:
                        direction = (cubeSize, 0)
                    elif event.key == pygame.K_UP:
                        direction = (0, -cubeSize)
                    elif event.key == pygame.K_DOWN:
                        direction = (0, cubeSize)

            snk.Move(direction)
            #print(snk.segments)

            if snk.isCollision():
                game_over = True
            
            if snk.x >= resolution or snk.x < 0 or snk.y >= resolution or snk.y < 0:
                game_over = True

            if snk.x == fd.x and snk.y == fd.y:
                clockTick += 1
                snk.Eat()
                fd.GetNew()
                clock.tick(clockTick)

                

            dis.fill(BACKGROUND_COLOR)
            snk.Draw(dis)
            fd.Draw(dis)
    
            clock.tick(clockTick)
            pygame.display.update()

        
        clock.tick(100)
    pygame.quit()
    quit()

main()