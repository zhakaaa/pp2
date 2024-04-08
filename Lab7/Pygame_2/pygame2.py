import pygame
import random

pygame.init()

screen = pygame.display.set_mode((230,75))
screen.fill((190,198,195))

pygame.display.set_caption("Music Player")

musiclist = ["sounds/music1.mp3", "sounds/music2.mp3", "sounds/music3.mp3" , "sounds/music4.mp3"]
current_music = random.randint(0,3)

def play_song() :
    pygame.mixer.music.load(musiclist[current_music])
    pygame.mixer.music.play()

def next_song():
    global current_music
    if 0 <=current_music < 3 :
        current_music += 1
    play_song()

def prev_song():
    global current_music
    if 0 < current_music <= 3 :
        current_music -= 1
    play_song()

play_song()

play_music = pygame.image.load('images/play.png').convert_alpha()
play_music_rect = play_music.get_rect(topleft=(75,20))

stop_music = pygame.image.load('images/stop.png').convert_alpha()
stop_music_rect = stop_music.get_rect(topleft=(125,20))

next_music = pygame.image.load('images/next.png').convert_alpha()
next_music_rect = next_music.get_rect(topleft=(175,20))

previous_music = pygame.image.load('images/previous.png').convert_alpha()
previous_music_rect = previous_music.get_rect(topleft=(25,20))

running = True
while running :

    screen.blit(stop_music, stop_music_rect)
    screen.blit(play_music, play_music_rect)
    screen.blit(next_music, next_music_rect)
    screen.blit(previous_music, previous_music_rect)

    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if play_music_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0] :
            pygame.mixer.music.unpause()
        elif stop_music_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0] :
             pygame.mixer.music.pause()
        elif next_music_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0] :
            next_song()
        elif previous_music_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0] :
            prev_song()

    pygame.display.update()