# Задача №3. Решение в группах
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

n1 = int(input("Введите число учащихся в 1 классе: "))
n2 = int(input("Введите число учащихся в 3 классе: "))
n3 = int(input("Введите число учащихся в 7 классе: "))

a = n1 // 2 + n1 % 2
b = n2 // 2 + n2 % 2
c = n3 // 2 + n3 % 2

sum = (a + b + c)

print(sum)