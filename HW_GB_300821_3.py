class Worker:

    # словарь для вычисления оклада сотрудника
    dictionary_for_salary = {
        'wage': 0,
        'bonus': 0
    }

    # системный метод родительского класса
    def __init__(self, name, surname, position, wage, bonus):
        self.wage = wage
        self.bonus = bonus
        self.name = name
        self.surname = surname
        self.position = position
        Worker.dictionary_for_salary['wage'] = self.wage
        Worker.dictionary_for_salary['bonus'] = self.bonus
        self._income = Worker.dictionary_for_salary['wage'] + Worker.dictionary_for_salary['bonus']
        print(Worker.dictionary_for_salary)

class Position(Worker):
    # методы дочернего класса
    def get_full_information(self):
        print(f'новый сотрудник "{self.name} {self.surname}" занимает должность "{self.position}"')

    def get_total_income(self):
        print(self._income)

new_person_1 = Position('сергей', 'махов', 'middle', 10000, 5000)
new_person_1.get_full_information()
new_person_1.get_total_income()

