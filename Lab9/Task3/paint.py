import pygame
import math

pygame.init()

WIDTH = 800
HEIGHT = 600
active_size = 0
active_color = 'white'

SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Paint")

clock = pygame.time.Clock()

#painting = []   # списко где хранится цвета и размеры
active_colors = []
active_sizes = []
active_pos = []

active_shape = pygame.draw.circle(SCREEN, 'white', (10,10), 5)

root = math.sqrt(3)

eraser = pygame.image.load('eraser.png')
eraser_rect = eraser.get_rect(topleft=(300,10))

def pick_size(size,color):
    pygame.draw.rect(SCREEN,'gray',(0,0,WIDTH,70))       # поле инструментов 
    pygame.draw.line(SCREEN,'black',(0,70), (WIDTH,70), 3)

    xl_brush = pygame.draw.rect(SCREEN, 'black', (10,10,50,50))   # очень большой размер кисти
    pygame.draw.circle(SCREEN,'white',(35,35), 20)
    l_brush = pygame.draw.rect(SCREEN, 'black', (70,10,50,50))    # большой размер кисти
    pygame.draw.circle(SCREEN,'white',(95,35), 15)
    m_brush = pygame.draw.rect(SCREEN, 'black', (130,10,50,50))   # средний размер кисти
    pygame.draw.circle(SCREEN,'white',(155,35), 10)
    s_brush = pygame.draw.rect(SCREEN, 'black', (190,10,50,50))   # маленький размер кисти
    pygame.draw.circle(SCREEN,'white',(215,35), 5)
    brush_list = [xl_brush, l_brush, m_brush, s_brush]            # список где хранится размеры

    if size == 20 :
        pygame.draw.rect(SCREEN, 'green', (10,10,50,50), 3)       # когда мы выбираем размеры, появляется зеленая рамка что создаст эффект выбора
    elif size == 15 :
        pygame.draw.rect(SCREEN, 'green', (70,10,50,50), 3)
    elif size == 10 :
        pygame.draw.rect(SCREEN, 'green', (130,10,50,50), 3)
    elif size == 5 :
        pygame.draw.rect(SCREEN, 'green', (190,10,50,50), 3)

    pygame.draw.circle(SCREEN, color, (650,35), 30)                # показывает какой цвет мы выбрали 
    pygame.draw.circle(SCREEN, 'dark gray', (650,35), 30, 3) 

    return brush_list

def pick_shape():
    #отображение прямоугольника в меню 
    rect_rect = pygame.draw.rect(SCREEN, 'white', (350,10,40,25))   
    pygame.draw.rect(SCREEN, 'dark gray', (350,10,40,25), 2)

    #отображние круга в меню
    circle_rect = pygame.draw.circle(SCREEN, 'white', (410,20), 15)
    pygame.draw.circle(SCREEN, 'dark gray', (410,20), 15, 2)

    # отображание квадрата в меню
    square_rect = pygame.draw.rect(SCREEN, 'white', (430,10,25,25))   
    pygame.draw.rect(SCREEN, 'dark gray', (430,10,25,25), 2)

    # отображение прямого треугольника в меню
    right_triangle = pygame.image.load('rigtriangle.png') 
    SCREEN.blit(right_triangle, (348,37))
    right_triangle_rect = right_triangle.get_rect(topleft=(348,37)) 

    # отображение равностороннего треугольника в меню
    equal_triangle = pygame.image.load('eqtriangle.png')
    SCREEN.blit(equal_triangle, (388,37)) 
    equal_triangle_rect = equal_triangle.get_rect(topleft=(388,37))

    # отоюражение ромба в меню
    rhombus = pygame.image.load('rhombus.png')
    SCREEN.blit(rhombus, (430,37)) 
    rhombus_rect = rhombus.get_rect(topleft=(430,37))

    # список всех фигур
    shapes = [rect_rect, circle_rect, square_rect, right_triangle_rect, equal_triangle_rect, rhombus_rect]

    return shapes

def pick_color():

    # все имеющиеся цвета
    blue = pygame.draw.rect(SCREEN, (0,0,255), (WIDTH - 35, 10,25,25))    
    red = pygame.draw.rect(SCREEN, (255,0,0), (WIDTH - 35, 35,25,25))
    green = pygame.draw.rect(SCREEN, (0,255,0), (WIDTH - 60, 10,25,25))
    yellow = pygame.draw.rect(SCREEN, (255,255,0), (WIDTH - 60, 35,25,25))
    teal = pygame.draw.rect(SCREEN, (0,255,255), (WIDTH - 85, 10,25,25))
    purple = pygame.draw.rect(SCREEN, (255,0,255), (WIDTH - 85, 35,25,25))
    white = pygame.draw.rect(SCREEN, (0,0,0), (WIDTH - 110, 10,25,25))
    black = pygame.draw.rect(SCREEN, (255,255,255), (WIDTH - 110, 35,25,25))
    color_rect = [blue,red,green,yellow,teal,purple,white,black]
    rgb_list= [(0,0,255),(255,0,0),(0,255,0),(255,255,0),(0,255,255),(255,0,255),(0,0,0),(255,255,255)]  # список где хранится все цвета

    return color_rect, rgb_list

