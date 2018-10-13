# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

def nod(a,b):
    if a<b:
        a, b = b, a
    if b==0:
        return a
    while a%b != 0:
        b, a = a%b, b
    return b

print('Задание-1'+'-'*20)
expr = '-5/6 - - 4/7 +1/42 + 1/3 + 38/42 - 13/13'
expr = expr.strip() + '+'
sign = [1]  # знаки слагаемых
num = []    # числители слагаемых
denom = []  # знаменатели слагаемых
process = 1 #  - чтение знака, 2 - чтение числителя, 3 - чтение знаменателя
nterm=0
for ch in expr:
    if ch != ' ':
        issign = (ch in ('+', '-'))
        if process == 1:
            if ch =='-':
                sign[nterm] *= -1
            elif ch.isdigit():
                process = 2
                denom.append(1)
                snum = ch
        elif process == 2:
            if ch.isdigit():
                snum +=ch
            elif ((ch == '+') or (ch == '-')):
                num.append( int(snum) )
                process = 1
                nterm += 1
                sign.append( int(ch + '1'))
            elif ch == '/':
                num.append( int(snum) )
                process = 3
                sdenom = ''
        elif process == 3:
            if issign:
                denom[nterm] =( int(sdenom) )
                process = 1
                nterm += 1
                sign.append( int(ch + '1') )
            elif ch.isdigit:
                sdenom += ch
            
common_denom = denom[0]
for i in range(1, len(denom)):
    common_denom *= denom[i]
common_num = 0

for i in range(0, len(denom)):
    common_num += sign[i]*num[i]*common_denom/denom[i]

d = nod(abs(common_num), abs(common_denom))
common_num, common_denom = int(common_num / d), int(common_denom / d)

int_part = common_num // common_denom
common_num =  common_num % common_denom 
if int_part == 0:
    int_part = ''
else:
    int_part = str(int_part) + ' '
if common_num == 0:
    fract_part = ''
else:
    fract_part = '{}/{}'.format(common_num, common_denom) 
if int_part + fract_part == '':
   int_part = '0' 
print (int_part + fract_part)
print (float(int_part)+ float(common_num)/ float(common_denom)) # контрольная проверка
print (str(-5/6 - - 4/7 +1/42 + 1/3 + 38/42 - 13/13))

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

print('Задание-2'+'-'*20)
import os
path = os.path.join('data', 'workers')
f = open(path, 'r', encoding='UTF-8')
workers = dict()
fl = f.readlines()

for line in fl:
    if fl.index(line)>0:
        key=line[0:8].strip() + line[8:21].strip()
        worker = dict()
        worker['name']  = line[0:8].strip()
        worker['fam']   = line[8:21].strip()
        worker['salar'] = float(line[21:36].strip())
        worker['pos']   = line[36:52].strip()
        worker['norm']  = float(line[52:].strip())
        workers[key] = worker
f.close

path = os.path.join('data', 'hours_of')
f = open(path, 'r', encoding='UTF-8')
hours = dict()
fl = f.readlines()

for line in fl:
    if fl.index(line)>0:
        key=line[0:8].strip() + line[8:21].strip()
        hour = dict()
        hour['hours'] = float(line[21:36].strip())
        hours[key] = hour
f.close

print ('{:<10}{:<10} {:>8} {:>8}{:>10}{:>11}'.format('Имя', 'Фамилия', 'Норма, ч', 'Факт, ч', 'Ставка', 'Оплата') )
for key, person in workers.items():
    try:
        h = hours[key]['hours']
    except:
        print('{:<10}{:<10} -- на сотрудника  не найдены часы'.format(person['name'], person['fam']))
        continue
    diff = h - person['norm']
    if  diff > 0:
        diff *= 2
    amount = round (( 1 + diff/person['norm'] ) * person['salar'], 2)
    print ('{:<10}{:<10} {:>8} {:>8}{:>10}{:>11}'.format(person['name'], person['fam'], person['norm'], h, person['salar'], amount))


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
print('Задание-3'+'-'*20)
import os, shutil

if os.path.exists('data/res'): # зачистить, если раньше уже запускали программу
    respath = os.path.join('data/res')
    shutil.rmtree(respath)
os.mkdir('data/res')

path = os.path.join('data', 'fruits.txt')
f = open(path, 'r', encoding='UTF-8')

for line in f:
    if line.strip() != '':
        with open('data/res/fruits_{}.txt'.format(line[0]), 'a', encoding='utf-8') as g:
            g.write(line)
print('Файлы созданы в папке data/res')