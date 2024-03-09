import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
done = False
x = 250
y = 250

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y - 20 >= 25: y -= 20
    if pressed[pygame.K_DOWN] and y + 20 <= 475: y += 20
    if pressed[pygame.K_LEFT] and x - 20 >= 25: x -= 20
    if pressed[pygame.K_RIGHT] and x + 20 <= 475: x += 20
        
    screen.fill((255, 255, 255))
    color = (255, 0, 0)
    pygame.draw.circle(screen, color, [x, y], 25, 0)
        
    pygame.display.flip()
    clock.tick(60)