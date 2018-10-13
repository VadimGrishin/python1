# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
print('\nЗадание 1' + '-'*20)
if input("Введите 'm', чтобы создать директории: ") == 'm':
    if not os.path.exists('dir_1'):
        for i in range(1, 10):
            os.mkdir('dir_' + str(i).strip())
    else:
        if input('Папки уже существуют, удалить? - "d"') == 'd':
            for i in range(1, 10):
                os.rmdir('dir_' + str(i).strip())

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
print('\nЗадание 2' + '-'*20)
for ob in os.listdir(os.getcwd()):
    if os.path.isdir(ob):
        print(ob)
        
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import shutil
print('\nЗадание 3' + '-'*20)
file = os.path.split(__file__)[1]
shutil.copyfile(os.path.abspath(__file__),'copy_' + file)


