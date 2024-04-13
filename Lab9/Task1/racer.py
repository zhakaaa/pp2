#Imports
import pygame, sys
from pygame.locals import *
import random, time
 
#Initialzing 
pygame.init()
 
#Setting up FPS 
fps = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5   # скорость красной машины
SCORE = 0   # счетчик
MONEY = 0   # монеты 
 
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)       # шрифт для надписи "GAME OVER"
font_small = pygame.font.SysFont("Verdana", 20) # шрифт для надписи Coins:
game_over = font.render("Game Over", True, BLACK)      # надпись "Game Over"
coin_font = font_small.render("Coins:", True, BLACK)   # надпись Coins:

background = pygame.image.load("images/AnimatedStreet.png") # загрузка заднего фона
 
#Create a white screen 
SCREEN = pygame.display.set_mode((400,600))  # установка размеров экрана 
SCREEN.fill(WHITE)    # цвет экрана
pygame.display.set_caption("Game") # заголовок игры

class Coin1(pygame.sprite.Sprite):
    def __init__(self) :
        super().__init__()
        self.image = pygame.image.load('images/coin.png') 
        self.rect = self.image.get_rect()  # получения прямоугольника вокруг монеты
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40),random.randint(100,SCREEN_HEIGHT-80)) # рандомное появление монет

class Coin2(pygame.sprite.Sprite):
    def __init__(self) :
        super().__init__()
        self.image = pygame.image.load('images/coin2.png') 
        self.rect = self.image.get_rect()  # получения прямоугольника вокруг монеты
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40),random.randint(100,SCREEN_HEIGHT-80)) # рандомное появление монет
 
        
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("images/Enemy.png")
        self.rect = self.image.get_rect()           # получаем прямоугольник вокруг красной машины
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0) # рандомное появление красной машины 
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED) # движение красной машины вниз
        if (self.rect.top > 600):  # если враг вышел за границы
            SCORE += 1             # прибавляем единицу каждый раз когда враг выходит за границу
            self.rect.top = 0      
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  #  следующее появление красной машины
 
 
class Player(pygame.sprite.Sprite):    # class Player is child class of Sprite
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("images/Player.png")
        self.rect = self.image.get_rect()  # create rectangle of the same size as the image
        self.rect.center = (160, 520)      # позиция синей машины
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)  # движение вверх
        if self.rect.bottom < SCREEN_HEIGHT :
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0,5)    # движение вниз
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0) # движение влево
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)  # движение вправо
                   
#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin1()
C2 = Coin2()
 
#Creating Sprites Groups
#Группа - это множество схожих классов к примеру, все красные машины это одна группа, все монеты весом в едницу другая группа
# например в других играх, противники считается одной группой, пули главного персонажа это одна группа
# и члены этой группы являются классами
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()  # это типа массива который хранит в себе каждое изображение красной и синей машины при каждом кадре
all_sprites.add(P1)
all_sprites.add(E1)
COIN = pygame.sprite.Group()
COIN.add(C1)
COIN2 = pygame.sprite.Group()
COIN2.add(C2)

#Game Loop
while True:
       
    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    SCREEN.blit(background, (0,0)) # появление на экране заднего фона 
    scores = font_small.render(str(SCORE), True, BLACK)
    SCREEN.blit(scores, (10,10))   # появление на экране счетчика 

    SCREEN.blit(coin_font, (290,10)) # появление на экране надписи Coins:
    coins = font_small.render(str(MONEY),True, BLACK)
    SCREEN.blit(coins, (350,10))  
    SCREEN.blit(C1.image, C1.rect)   # появлние самой монеты и невидимого прямоугольника вокруг него
    SCREEN.blit(C2.image, C2.rect)   # появлние второй монеты и невидимого прямоугольника вокруг него
    
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        SCREEN.blit(entity.image, entity.rect)  # появление красной машины и синей машины и невидимых прямоугольников вокруг них
        entity.move()     # движение красной и синей машины 

 
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('carcrash.mp3').play()
          time.sleep(0.5)
                    
          SCREEN.fill(WHITE)    # экран закрашивается в белый цвет при столкновении двух машин 
          SCREEN.blit(game_over, (30,250))    # появляется надпись Game over!
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() #  при проигрыше, мы очищаем все данные с нашего якобы массива 
          time.sleep(2)
          pygame.quit() 
          sys.exit()  

    if pygame.sprite.spritecollideany(P1,COIN):  # если мы собрали монету 
        MONEY += 1    # прибавляется одна монета
        if MONEY % 3 == 0 :    # за каждые собранные 3 монеты скорость противника увеличивается
            SPEED += 1
        C1.rect.center = (random.randint(40, SCREEN_WIDTH-40),random.randint(100,SCREEN_HEIGHT-80)) # рандомное появление монет
    
    if pygame.sprite.spritecollideany(P1,COIN2):   # собрали другую монету весом в 2 очка
        MONEY += 2    # прибавляется одна монета
        if MONEY % 3 == 0 :    # за каждые собранные 3 монеты скорость противника увеличивается
            SPEED += 1
        C2.rect.center = (random.randint(40, SCREEN_WIDTH-40),random.randint(100,SCREEN_HEIGHT-80)) # рандомное появление монет


    pygame.display.update()
    FramePerSec.tick(fps)