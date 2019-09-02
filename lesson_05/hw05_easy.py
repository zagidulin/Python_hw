# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

print(os.getcwd())
# Создание директорий:
def create(name):
    dir_name = str(name)
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('{dir_name} создана'.format(dir_name=dir_name))
    except:
        print('{dir_name} уже существует'.format(dir_name = dir_name))


def delete(name):
    dir_name = str(name)
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.rmdir(dir_path)
        print('{dir_name} удалена'.format(dir_name=dir_name))
    except FileExistsError:
        print('{dir_name} не найдена'.format(dir_name=dir_name))


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def content(path):
    dir_list = [_ for _ in os.listdir(path) if os.path.isdir(_)]
    print("Папки в текущей директории:")
    for dir in dir_list:
        print(dir)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import shutil
import sys

def copy_file(f_orig, f_copy):
    shutil.copy(f_orig, f_copy)

f_orig = sys.argv[0]
f_copy = "copy_" + os.path.basename(f_orig)
