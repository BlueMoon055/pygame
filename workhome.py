import pygame
pygame.init() #инициализация
window_size=(300, 300) #размеры окна
screen=pygame.display.set_mode(window_size) #создаём экран с размерами
pygame.display.set_caption("моя игра") #название окна
background_color = (0, 0, 225)#заливка фона цветом
screen.fill(background_color) #применение заливки фона
clock = pygame.time.Clock() #создание игрового таймера (фпс)
r = pygame.Rect(150, 150, 100, 50) #создание прямоугольника
color = (0, 0, 130)
font = pygame.font.SysFont("Arial", size)
text = font.render("Ваня", True, color)
screen.blit(text, (50, 50))
while True: #игровой цикл
    clock.tick(40) #частота обновления сцены (40 кдр / с)
    pygame.display.update() #обновление содержимого экрана
    pygame.draw.rect(screen, color, r)
    for event in pygame.event.get(): #проходимся по событиям
        if event.type == pygame.QUIT: #если нажали на крестик
            pygame.QUIT() #выход из игры