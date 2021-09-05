import os
import os.path
new_name_folder = 'my_project_1'
number = int(input('Сколько файлов вы хотите создать: '))

# создание папки
if not os.path.isdir(new_name_folder):
    os.mkdir(new_name_folder)
os.chdir(new_name_folder)

# создание файлов в папке
for i in range(number):
    name_file = input('Укажите имя файла: ')
    permission = '.' + input('Укажите разрешение файла: ')
    the_finished_file = name_file + permission
    if os.path.exists(the_finished_file) == False:
        new_file = open(the_finished_file, 'w')
        new_file.close()
    else:
        print('такой файл уже сущесвует')



