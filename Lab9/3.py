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

shapes = {"drawCircle": False, "drawRect": True, "drawSquare": False, "eraser": False, 
          "drawTriangle": False, "drawRightTriangle": False, "drawRhombus": False}

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

def calculate_triangle(x1, y1, x2, y2): #Draw equilateral triangle 
    cor = [(x1, y1)]
    height = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    side_length = height * math.sqrt(4/3)
    if (y1 < y2):
        cor.append((x1 + side_length / 2, y1 + height))
        cor.append((x1 - side_length / 2, y1 + height))
    else:
        cor.append((x1 + side_length / 2, y1 - height))
        cor.append((x1 - side_length / 2, y1 - height))
    return cor

def right_triangle(x1, y1, x2, y2):
    cor = [(x1, y1)]
    rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))
    if (x1 < x2 and y1 < y2) or (x1 > x2 and y1 > y2):
        cor.append((rect.left, rect.bottom))
        cor.append((rect.right, rect.top))
    else:
        cor.append((rect.left, rect.top))
        cor.append((rect.right, rect.bottom))
    return cor

def calculate_rhombus(x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        return [(x1 + dx, y1), (x1, y1 + dy), (x1 - dx, y1), (x1, y1 - dy)]

def all_false(s):
    for i, j in s.items():
        s[i] = False

done = False

while not done:

    if shapes["eraser"]:
        currentX = prevX
        currentY = prevY

    for event in pygame.event.get():
        if LMBpressed and not shapes["eraser"]:
            screen.blit(base_layer, (0, 0))
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True
            if not shapes["eraser"]:
                prevX = event.pos[0]
                prevY = event.pos[1]
            
        if event.type == pygame.MOUSEMOTION:
            if LMBpressed:
                currX = event.pos[0]
                currY = event.pos[1]
                if shapes["drawRect"]:
                    pygame.draw.rect(screen, colors[0], calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                elif shapes["drawCircle"]:
                    x, y, r = calculate_circle(prevX, prevY, currX, currY)
                    pygame.draw.circle(screen, colors[0], (x, y), r, THICKNESS)
                elif shapes["drawSquare"]:
                    pygame.draw.rect(screen, colors[0], calculate_square(prevX, prevY, currX, currY), THICKNESS)
                elif shapes["drawRightTriangle"]:
                    cor = right_triangle(prevX, prevY, currX, currY)
                    pygame.draw.polygon(screen, colors[0], (cor[0], cor[1], cor[2]), THICKNESS)

                elif shapes["drawTriangle"]:
                    cor = calculate_triangle(prevX, prevY, currX, currY)
                    pygame.draw.polygon(screen, colors[0], (cor[0], cor[1], cor[2]), THICKNESS)

                elif shapes["drawRhombus"]:
                    pygame.draw.polygon(screen, colors[0], calculate_rhombus(prevX, prevY, currX, currY), THICKNESS)

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False
            if not shapes["eraser"]:
                currX = event.pos[0]
                currY = event.pos[1]
                if shapes["drawRect"]:
                    pygame.draw.rect(screen, colors[0], calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                elif shapes["drawCircle"]:
                    x, y, r = calculate_circle(prevX, prevY, currX, currY)
                    pygame.draw.circle(screen, colors[0], (x, y), r, THICKNESS)
                elif shapes["drawSquare"]:
                    pygame.draw.rect(screen, colors[0], calculate_square(prevX, prevY, currX, currY), THICKNESS)
                elif shapes["drawRightTriangle"]:
                    cor = right_triangle(prevX, prevY, currX, currY)
                    pygame.draw.polygon(screen, colors[0], (cor[0], cor[1], cor[2]), THICKNESS)

                elif shapes["drawTriangle"]:
                    cor = calculate_triangle(prevX, prevY, currX, currY)
                    pygame.draw.polygon(screen, colors[0], (cor[0], cor[1], cor[2]), THICKNESS)
                elif shapes["drawRhombus"]:
                    pygame.draw.polygon(screen, colors[0], calculate_rhombus(prevX, prevY, currX, currY), THICKNESS)
            base_layer.blit(screen, (0, 0))

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_EQUALS:
                print("increased thickness")
                THICKNESS += 1
            if event.key == pygame.K_MINUS:
                print("reduced thickness")
                THICKNESS -= 1
            if event.key == pygame.K_c:
                all_false(shapes)
                shapes["drawCircle"] = True
                print(shapes)
            if event.key == pygame.K_r:
                all_false(shapes)
                shapes["drawRect"] = True
            if event.key == pygame.K_s:
                all_false(shapes)
                shapes["drawSquare"] = True
            if event.key == pygame.K_q:
                all_false(shapes)
                shapes["drawTriangle"] = True
            if event.key == pygame.K_t:
                all_false(shapes)
                shapes["drawRightTriangle"] = True
            if event.key == pygame.K_h:
                all_false(shapes)
                shapes["drawRhombus"] = True    

            if event.key == pygame.K_e:
                all_false(shapes)
                shapes["eraser"] = True

            elif event.key == pygame.K_RIGHT:
                colors = colors[1:] + [colors[0]]
            elif event.key == pygame.K_LEFT:
                colors = [colors[-1]] + colors[:-1]

    if shapes["eraser"]:
        if LMBpressed:
            pygame.draw.line(screen, colorBLACK, (prevX, prevY), (currX, currY), THICKNESS)

        prevX = currX
        prevY = currY

    # pygame.draw.line(screen, colorRED, (prevX, prevY), (currX, currY), THICKNESS)

    pygame.display.flip()
    clock.tick(60)