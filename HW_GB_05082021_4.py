# начальные данные
result = ''
my_list = [5.56, 45, 46.7, 234, 45.2, 87.99, 44.44, 56.21, 100, 32.01]
for i in range(len(my_list)):
    # переводим элемент в строку, чтобы было удобнее работать с ним
    elem = str(my_list[i])
    # узнаем, есть ли в цене копейки или нет
    if '.' in elem:
        temp_str_left = elem[:elem.find('.')]
        temp_str_right = elem[elem.find('.') + 1:].zfill(2)
    else:
        temp_str_left = elem
        temp_str_right = '00'
    # сообираем итогувую строку для пунка "A"
    result = result + f'{temp_str_left}руб {temp_str_right}коп, '
    # параллельно с этим редактируем вид цены
    final_str = temp_str_left + '.' + temp_str_right
    # преобразовываем элемент в тип Float, чтобы затем отсортировать итоговый список
    my_list[i] = float(final_str)
# ответ на пункт "A"
result = result[:(len(result) - 2)]
print(result)
# ответ на пункт "Б"
my_list.sort()
print(my_list)
# ответ на пункт "C"
my_list.reverse()
print(my_list)
my_list.reverse()
# ответ на пункт "D"
top_5_list = my_list[len(my_list) - 5:]
print(top_5_list)
