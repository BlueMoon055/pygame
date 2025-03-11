import pygame
pygame.init()
window_size=(600, 600)
win = pygame.display.set_mode(window_size)
color = 0, 0, 255
x = 300
y = 150
rad = 100
while True:
    win = pygame.display.set_mode(window_size)
    pygame.draw.circle(win, (0, 255, 255), (x, y), rad)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = x - 10
            if event.key == pygame.K_RIGHT:
                x = x + 10
            if event.key == pygame.K_UP:
                y = y - 10
            if event.key == pygame.K_DOWN:
                y = y + 10