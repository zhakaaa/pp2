import pygame
import random
import time

pygame.init()

# Define colors
green = (0,255,0)    # snake color
black = (0,0,0)      # background color
orange = (255,165,0) # fruit color
red = (255,0,0)      # game over color

# Screen size
width = 600
height = 400

screen = pygame.display.set_mode((width,height)) # screen size
pygame.display.set_caption("Snake Game")         # title of game

clock = pygame.time.Clock()

snake_size = 10   # snake size
 # snake speed

message_font = pygame.font.SysFont('ubuntu', 30)  # game over font
score_font = pygame.font.SysFont('ubuntu', 25)   # score font
level_font = pygame.font.SysFont('ubuntu', 25)


def print_score(score):
    text = score_font.render("Score: " + str(score) , True , orange)
    screen.blit(text, (0,0))

def print_level(level_snake):
    level = level_font.render("Level: " + str(level_snake) , True , orange)
    screen.blit(level,(200,0))

def draw_snake(snake_size, snake_pixels) : # snake_pixels is list with coordinates of every square
    for pixels in snake_pixels :          # x         # y
        pygame.draw.rect(screen, green, (pixels[0], pixels[1], snake_size , snake_size))

def run_game():

    # Initialize basic variables
    game_over = False  # when game is ended
    game_close = False # when round is losed

    x = width / 2   # start position
    y = height / 2

    x_speed = 0  # change of coordinates while moving
    y_speed = 0

    snake_pixels = [] 
    snake_length = 1  # one block of snake

    food_x = round(random.randrange(0, width - snake_size) / 10) * 10
    food_y = round(random.randrange(0, height - snake_size) / 10) * 10

    count = 0 # количество съеденных фруктов
    level_snake = 0  # уровень

    snake_speed = 10 

    while not game_over :
        while game_close :  # if round is losed
            screen.fill(black)
            game_over_message = message_font.render("Game Over!" , True, red)
            screen.blit(game_over_message , (width / 3, height / 3))
            print_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_2:
                        run_game()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False


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

        # if we hit boundary, then round is losed
        if x >= width or x < 0 or y >= height or y < 0 :
            game_close = True
        
        # change the position of snake
        x += x_speed 
        y += y_speed

        screen.fill(black)  # background of screen
        pygame.draw.rect(screen, orange, (food_x, food_y, snake_size, snake_size))  # draw fruit

        # мы должны постоянно обновлять змейку, каждый раз когда мы нажимаем на клавишу
        # то есть, мы добавляем новые координаты в наш список
        snake_pixels.append((x,y)) 

        # но если координат больше чем длина змейки, то мы удаляем старые координаты
        # другими словами, мы добавляем новые координаты к хвосту и удаляем старые коориднаты головы
        if len(snake_pixels) > snake_length :   # закомментируй 
            del snake_pixels[0]

        # когда змея коснется самого себя, то игра проиграна
        for pixel in snake_pixels[:-1] :  # проверяем все координаты кроме головы
            if pixel == (x,y) :
                game_close = True  # раунд окончен, но не игра

        draw_snake(snake_size, snake_pixels)
        print_score(snake_length - 1)
        print_level(level_snake)

        if count == 3 :  # съедая по 3 фрукта уровень растет на одну ступень
            level_snake += 1
            # print_level(level_snake)
            snake_speed += 2  # также растет скорость змеи с ростом уровня
            count = 0    # устанавливаем обратно исходное значение

        pygame.display.update()

        if x == food_x and y == food_y :  # если змея кушает фрукт
            food_x = round(random.randrange(0,width - snake_size) / 10) * 10 # только в этом случае появляется новый фрукт
            food_y = round(random.randrange(0,height - snake_size) / 10) * 10
            snake_length += 1  # длина змеи растет на один блок
            count += 1 
        
        clock.tick(snake_speed)  # frequency of cycle
 
    pygame.quit()

run_game()
