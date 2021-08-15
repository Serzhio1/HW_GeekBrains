import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

count = int(input('Склько шуток вы хоите получиить: '))
preference = input('Хотите ли вы, чтобы все шутки были оригинальми(да/нет): ')

def get_jokes(n, choice):
    jokes_list = []
    "функция запрашивает от пользователя то колличство шуток, которое он хочет получить"
    if choice == 'нет':
        for i in range(n):
            jokes_list += [f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}']
        return jokes_list
    else:
        for i in range(n):
            elem_of_nouns = random.choice(nouns)
            elem_of_adverbs = random.choice(adverbs)
            elem_of_adjectives = random.choice(adjectives)
            jokes_list += [f'{elem_of_nouns} {elem_of_adverbs} {elem_of_adjectives}']
            nouns.remove(elem_of_nouns)
            adverbs.remove(elem_of_adverbs)
            adjectives.remove(elem_of_adjectives)
        return jokes_list



print(get_jokes(count, preference))


