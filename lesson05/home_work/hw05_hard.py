# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.


# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл (запросить подтверждение операции)")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")


def copy_file():
    if not file_name:
        print("Необходимо указать путь к файлу вторым параметром")
        return
    if os.path.isfile(file_name + '.copy'):
        print('Невозможно скопировать исполняемый файл\n'
              'Файл "{}.copy" уже существует'.format(file_name))
    else:
        shutil.copyfile(file_name, file_name + '.copy')
        print('Файл "{}" скопирован'.format(file_name))


def remove_file():
    if not file_name:
        print("Необходимо указать путь к файлу вторым параметром")
        return
    if os.path.isfile(file_name):
        q = input('Вы действительно хотите удалить файл {}. [Y/N]: '.format(file_name))
        if q == 'Y':
            os.remove(file_name)
            print('Файл "{}" удален'.format(file_name))
        elif q == 'N':
            print('Удаление файла - {} ОТМЕНЕНО'.format(file_name))
        else:
            print('Неверный ключ ответа')
            return
    else:
        print('{} - не является файлом'.format(file_name))


def change_dir():
    if not file_name:
        print("Необходимо указать путь для перехода вторым параметром")
        return
    try:
        os.chdir(dir_name)
        print('Успешно перешел')
        print('Текущая папка {}\n'.format(os.getcwd()))
        print('В текущей папке находятся следующие элементы')
        list_dir()
    except FileNotFoundError:
        print('Невозможно перейти')


def list_dir():
    for e in os.listdir(os.curdir):
        print('[ {} ]'.format(e))
    return


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": remove_file,
    "cd": change_dir,
    "ls": list_dir,
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    file_name = sys.argv[2]
except IndexError:
    file_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
