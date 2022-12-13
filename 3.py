# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.


# def fill_list(lenght):
#     from random import randint
#
#     list = []
#     for i in range(lenght):
#         list.append(randint(-10, 10))
#     return list
#
# size = 10
# lst = fill_list(size)
# print(lst)
#
# i = 1
# sum = 0
# while i < size:
#     sum += lst[i]
#     i += 2
# print("Сумма элементов на нечетных позициях равна", sum)

# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# def fill_list(lenght):
#     from random import randint
#
#     list = []
#     for i in range(lenght):
#         list.append(randint(-10, 10))
#     return list
#
# size = 10
# lst = fill_list(size)
# print(lst)
# i = 0
# j = -1
# sum_el = []
# while i < size/2 and j >= -size/2:
#     sum_el.append(lst[i] + lst[j])
#     i += 1
#     j -= 1
# print(sum_el)

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.


# def fill_list_float(lenght):
#     import random
#
#     list = []
#     for i in range(lenght):
#         list.append(round(random.uniform(0, 10), 2))
#     return list
#
# size = 10
# lst = fill_list_float(size)
# print(lst)
#
# lst2 = []
# i = 0
# while i < size:
#     lst2.append(round((lst[i]%1), 2))
#     i += 1
#
# min = min(lst2)
# max = max(lst2)
# diff = max - min
# print(f"Разница между максимальным и минимальным значениями дробной части элементов равна: {diff}")

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# print("Введите натуральное число:")
# a = int(input())
# b = ''
# while a > 0:
#     b = str(a%2) + b
#     a = a // 2
#
# print(f"Десятичное преставление числа: {b}")


# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# print("Введите натуральное число:")
# a = int(input())
#
# list = []
# list.append(0)
# list.append(1)
# i = 1
# while i < a:
#     n = list[i] + list[i-1]
#     list.append(n)
#     i += 1
# print(list)
#
# list2 = list.copy()
# list.remove(0)
# i = 0
# while i < a:
#     list[i] *= -1
#     i += 1
# i = 0
# j = -1
# while i < a/2 and j >= -a/2:
#     tmp = list[i]
#     list[i] = list[j]
#     list[j] = tmp
#     i += 1
#     j -= 1
# list.extend(list2)
# print(list)





