# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

# from random import randint

# n_set = set(randint(1, 20) for i in range(int(input('Введите кол-во элементов первого множества: '))))
# # print(n_set)
# m_set = set(randint(1, 20) for i in range(int(input('Введите кол-во элементов второго множества: '))))
# print(m_set)
# s_set = sorted(n_set.intersection(m_set))
# print(*s_set)

from random import randint


set_1 = set(randint(1, 10) for i in range(
    int(input('Введите кол-во элементов первого множества: '))))
print(*set_1)
set_2 = set(randint(1, 10) for i in range(
    int(input('Введите кол-во элементов второго множества: '))))
print(*set_2)


kool = list(set_1 and set_2)
kool.sort()

for i in kool:
    print(i, end=' ')
