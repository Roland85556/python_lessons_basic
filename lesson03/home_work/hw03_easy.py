# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    a = 10**ndigits
    b = int(number*a)
    c = number*a - b
    if c >= 0.5:
        n = (b+1)/a
    else:
        n = b/a
    return n

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    a = str(ticket_number)
    l=0
    r=0
    if len(a)%2==0:
        for i in range(int(len(a)/2)):
            l+=int(a[i])
            r+=int(a[-i-1])
        check = l==r
    else:
        check = False
    return check


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
