import pygame
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((700, 525))
done = False

bg_image = pygame.image.load("mickeyclock.jpg")
minute = pygame.image.load("min.png")
second = pygame.image.load("sec.png")

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    time = datetime.now()
    min_angle = (time.minute / 60) * 360
    sec_angle = (time.second / 60) * 360
    
    screen.blit(bg_image, (0, 0))

    w, h = second.get_size()
    box = [pygame.math.Vector2(p) for p in [(0, h), (w, h), (w, 0), (0, 0)]]
    box_rotate = [p.rotate(-sec_angle) for p in box]
    min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
    max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])
    sec_origin = (370 + min_box[0], 262 - max_box[1])
    sec_rotated = pygame.transform.rotate(second, -sec_angle)
    screen.blit(sec_rotated, sec_origin)

    w, h = minute.get_size()
    box = [pygame.math.Vector2(p) for p in [(0, h), (w, h), (w, 0), (0, 0)]]
    box_rotate = [p.rotate(-min_angle) for p in box]
    min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
    max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])
    min_origin = (350 + min_box[0], 262 - max_box[1])
    min_rotated = pygame.transform.rotate(minute, -min_angle)
    screen.blit(min_rotated, min_origin)
    
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()