# рисуем круг
def draw_painting_circle(color, size, pos) :
    length = len(color)
    for i in range(length):
        pygame.draw.circle(SCREEN, color[i], pos[i], size[i])
    
# рисуем прямоугольник
def draw_painting_rect(color, size, pos):
    length = len(color)
    for i in range(length):
        pygame.draw.rect(SCREEN, color[i], (pos[i][0], pos[i][1], size[i]*2, size[i]))

# рисуем квадрат
def draw_painting_square(color, size, pos):
    length = len(color)
    for i in range(length):
        pygame.draw.rect(SCREEN, color[i], (pos[i][0], pos[i][1], size[i], size[i]))


# рисуем прямой треугольник
def draw_painting_right_triangle(color, size, pos):
    length = len(color)
    for i in range(length):
        pygame.draw.polygon(SCREEN, color[i], ((pos[i][0], pos[i][1]), (pos[i][0], pos[i][1] + size[i]), (pos[i][0] + size[i], pos[i][1])))

# рисуем равносторонний треугольник
def draw_painting_equal_triangle(color, size, pos):
    length = len(color)
    for i in range(length):
        pygame.draw.polygon(SCREEN, color[i], ((pos[i][0], pos[i][1]), (pos[i][0] + 2*size[i], pos[i][1]), (pos[i][0]+size[i],pos[i][1] + size[i]*root)))

# рисуем ромб
def draw_painting_rhombus(color, size, pos):
    length = len(color)
    for i in range(length):
        pygame.draw.polygon(SCREEN, color[i], ((pos[i][0] + size[i], pos[i][1]), (pos[i][0] + 2*size[i], pos[i][1] + size[i]), (pos[i][0] + size[i], pos[i][1] + size[i]*2), (pos[i][0], pos[i][1] + size[i])))


run = True
while run:
    SCREEN.fill('white')
    
    mouse = pygame.mouse.get_pos()    # получаем позицию мыши
    left_click = pygame.mouse.get_pressed()[0]  # левая кнопка мыши 
    
    if left_click and mouse[1] > 70 :   # чтобы мы не рисовали на поле инструментов 
        active_colors.append(active_color)
        active_sizes.append(active_size)
        active_pos.append(mouse)
        # painting.append((active_color, mouse, active_size))  # передаем текущий цвет, размер, позицию в главный список 

    brushes = pick_size(active_size,active_color)
    shapes = pick_shape()
    colors, rgbs = pick_color()
    
    SCREEN.blit(eraser, (300,10))

    # так как список painting сохраняет все данные о фигуре (координаты и размер), то при выборе другой фигуры
    # фигура всех предыдущих рисунков превращается в новую фигуру
    # в функциях где мы рисуем фигуру, через цикл мы перебираем все данные списка painting поэтому такой эффект
    if active_shape == shapes[0]:    # пользовательский выбор прямоугольника
        draw_painting_rect(active_colors, active_sizes, active_pos)  
    elif active_shape == shapes[1] :   # пользовательский выбор круга
        draw_painting_circle(active_colors, active_sizes, active_pos)
    elif active_shape == shapes[2] :   # пользовательский выбор квадрата
        draw_painting_square(active_colors, active_sizes, active_pos)
    elif active_shape == shapes[3] :   # пользовательский выбор прямого треугольника
        draw_painting_right_triangle(active_colors, active_sizes, active_pos)
    elif active_shape == shapes[4]:    # пользовательский выбор равностороннего треугольника
        draw_painting_equal_triangle(active_colors, active_sizes, active_pos)
    elif active_shape == shapes[5]:    # пользовательский выбор ромба
        draw_painting_rhombus(active_colors, active_sizes, active_pos)
    

    # if mouse[1] > 70 :  
    #     pygame.draw.circle(screen, active_color, mouse, active_size)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(brushes)) :
                if brushes[i].collidepoint(event.pos):  #  если мы выбрали размер
                    active_size = 20 - (i * 5)

            for i in range(len(colors)) :
                if colors[i].collidepoint(event.pos):   #  если мы выбрали цвет
                    active_color = rgbs[i]

            for i in range(len(shapes)) :
                if shapes[i].collidepoint(event.pos):   # какую фигуру выберем 
                    active_shape = shapes[i]

            if eraser_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                active_color = (255,255,255)
                
        
    clock.tick(120)
    pygame.display.update()