import pygame
import random
import time

pygame.init()

# Define colors
GREEN = (0,255,0)    # snake color
BLACK = (0,0,0)      # background color
ORANGE = (255,165,0) # fruit color
PURPLE = (255,0,255) # second fruit color
RED = (255,0,0)      # game over color

# Screen size
WIDTH = 600
HEIGHT = 400

SCREEN = pygame.display.set_mode((WIDTH,HEIGHT)) # screen size
pygame.display.set_caption("Snake Game")         # title of game

clock = pygame.time.Clock()

snake_size = 10   # snake size

message_font = pygame.font.SysFont('ubuntu', 30)  # game over font
score_font = pygame.font.SysFont('ubuntu', 25)   # score font
level_font = pygame.font.SysFont('ubuntu', 25)


def print_score(score):
    text = score_font.render("Score: " + str(score) , True , ORANGE)
    SCREEN.blit(text, (0,0))

def print_level(level_snake):
    level = level_font.render("Level: " + str(level_snake) , True , ORANGE)
    SCREEN.blit(level,(200,0))

def draw_snake(snake_size, snake_pixels) : # snake_pixels is list with coordinates of every square
    for pixels in snake_pixels :          # x         # y
        pygame.draw.rect(SCREEN, GREEN, (pixels[0], pixels[1], snake_size , snake_size))

def run_game():

    # Initialize basic variables
    game_over = False  # when game is ended
    game_close = False # when round is losed

    x = WIDTH / 2   # start position
    y = HEIGHT / 2

    x_speed = 0  # change of coordinates while moving
    y_speed = 0

    snake_pixels = [] 
    snake_length = 1  # one block of snake

    food_x = round(random.randrange(0, WIDTH - snake_size) / 10) * 10
    food_y = round(random.randrange(0, HEIGHT - snake_size) / 10) * 10

    food2_x = round(random.randrange(0, WIDTH - snake_size) / 10) * 10
    food2_y = round(random.randrange(0, HEIGHT - snake_size) / 10) * 10

    count = 0 # количество съеденных фруктов
    level_snake = 0  # уровень

    snake_speed = 10 # скорость змеи происходит засчет изменение координат змеи

    timer, timer2 = 50, 50   # timers

    while not game_over :
        while game_close :  # if round is losed
            SCREEN.fill(BLACK)
            game_over_message = message_font.render("Game Over!" , True, RED)
            SCREEN.blit(game_over_message , (WIDTH / 3, HEIGHT / 3))
            print_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT: # игра проиграна и экран закрыт
                    game_over = True    
                    game_close = False  
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1: # игра проиграна и экран закрыт
                        game_over = True   
                        game_close = False
                    if event.key == pygame.K_2: # restart
                        run_game()
                # if event.type == pygame.QUIT:
                #     game_over = True
                #     game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:   # when key is pressed
                # change coordinates while moving
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size  
                    y_speed = 0
                if event.key == pygame.K_RIGHT :
                    x_speed = snake_size
                    y_speed = 0
                if event.key == pygame.K_UP :
                    x_speed = 0
                    y_speed = -snake_size
                if event.key == pygame.K_DOWN :
                    x_speed = 0
                    y_speed = snake_size
                timer -= 1   # время идет при каждом клике для оранжевого фрукта 
                timer2 -= 1  # время идет при каждом клике для фиолетового фрукта

        # if we hit boundary, then round is losed
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0 :
            game_close = True
        
        # change the position of snake
        x += x_speed 
        y += y_speed

        SCREEN.fill(BLACK)  # background of screen
        
        pygame.draw.rect(SCREEN, ORANGE, (food_x, food_y, snake_size, snake_size)) # draw fruit
        pygame.draw.rect(SCREEN, PURPLE, (food2_x, food2_y, snake_size, snake_size)) 

        # мы должны постоянно обновлять змейку, каждый раз когда мы нажимаем на клавишу
        # то есть, мы добавляем новые координаты в наш список
        snake_pixels.append((x,y)) 

        # но если координат больше чем длина змейки, то мы удаляем старые координаты
        # другими словами, мы добавляем новые координаты к хвосту и удаляем старые коориднаты головы
        if len(snake_pixels) > snake_length :   # закомментируй 
            del snake_pixels[0]

        # когда змея коснется самого себя, то игра проиграна
        for pixel in snake_pixels[:-1] :  # проверяем все координаты до головы змеи
            if pixel == (x,y) :
                game_close = True  # раунд окончен, но не игра

        draw_snake(snake_size, snake_pixels)
        print_score(snake_length - 1)
        print_level(level_snake)

        if count >= 3 :  # съедая по 3 фрукта уровень растет на одну ступень
            level_snake += 1
            # print_level(level_snake)
            snake_speed += 2  # также растет скорость змеи с ростом уровня
            count = 0    # устанавливаем обратно исходное значение

        pygame.display.update()

        if x == food_x and y == food_y :  # если змея кушает фрукт
            food_x = round(random.randrange(0,WIDTH - snake_size) / 10) * 10    # следующие координаты нового фрукта
            food_y = round(random.randrange(0,HEIGHT - snake_size) / 10) * 10
            snake_length += 1  # длина змеи растет на один блок
            count += 1 
            timer = 50   # устанавливаем исходное значение таймера

        if timer <= 0:  # если время истекло, предыдущий фрукт исчезает и появляется новый фрукт
            food_x = round(random.randrange(0,WIDTH - snake_size) / 10) * 10    # следующие координаты нового фрукта
            food_y = round(random.randrange(0,HEIGHT - snake_size) / 10) * 10
            timer =  50  # устанавливаем исходное значение таймера

        if x == food2_x and y == food2_y :  # если змея кушает фрукт
            # pygame.time.wait(2000) 
            food2_x = round(random.randrange(0,WIDTH - snake_size) / 10) * 10    # следующие координаты нового фрукта
            food2_y = round(random.randrange(0,HEIGHT - snake_size) / 10) * 10
            snake_length += 2  # длина змеи растет на один блок
            count += 2 
            timer2 = 50 # устанавливаем исходное значение таймера

        if timer2 <= 0 :  # если время истекло, предыдущий фрукт исчезает и появляется новый фрукт
            # pygame.time.wait(2000) 
            food2_x = round(random.randrange(0,WIDTH - snake_size) / 10) * 10    # следующие координаты нового фрукта
            food2_y = round(random.randrange(0,HEIGHT - snake_size) / 10) * 10
            timer2 = 50  # устанавливаем исходное значение таймера
        
        clock.tick(snake_speed)  # frequency of cycle
 
    pygame.quit()

run_game()


