import random
import os
import os.path
dictionary = {}
name_new_folder = 'new_project_3'
if not os.path.isdir(name_new_folder):
    os.mkdir(name_new_folder)
# создаем алфавит для названия файлов
alphabet = [chr(i) for i in range(ord('a'), ord('z'))]

# создаем возможные размеры файлов
sizes = [10 ** i for i in range(2, 6)]
for i in range(len(sizes)):
    dictionary.setdefault(sizes[i], 0)

number_of_folders = int(input('Сколько файлов вы хотите создать: '))

# создание информации для файлов(имена и контент)
for i in range(number_of_folders):
    name_new_file = ''
    # контент(размер файла)
    file_content = bytes(random.randint(0, 255) for _ in range(random.randrange(10 ** 5)))
    number_of_letters = random.randint(1, 10)
    for j in range(number_of_letters):
        name_new_file += random.choice(alphabet)
    # создаем сам файл и записываем контент
    with open(os.path.join(name_new_folder, f'{name_new_file}.bin'), 'wb') as f:
        # узнаем размер файла
        f.write(file_content)
        file_size = os.stat(os.path.join(name_new_folder, f'{name_new_file}.bin')).st_size

        # заполняем словарь
        if 0 <= file_size <= 100:
            dictionary[100] += 1
        elif 100 < file_size <= 1000:
            dictionary[1000] += 1
        elif 1000 < file_size <= 10000:
            dictionary[10000] += 1
        else:
            dictionary[100000] += 1
print(dictionary)





