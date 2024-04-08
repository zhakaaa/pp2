import pygame
import datetime

pygame.init()

screen = pygame.display.set_mode((1200, 1000))


seconds = pygame.image.load("images/leftarm.png").convert_alpha()
minutes = pygame.image.load("images/rightarm.png").convert_alpha()
background = pygame.image.load("images/mainclock.png").convert_alpha()

background = pygame.transform.scale(background, (1200, 1000)) # изменение размера фона на новый размер, оно как бы сжалось. мы меняем размеры самого объекта 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    time_now = datetime.datetime.now()
    minute_time = time_now.minute 
    second_time = time_now.second

   
    minute_angle = -minute_time * 6 
    second_angle = -second_time * 6 

    
    rotated_minutes = pygame.transform.rotate(minutes, minute_angle)
    rotated_seconds = pygame.transform.rotate(seconds, second_angle)

    
    screen.blit(background, (0, 0))
    screen.blit(rotated_minutes, (600 - rotated_minutes.get_width()//2, 500 - rotated_minutes.get_height()//2))  
    screen.blit(rotated_seconds, (600 - rotated_seconds.get_width()//2, 500 - rotated_seconds.get_height()//2)) #right arm parameters: (63, 1050)

    pygame.display.flip()