import pygame

class Food:
    def __init__(self, a, c, d): #конструктор, в нём создаются свойства, вызывается при создании объекта
        self.image = pygame.image.load(a) # self.image - свойство
        self.rect = self.image.get_rect() # self.rect - свойство объекта, прямоугольник
        self.x = c # self.x - свойство объекта
        self.y = d #self.y - свойство объекта

    def draw_image(self): # метод отрисовки
        win.blit(self.image, (self.x , self.y))

plate = Food("тарелка.png", 450, 550) #создание объекта класса Food
fon = Food("кухня.jpg", 0, 0)
pygame.init()
window_size=(900, 600)
win = pygame.display.set_mode(window_size)
while True:
    clock = pygame.time.Clock()
    clock.tick(40)
    fon.draw_image()

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
    pygame.display.update()
