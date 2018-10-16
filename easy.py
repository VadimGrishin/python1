## Библиотека функций для normal
import os

def goto_next_dir(dirname):
    try:
        os.chdir(dirname)
    except:
        print(' ' + dirname + ' - такой папки не существует')

def list_cur_dir():
    print(' ' + '..')
    for ob in os.listdir(os.getcwd()):
        if os.path.isdir(ob):
            print(' ' + ob)
    for ob in os.listdir(os.getcwd()):
        if os.path.isfile(ob):
            print(' ' + '-' + ob)
    
def rm_dir(dirname):
    try:
        os.rmdir(dirname)
        print(' ' + 'Папка удалена: ' + dirname)
    except:
        print(' ' + dirname + ' - такой папки не существует')
        
def mk_dir(dirname):
    try:
        os.mkdir(dirname)
        print(' ' + 'Папка создана')
    except:
        print(' ' + dirname + ' - такая папка уже существует')
