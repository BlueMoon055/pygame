class My_name():
    def __init__(self, a, b, c, d, e):
        self.name = a
        self.close = b
        self.health = c
        self.weapon = d
        self.atk = e
    def print_info(self):
        print("Ваше имя:", self.name)
        print("Одежда:", self.close)
        print("Здоровье:", self.health)
        print("Оружие:", self.weapon)
        print("Сила удара:", self.atk)

me = My_name("Daniil", "special form", 1000000, "sword", 700000)
me.print_info()