import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
stop = False

songs = ["1.mp3", "2.mp3", "3.mp3"]
current_song_index = 0

pygame.mixer.music.load(songs[current_song_index])
pygame.mixer.music.play()

clock = pygame.time.Clock()

font = pygame.font.SysFont("comicsansms", 20)
text1 = font.render("press SPACE to - Play/Stop", True, (0, 0, 200))
text2 = font.render("press -> or <- to - Change song", True, (0, 0, 200))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                stop = not stop
                if stop:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:
                songs = songs[1:] + [songs[0]]
                pygame.mixer.music.load(songs[0])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                songs = [songs[-1]] + songs[:-1]
                pygame.mixer.music.load(songs[0])
                pygame.mixer.music.play()

    screen.fill((255, 255, 255))
    screen.blit(text1, (200 - text1.get_width() // 2, 50))
    screen.blit(text2, (200 - text2.get_width() // 2, 90))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()