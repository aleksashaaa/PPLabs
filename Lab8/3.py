import pygame
import math

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))

colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)
colorGREEN = (0, 255, 0)
colorYELLOW = (255, 255, 0)

colors = [colorRED, colorBLUE, colorWHITE, colorGREEN, colorYELLOW]
current_color = 0

clock = pygame.time.Clock()

LMBpressed = False
THICKNESS = 5

currX = 0
currY = 0

prevX = 0
prevY = 0

drawCircle = False
drawRect = True
eraser = False

def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def calculate_square(x1, y1, x2, y2):
    w = abs(x1 - x2)
    h = abs(y1 - y2)
    lenght = min(w, h)
    rect = pygame.Rect(x1, y1, lenght, lenght)
    if (x1 < x2):
        if y1 > y2:
            rect.bottom = y1
            rect.left = x1
        else:
            rect.top = y1
            rect.left = x1
        return rect
    elif y2 < y1:
        rect.right = x1
        rect.bottom = y1
        return rect
    else:
        rect.right = x1
        rect.top = y1
        return rect

def calculate_circle(x1, y1, x2, y2):
    a = (x1 - x2)**2 + (y1 - y2)**2
    r = math.sqrt(a / 8)
    if a == 0:
        return x1, y1, 1
    if (x1 < x2):
        x = x1 + r
    else:
        x = x1 - r
    if (y1 < y2):
        y = y1 + r
    else:
        y = y1 - r
    return x, y, r

done = False

while not done:

    if eraser:
        currentX = prevX
        currentY = prevY

    for event in pygame.event.get():
        if LMBpressed and not eraser:
            screen.blit(base_layer, (0, 0))
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True
            if not eraser:
                prevX = event.pos[0]
                prevY = event.pos[1]
            
        if event.type == pygame.MOUSEMOTION:
            if LMBpressed:
                currX = event.pos[0]
                currY = event.pos[1]
                if drawRect:
                    pygame.draw.rect(screen, colors[0], calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                elif drawCircle:
                    x, y, r = calculate_circle(prevX, prevY, currX, currY)
                    pygame.draw.circle(screen, colors[0], (x, y), r, THICKNESS)

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False
            if not eraser:
                currX = event.pos[0]
                currY = event.pos[1]
                if drawRect:
                        pygame.draw.rect(screen, colors[0], calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                elif drawCircle:
                    x, y, r = calculate_circle(prevX, prevY, currX, currY)
                    pygame.draw.circle(screen, colors[0], (x, y), r, THICKNESS)
            base_layer.blit(screen, (0, 0))

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_EQUALS:
                print("increased thickness")
                THICKNESS += 1
            if event.key == pygame.K_MINUS:
                print("reduced thickness")
                THICKNESS -= 1
            if event.key == pygame.K_c:
                drawCircle = True
                drawRect = False
                eraser = False
            if event.key == pygame.K_r:
                drawCircle = False
                drawRect = True
                eraser = False

            if event.key == pygame.K_e:
                eraser = True
                drawCircle = False
                drawRect = False

            elif event.key == pygame.K_RIGHT:
                colors = colors[1:] + [colors[0]]
            elif event.key == pygame.K_LEFT:
                colors = [colors[-1]] + colors[:-1]

    if eraser:
        if LMBpressed:
            pygame.draw.line(screen, colorBLACK, (prevX, prevY), (currX, currY), THICKNESS)

        prevX = currX
        prevY = currY

    # pygame.draw.line(screen, colorRED, (prevX, prevY), (currX, currY), THICKNESS)

    pygame.display.flip()
    clock.tick(60)