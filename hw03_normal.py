# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    def genfibo(m):
        a = [1, 1]
        while len (a)< m:
            i = len(a) - 1
            x = a[i-1] + a[i]
            a.append(x)
        return a
    return genfibo(m)[n-1:]

print('Задание-1'+'-'*20)
print(fibonacci(1, 10))
print(fibonacci(8, 10))
    

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    for j in range(1, len(origin_list)):
        f = 0
        for i in range(0,len(origin_list) - j):
            if origin_list[i]>origin_list[i+1]:
                origin_list[i], origin_list[i+1] = origin_list[i+1], origin_list[i]
                f=1
        if f==0:
            break
    return origin_list

print('Задание-2'+'-'*20)

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(func, itr):
    a=list(itr)
    x=[]
    for el in a:
        if func(el):
            x.append(el)
    if type(itr)==str:
        res = ''
        for ch in x:
            res +=ch
    else:
        res = type(itr) (x)
    return res

print('Задание-3'+'-'*20)
print(my_filter(lambda x:int(x)>1, '123123'))
print(my_filter(lambda x:x!='a', 'abcabca'))
print(my_filter(lambda x:int(x)>1, (1,23,0,2,3)))
print(my_filter(lambda x:int(x)>1, set([1,23,0,2,3])))
print(my_filter(lambda x:int(x)>1, (1,23,0,2,3)))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def vector(f,g):
    return [ g[0] - f[0], g[1] - f[1] ]

print('Задание-4'+'-'*20)    
a1 = (-1, -2)
a2 = (0, 1)
a4 = (1, -1)
a3 = (1, 2)
res = not (a1==a2 or a1==a3 or a1==a4 or a2==a3 or a2==a4 or a3==a4)
res = res and (vector(a1,a2) == vector(a3,a4) or vector(a1,a2) == vector(a4,a3) or vector(a1,a3) == vector(a2,a4) or vector(a1,a3) == vector(a4,a2))
print('Параллелограмм' if res else 'Не параллелограмм')
