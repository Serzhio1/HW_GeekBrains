# ввод данных
duration = int(input('Введите число: '))
data = []
divisions = {
    0 : 'дн',
    1 : 'час',
    2 : 'мин',
    3 : 'сек'
}
rez_string = ''

# вычисления
days = duration // 86400
data += [days]
hours = (duration // 3600) % 24
data += [hours]
minutes = (duration // 60) % 60
data += [minutes]
seconds = duration - (days * 86400 + hours * 3600 + minutes * 60)
data += [seconds]

# вывод
for i in range (len(data)):
    if data[i] != 0:
        rez_string += f'{data[i]}{divisions[i]} ' ''
print(rez_string)








