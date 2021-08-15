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
print(num_translate(num))
