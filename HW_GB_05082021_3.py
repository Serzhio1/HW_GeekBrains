initial_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in range(len(initial_list)):
    temporary_list = initial_list[i].split()
    # получаем имя сотрудника
    name = temporary_list[-1]
    # редактируем имя сотрудника
    name = name.lower().capitalize()
    print(f'Привет, {name}!')
    # приводим список в приемлимый вид
    temporary_list[-1] = name
    temporary_string = ' '.join(temporary_list)
    initial_list[i] = temporary_string
print(initial_list)