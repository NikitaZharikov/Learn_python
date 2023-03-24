# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def powNumbers(num1, num2):
    if num2 == 0:
        return 1
    else:  # для читаемости добавил else
        return num1 * powNumbers(num1, num2 - 1)


num1 = int(input('Введите число: '))
num2 = int(input('Введите степень: '))
print(powNumbers(num1, num2))
