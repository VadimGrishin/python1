# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    def maxround(n): # максимальное круглое целое, не превышающее n
        ndg=0
        while n >= 1:
           n= n/10
           ndg +=1
        n *=10
        for i in range(0,11):
            if i>n:
                n=i-1
                break
        # print (n,ndg-1)
        return n*10**(ndg-1)

    def roundinteger(n): # округление до целого
        s=0
        while n - s >= 1:
            s += maxround(n - s)
        if n - s >= 0.5:
            s +=1
        return s

    return roundinteger (number * 10**ndigits) / 10**ndigits

print('Задание-1'+'-'*20)
print (my_round(2.1234567, 5))

# my_round(2.1234567, 5)


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    s = str(ticket_number)
    s.strip()
    if len(s) != 6:
        return ('Введите корректный номер')
    lucky = sum( list(map(int, list(s[0:3]) ))) == sum( list(map(int, list(s[3:]) )))
    return ('У Вас счастливый билет' if lucky else 'Не повезло')
        
print('Задание-2'+'-'*20)
print (lucky_ticket('123456'))  

