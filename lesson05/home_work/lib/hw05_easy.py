# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import shutil


def make_dir(name):
    dir_path = os.path.join(os.getcwd(), name)
    try:
        os.mkdir(dir_path)
        print('Папка "{}" создана'.format(name))
    except FileExistsError:
        print('Папка "{}" уже существует'.format(name))
    return True


def remove_dir(name):
    dir_path = os.path.join(os.getcwd(), name)
    try:
        os.rmdir(dir_path)
        print('Папка "{}" удалена'.format(name))
    except FileNotFoundError:
        print('Папки "{}" не существует'.format(name))


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def list_dir(path=os.curdir, ltype='all'):
    for e in os.listdir(path):
        if ltype == 'all':
            print('[ {} ]'.format(e))
        elif ltype == 'file':
            if os.path.isfile(e):
                print('[ {} ]'.format(e))
        elif ltype == 'dir':
            if os.path.isdir(e):
                print('[ {} ]'.format(e))
        elif ltype == 'link':
            if os.path.islink(e):
                print('[ {} ]'.format(e))
        else:
            print('Некорректно указан тип')


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def copy_this():
    file = os.path.realpath(__file__)
    if os.path.isfile(file + '.copy'):
        print('Невозможно скопировать исполняемый файл\n'
              'Файл "{}.copy" уже существует'.format(file))
    else:
        shutil.copyfile(file, file + '.copy')
        print('Файл "{}" скопирован'.format(file))


def init():
    while True:
        menu = input('\n'
                     'Выберите пункт меню:\n'
                     'Задача-1:\n'
                     '[1] - Создать папки dir_1 - dir_9\n'
                     '[2] - Удалить папки dir_1 - dir_9\n'
                     'Задача-2:\n'
                     '[3] - Отобразть папки в данной директории\n'
                     'Задача-3:\n'
                     '[4] - создать копию исполняемого файла\n'
                     '[5] - Выход\n\n')

        if menu == '5':
            print('Завершение работы программы.')
            break
        elif menu == '1':
            for i in range(9):
                make_dir('dir_' + str(i + 1))
        elif menu == '2':
            for i in range(9):
                remove_dir('dir_' + str(i + 1))
        elif menu == '3':
            list_dir()
        elif menu == '4':
            copy_this()


if __name__ == '__main__':
    init()
