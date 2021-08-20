tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
len_tut = len(tutors)
len_klas = len(klasses)
if len_tut > len_klas:
    klasses.extend([None] * (len_tut - len_klas))
gen = ((tutors[i], klasses[i]) for i in range(len_tut))
print(list(gen))