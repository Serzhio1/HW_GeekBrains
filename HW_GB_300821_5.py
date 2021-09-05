class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('запуск отрисовки')
class Pen(Stationery):
    def draw(self):
        print(f'это - {self.title}')

class Pencil(Stationery):
    def draw(self):
        print(f'это - {self.title}')

class Handle(Stationery):
    def draw(self):
        print(f'это - {self.title}')

object_1 = Pen('ручка')
object_1.draw()
print()
object_2 = Pencil('карандаш')
object_2.draw()
print()
object_3 = Handle('маркер')
object_3.draw()