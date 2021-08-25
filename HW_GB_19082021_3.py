import json
dictionary = {}
with open('HW_GB_file_19082021_3_name.txt', 'r', encoding='utf-8') as f:
    for line in f:
        temp_str = line.replace(',', ' ').rstrip('\n')  # удаляем 'сырые символы'
        dictionary.setdefault(temp_str)
with open('HW_GB_file_19082021_3_hobby.txt', 'r', encoding='utf-8') as f:
    for i in dictionary:
        for line in f:
            # проверяем, есть ли хобби у человека или нет
            if line == '\n':  # не забываем про 'сырые символы'
                dictionary[i] = None
            else:
                dictionary[i] = line.rstrip('\n')
            break # брейк ставим для того, чтобы каждому человеку дать именно его хобби
with open('new_json', 'w') as f:
    json.dump(dictionary, f, indent = 3)
print(dictionary)