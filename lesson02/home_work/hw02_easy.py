# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

print("Задача-1")
a=["яблоко", "банан", "киви", "арбуз"]
for i in range(len(a)):
    #print(i+1,'.',a[i].format())
    print('{}. {:>10}'.format((i+1),a[i]))
print("Завершение программы. Задача-1")

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

print("Задача-2")
a = ['a','b','c','d','e','f']
b = ['t','e','s','t']
for i in a:
    if i in b:
        print('Удален элемент \'{}\' из списка {}'.format(i,str(a)))
        a.remove(i)
print('Полученный список {}'.format(a))
print("Завершение программы. Задача-2")

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

print("Задача-3")
a = [1,2,3,4,5,6]
b = []
for i in range(len(a)):
    if a[i]%2==0:
        b.append(a[i]/4)
    else:
        b.append(a[i]*2)
print(b)
print("Завершение программы. Задача-3")