import pygame # импортируем библиотеку pygame

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

sushi = Food("суши.png", 30, 5)
sushi2 = Food("суши.png", 200, 5)
sushi3 = Food("суши.png", 370, 5)
sushi4 = Food("суши.png", 540, 5)
sushi5 = Food("суши.png", 710, 5)
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
    sushi.draw_image()
    sushi2.draw_image()
    sushi3.draw_image()
    sushi4.draw_image()
    sushi5.draw_image()
    plate.move_plate() #применение метода движения к тарелки
    sushi.move_food()
    sushi2.move_food()
    sushi3.move_food()
    sushi4.move_food()
    sushi5.move_food()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()

    pygame.display.update() #обновление содержимого экрана