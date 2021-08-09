initial_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
while i < len(initial_list):
    point = i
    elem = initial_list[i][0]
    if 32 <= ord(elem) <= 64:
        # находим те элементы, с которыми будем взаимодействовать
        right_elem = (initial_list[i])
        count_digit = 0
        for j in range(len(right_elem)):
            # теперь нужно найти только цифры!
            if 48 <= ord(right_elem[j]) <= 57:
                count_digit += 1
                help_elem = right_elem[j]
        # проверяем колличество разрядов у числа
        if count_digit == 1:
            temporary_list = list(right_elem)
            temporary_list.insert(right_elem.index(help_elem), '0')
            right_elem = ''.join(temporary_list)
            initial_list[point] = right_elem
        # задача №2 - обособить нужные элементы ковычками
        initial_list.insert(i, '"')
        initial_list.insert(i + 2, '"')
        # смещаем счетчик, для корректности работы цикла
        i += 3
    else:
        i += 1
# преобразовываем список  строку
print(initial_list)
finish_string = ' '.join(initial_list)
print(finish_string)


