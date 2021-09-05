import os
import os.path

# создание новой директории
name_new_directory = 'my_project_2'
name_main_folder = 'templates'
rez_hierarchy = os.path.join(name_new_directory, name_main_folder)
if not os.path.isdir(name_new_directory) and not os.path.isdir(name_main_folder):
    os.makedirs(rez_hierarchy)

# переходим в нужную директорию
os.chdir(name_new_directory)
os.chdir(name_main_folder)

# создаем родительсике папки с файлами внутри
number_of_folders = int(input('Сколько папок вы хотите создать? '))
i = 1
while i <= number_of_folders:
    name_folder = input('введите имя папки ')
    os.mkdir(name_folder)
    os.chdir(name_folder)
    number_of_files = int(input(f'Сколько файлов вы хотите создать в папке {name_folder}? '))
    for j in range(number_of_files):
        name_file = input('Укажите имя файла: ')
        permission = input('Укажите разрешение файла: ')
        result = name_file + '.' + permission
        if not os.path.exists(result):
            file = open(result, 'w')
        file.close()
        print('файл создан успешно!')
    i += 1
    os.chdir('..')
