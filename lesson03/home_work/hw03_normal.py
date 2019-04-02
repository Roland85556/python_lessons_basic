# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    f=[]
    a,b=0,1
    for i in range(m):
        f.append(b)
        a,b=b,a+b
    return f[n-1:m:1]

print(fibonacci(5, 15))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    n=[]
    l=len(origin_list)
    while l>0:
        for i in range(l):
            if min(origin_list) == origin_list[i]:
                l-=1
                n.append(origin_list.pop(i))
                break
    return print(n)

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def test(x):
    if float(x) > 0:
        return True
    else:
        return False

def f_test(func,x):
    a=[]
    for i in x:
        if func(i):
            a.append(i)
    if type(x) is tuple:
        a = tuple(a)
    if type(x) is set:
        a = set(a)
    if type(x) is str:
        a = ''.join(a)
    return a

print(f_test(test, {2, 10, -12, 2.5, 20, -11, 4, 4, 0}))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
import math
a1, b1, c1, d1 = (1, 1), (3, 4), (8, 4), (6, 1)

def parall_check(a,b,c,d):
    #находим стороны
    ab = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
    bc = math.sqrt((b[0]-c[0])**2 + (b[1]-c[1])**2)
    cd = math.sqrt((c[0]-d[0])**2 + (c[1]-d[1])**2)
    ad = math.sqrt((a[0]-d[0])**2 + (a[1]-d[1])**2)
    #В параллелограмме противоположные стороны равны
    if ab==cd and bc==ad:
        #находим координаты середин диагоналей AC и BD
        aco=((a[0]+c[0])/2,(a[1]+c[1])/2)
        bdo=((b[0]+d[0])/2,(b[1]+d[1])/2)
        if aco==bdo:
            return print('Вершины a, b, c, d образуют паралелограмм')
        else:
            return print('не паралелограмм')
    else:
        return print('не паралелограмм')

parall_check(a1,b1,c1,d1)
