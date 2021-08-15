def num_translate(num):
    if num in translate:
        return str(translate[num])

translate = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять',
}

num = input('Введите числительное на английском: ')
lower_num = num.lower()
translated = num_translate(lower_num)
# проверка на заглавную  букву
if 65 <= ord(num[0]) <= 90:
    print(translated.capitalize())
else:
    print(translated)




