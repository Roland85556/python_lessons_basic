
__author__ = 'Руслан Мещеряков'

# Задание-1:
# Ваня набрал несколько операций в интерпретаторе и получал результаты:
# 	Код: a == a**2
# 	Результат: True
# 	Код: a == a*2
# 	Результат: True
# 	Код: a > 999999
# 	Результат: True

# Вопрос: Чему была равна переменная a,
# если точно известно, что её значение не изменялось?

# Подсказка: это значение точно есть ;)

print('Задание-1')
a = float('inf')
print(a==a*2)
print(a==a**2)
print(a>999999)
print("Ответ:",a)
"""
Начал с перебора, потом подумал что задачка с подвохом, пошел гуглить пришел к данному ответу.
Число удовлетворяющее первым 2 условиям это 0, но число больше 0 а значит это бесконечность
"""