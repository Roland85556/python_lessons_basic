
__author__ = 'Руслан Мещеряков'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.


print("Задача-1. цикл while")
while True:
    num = input('Введите число: ')
    max_num = 0
    if num.isdigit():
        l=len(num)
        num = int(num)
        while l>0:
            l-=1
            if (num//(10**l)) > max_num:
                max_num = num//(10**l)
            num-=(num//(10**l))*(10**l)
        print("Самая большая цифра -", max_num)
        print("Завершение программы. Задача-1. цикл while")
        break
    else:
        print("Вы ввели не число")
        continue

print("Задача-1. цикл for")
while True:
    num = input('Введите число: ')
    max_num = 0
    if num.isdigit():
        for l in range(len(num),0,-1):
            l-=1
            num=int(num)
            if (num//(10**l)) > max_num:
                max_num = num//(10**l)
            num-=(num//(10**l))*(10**l)
        print("Самая большая цифра -", max_num)
        print("Завершение программы. Задача-1. цикл for")
        break
    else:
        print("Вы ввели не число")
        continue

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

print("Задача-2. Действия над числами")
a = int(input('Введите значение первой переменной: '))
b = int(input('Введите значение второй переменной: '))
print('Первая переменная: ',a)
print('Вторая переменная: ',b)
print('Замена значений переменных')
b += a
a = b - a
b -= a
print('Первая переменная: ',a)
print('Вторая переменная: ',b)
print("Завершение программы. Задача-2. Действия над числами")


print("Задача-2. Синтаксис кортежей")
#тут было бы уместней сказать синтаксис списков Python, а не кортежей
a = int(input('Введите значение первой переменной: '))
b = int(input('Введите значение второй переменной: '))
print('Первая переменная: ',a)
print('Вторая переменная: ',b)
print('Замена значений переменных')
c = (a,b)
a=c[1]
b=c[0]
print('Первая переменная: ',a)
print('Вторая переменная: ',b)
print("Завершение программы. Задача-2. Синтаксис кортежей")

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

import math

print("Задача-3")
print("Введите коэфициенты уравнения")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

D = b**2 - 4*a*c
if D > 0:
    x1 = (-b+math.sqrt(D))/(2*a)
    x2 = (-b-math.sqrt(D))/(2*a)
    print("Дискриминант", D, "> 0. Найдено два корня уравнения: X1 =", x1,"X2 =", x2)
elif D == 0:
    x = -b/(2*a)
    print("Дискриминант", D, "= 0. Найден один корень уравнения: X =", x)
else:
    print("Дискриминант", D, "< 0. Корней нет")
print("Завершение программы. Задача-3")

