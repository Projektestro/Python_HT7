import os
import shutil
import random

'''
Задача №1
Написать программу для подсчета размера всех .py файлов в текущей папке
'''

total_size = 0
for item in os.listdir():   
    if os.path.splitext(item)[-1] == '.py':
        size = os.path.getsize(os.path.join(os.getcwd(), item))
        print(f'Размер файла "{item}" составляет {size} байт')
        total_size += size
print(f'Общий размер всех файлов с расширением ".py" составляет {total_size} байт')

'''
Задача № 2
Написать программу, которая находит все файла .txt и 
переносит их в подпапку backup, которую нужно создать.
'''

# Генерация файлов с расширением .txt в количестве от 1 до 100
for i in range(random.randint(1, 100)):
    file_name = 'file{}.txt'.format(i)
    file_txt = open(file_name, 'w')
    file_txt.close()

# Создание подпапки backup с обработкой исключения
try:
    os.mkdir('backup')
except FileExistsError:
    print('Файл "backup" создан')

# Перенос с заменой файлов с расширением .txt из текущей папки в подпапку backup
for item in os.listdir():
    if os.path.splitext(item)[-1] == '.txt':
        shutil.move(os.path.join(os.curdir, item), os.path.join('backup', item))