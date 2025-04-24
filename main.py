import pygame # импортируем библиотеку pygame
from random import *

class Food: # создаём класс food
    def __init__(self, a, c, d): #конструктор, в нём создаются свойства, вызывается при создании объекта
        self.image = pygame.image.load(a) # self.image - свойство
        self.rect = self.image.get_rect() # self.rect - свойство объекта, прямоугольник
        self.rect.x = c # self.x - свойство объекта
        self.rect.y = d #self.y - свойство объекта

    def move_plate(self): #метод движения тарелки
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] == True:
            self.rect.x -= 10
        if keys[pygame.K_RIGHT]:
            self.rect.x += 10
    def draw_image(self): # метод отрисовки
        win.blit(self.image, (self.rect.x , self.rect.y))

    def move_food(self):
        self.rect.y += 10


onigiri = Food("анигири.png", 20, randint(-300, 0))
onigiri2 = Food("анигири.png", 190, randint(-500, 0))
onigiri3 = Food("анигири.png", 360, randint(-500, 0))
onigiri4 = Food("анигири.png", 530, randint(-600, 0))
onigiri5 = Food("анигири.png", 700, randint(-400, 0))

sushi = Food("суши.png", 30, randint(-100, 0))
sushi2 = Food("суши.png", 200, randint(-100, 0))
sushi3 = Food("суши.png", 370, randint(-100, 0))
sushi4 = Food("суши.png", 540, randint(-100,0))
sushi5 = Food("суши.png", 710, randint(-100,0))
food_list = [onigiri, onigiri2, onigiri3, onigiri4, onigiri5, sushi, sushi2, sushi3, sushi4, sushi5]

plate = Food("тарелка.png", 450, 430) #создание объекта класса Food
fon = Food("кухня3.jpg", 0, 0) #создание объекта класса Food
pygame.init() # важная строка
window_size=(900, 600) #размеры окна
win = pygame.display.set_mode(window_size) # создание экрана
clock = pygame.time.Clock()  # создание фпс

while True: # игровой цикл
    clock.tick(40) #обновление содержимого экрана
    fon.draw_image() # отрисовка фона
    plate.draw_image() # отрисовка тарелки
    for i in food_list:
        i.draw_image()
        i.move_food()
        if i.rect.y > 600:
            i.rect.y = 0
        if plate.rect.colliderect(i.rect):
            food_list.remove(i)
        if food_list == []:
            pygame.QUIT()
    plate.move_plate() #применение метода движения к тарелки


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()

    pygame.display.update() #обновление содержимого экрана