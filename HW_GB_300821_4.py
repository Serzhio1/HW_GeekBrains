class Car:

    def __init__(self, speed, colour, name, is_police = False):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = is_police
        print(f'машаина едет со скоростью {self.speed} км/ч')
        print(f'цвет машины - {self.colour}')
        print(f'машина - {self.name}')
        print(f'эта машина полицейская - {self.is_police}')

    def go(self):
        print('машина поехала')

    def stop(self):
        print('машина остановилась')

    def turn(self, side):
        print(f'машина повернула на{side}')

    def show_speed(self):
        print(f'текущая скорость автомобиля - {self.speed}')

class Towncar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('превышение скорости!')
        else:
            print(self.speed)

class Sportcar(Car):
    pass

class Workcar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('превышение скорости!')
        else:
            print(self.speed)

class Policecar(Car):
    pass

car_1 = Towncar(141, 'зеленый', 'ЗИЛ', True)
car_1.show_speed()
print()
car_2 = Workcar(234, 'синий', 'Lexus', False)
car_2.show_speed()
print()
car_3 = Sportcar(124, 'черный', 'BMW', True)
print()
car_4 = Policecar(3245, 'белый', 'Lada', False)