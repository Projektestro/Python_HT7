import os

'''
Задача №1
Написать программу для подсчета размера всех .py файлов в текущей папке
'''

# size = {}
total_size = 0
path = os.curdir
for item in os.listdir(path):   
    if os.path.splitext(item)[-1] == '.py':
#         size[item] = str(os.path.getsize(os.path.join(os.getcwd(), item))) + ' байт'
        size = os.path.getsize(os.path.join(os.getcwd(), item))
        print(f'Размер файла "{item}" составляет {size} байт')
        total_size += size
print(f'Общий размер всех файлов с расширением ".py" составляет {total_size} байт')
# print(size)
  
'''
Задача № 2
Написать программу, которая находит все файла .txt и 
переносит их в подпапку backup, которую нужно создать.
'''