# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве
# и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.

# Ввод: 5
# Ввод: 1

# 1 2 1 2 2
# Вывод: 2

listRange = abs(int(input('Размер списка: ')))
inputElemList = input("Элементы списка через пробел!: ").split()
elemList = list(map(int, inputElemList))
if len(elemList) != listRange:
    print('Попробуй еще разок!')
else:
    findCountElems = int(
        input('Число, которое хотите найти в списке: '))
    count = 0
    for i in range(listRange):
        if elemList[i] == findCountElems:
            count += 1
    print(f'Число {findCountElems} встречается в списке {count} раз')
