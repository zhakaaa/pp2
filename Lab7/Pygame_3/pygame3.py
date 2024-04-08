import pygame

pygame.init()
screen = pygame.display.set_mode((600,300)) 

screen.fill((255,255,255))

circle_x = 300
circle_y = 150

running = True
while running :

    screen.fill((255,255,255))

    pygame.draw.circle(screen,'Red', (circle_x,circle_y), 25)

    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get() :  
        if event.type == pygame.QUIT :
            running = False
            pygame.quit()
        if keys[pygame.K_LEFT] and circle_x > 40 :
            circle_x -= 20
        if keys[pygame.K_RIGHT] and circle_x < 560:
            circle_x += 20
        if keys[pygame.K_UP] and circle_y > 40:
           circle_y -= 20
        if keys[pygame.K_DOWN] and circle_y < 260:
            circle_y += 20

        pygame.display.update()