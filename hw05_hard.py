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
import os, sys, shutil

print('Вы запустили: ', sys.argv[0])


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("cp <src> <dest> - создание копии указанного файла")
    print("rm <file_name> - удаление указанного файла")
    print(":) можно добавить и другие функции при необходимости")
    print("ping - тестовый ключ")


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

def copy_file():
    if not file_name or not new_name:
        print("Укажите имена копируемого и нового файла:  python hw05_hard.py cp source dest")
        return
    shutil.copyfile(file_name, new_name)
    print('Из файла {} создана копия {}'.format(file_name, new_name))

def remove_file():
    if not file_name:
        print("Укажите имя удаляемого файла:  python hw05_hard.py rm file")
        return
    if input('Точно удалить {}? y/n: '.format(file_name)) == 'y':
        try:
            os.remove(file_name)
            print('Файл {} удален'.format(file_name))
        except FileNotFoundError:	
            print('Его и так нету')

def ping():
    print("pong")

do = {
    "help": print_help,
    "mkdir": make_dir,
    "cp": copy_file,
    "rm": remove_file,
    "ping": ping
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
    new_name = sys.argv[3]
except IndexError:
    new_name = None
    
try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ " + key)
        print("Укажите ключ help для получения справки")
