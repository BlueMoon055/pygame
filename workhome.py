import sys

import pygame # импортируем библиотеку pygame
from random import *

class Monster: # создаём класс 
    def __init__(self, a, c, d): #конструктор, в нём  создаются свойства, вызывается при создании объекта
        self.image = pygame.image.load(a) # self.image - свойство
        self.rect = self.image.get_rect() # self.rect - свойство объекта, прямоугольник
        self.rect.x = c # self.x - свойство объекта
        self.rect.y = d #self.y - свойство объекта

    def move_cat(self): #метод движения кота убийцы
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] == True:
            self.rect.x -= 10
        if keys[pygame.K_RIGHT]:
            self.rect.x += 10
    def draw_image(self): # метод отрисовки
        win.blit(self.image, (self.rect.x , self.rect.y))

    def move_monsters(self):
        self.rect.y += 3


monster = Monster("монстр1а.png", 50, randint(-300, 0))
monster2 = Monster("монстр1а.png", 290, randint(-500, 0))
monster3 = Monster("монстр1а.png", 560, randint(-500, 0))
monster4 = Monster("монстр1а.png", 830, randint(-600, 0))
monster5 = Monster("монстр1а.png", 1200, randint(-400, 0))

monster6 = Monster("монстр2а.png", 80, randint(-100, 0))
monster7 = Monster("монстр2а.png", 300, randint(-100, 0))
monster8 = Monster("монстр2а.png", 770, randint(-100, 0))
monster9 = Monster("монстр2а.png", 840, randint(-100,0))
monster10 = Monster("монстр2а.png", 1210, randint(-100,0))

monster11 = Monster("монстр3а.png", 110, randint(-100, 0))
monster12 = Monster("монстр3а.png", 450, randint(-100, 0))
monster13 = Monster("монстр3а.png", 690, randint(-100, 0))
monster14 = Monster("монстр3а.png", 940, randint(-100,0))
monster15 = Monster("монстр3а.png", 1250, randint(-100,0))
monsters_list = [monster, monster2, monster3, monster4, monster5, monster6, monster7, monster8, monster9, monster10, monster11, monster12, monster13, monster14, monster15 ]

catkiller = Monster("кот.png", 450, 430) #создание объекта класса
fon = Monster("фон1.jpg", 0, 0) #создание объекта класса Monster
pygame.init() # важная строка
window_size=(1350, 700) #размеры окна
win = pygame.display.set_mode(window_size) # создание экрана
clock = pygame.time.Clock()  # создание фпс
bombs = []

while True: # игровой цикл
    clock.tick(40) #обновление содержимого экрана
    fon.draw_image() # отрисовка фона
    catkiller.draw_image() # отрисовка кота
    for i in monsters_list:
        i.draw_image()
        i.move_monsters()
        if i.rect.y > 600:
            i.rect.y = 0
    for i in bombs:
        i.draw_image()
        i.rect.y -= 5
        for j in monsters_list:
            if i.rect.colliderect(j.rect):
                monsters_list.remove(j)
                bombs.remove(i)

        if monsters_list == []:
            sys.exit()
    catkiller.move_cat() #применение метода движения к коту


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bomb = Monster("бомба.png",catkiller.rect.x, catkiller.rect.y)
            bombs.append(bomb)
    pygame.display.update() #обновление содержимого экрана     