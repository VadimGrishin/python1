# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла
import os
class Worker():
    def __init__(self,line):
        self.key=line[0:8].strip() + line[8:21].strip()
        self.name  = line[0:8].strip()
        self.fam   = line[8:21].strip()
        self.salar = float(line[21:36].strip())
        self.pos   = line[36:52].strip()
        self.norm  = float(line[52:].strip())
        
path = os.path.join('data', 'workers')
f = open(path, 'r', encoding='UTF-8')
workers = []
fl = f.readlines()

for line in fl:
    if fl.index(line)>0:
        workers.append(Worker(line))
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
for worker in workers:
    try:
        h = hours[worker.key]['hours']
    except:
        print('{:<10}{:<10} -- на сотрудника  не найдены часы'.format(worker.name, worker.fam))
        continue
    diff = h - worker.norm
    if  diff > 0:
        diff *= 2
    amount = round (( 1 + diff/worker.norm ) * worker.salar, 2)
    print ('{:<10}{:<10} {:>8} {:>8}{:>10}{:>11}'.format(worker.name, worker.fam, worker.norm, h, worker.salar, amount))
