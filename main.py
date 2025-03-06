import pygame
pygame.init() #инициализация
window_size=(300, 300) #размеры окна
screen=pygame.display.set_mode(window_size) #создаём экран с размерами
pygame.display.set_caption("моя игра") #название окна
background_color = (0, 0, 225)#заливка фона цветом
clock = pygame.time.Clock() #создание игрового таймера (фпс)
color = (0, 0, 130)
size = 30
font = pygame.font.SysFont("Arial", size)
text = font.render("Ваня", True, color)
screen.blit(text, (50, 50))
x = 150
y = 150
while True: #игровой цикл
    screen.fill(background_color)  # применение заливки фона
    r = pygame.Rect(x, y, 100, 50)  # создание прямоугольника
    clock.tick(40) #частота обновления сцены (40 кдр / с)
    pygame.draw.rect(screen, color, r)
    pygame.display.update()  # обновление содержимого экрана
    for event in pygame.event.get(): #проходимся по событиям
        if event.type == pygame.QUIT: #если нажали на крестик
            pygame.QUIT() #выход из игры
        if event.type == pygame.KEYDOWN: #если клавиша нажата
            if event.key == pygame.K_a: #если клавиша 'а'
                x = x - 5
            if event.key == pygame.K_d: #если клавиша 'd'
                x = x + 5
            if event.key == pygame.K_w: #если клавиша 'w'
                y = y - 5
            if event.key == pygame.K_s: #если клавиша 's'
                y = y + 5