class Road:
    def __init__(self, length, width, weight, thickness):
        self._length = length
        self._width = width
        self.weight = weight
        self.thickness = thickness
    def calculation_method(self):
        rez = self._length * self._width * self.weight * self.thickness // 1000
        print(f'{self._length}м * {self._width}м * {self.weight}кг * {self.thickness}см = {rez}т')

new_project = Road(20, 5000, 25, 5)
new_project.calculation_method()
