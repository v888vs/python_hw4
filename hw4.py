# Вычислить число c заданной точностью d
#
# Пример:
#
# - при $d = 0.001, π = 3.141.$
# $10^{-1} ≤ d ≤10^{-10}$

#import math

# n1 = int(input('Введите число: '))
# n2 = 10 ** (-n1)
# n3 = int(input('Введите число: '))
# x1 = 1
# x2 = 1
# print(n2)
# while x2 > n2:
#     x2 = round((1 / math.factorial(x1)), n1)
#     n3 = n3 + x2
#     x1 += 1
# print(round(n3, n1))

# from decimal import Decimal, getcontext
#
# n1 = int(input('Введите точность: '))
# n2 = (input('Введите число: '))
# n3 = int(input('Введите делитель: '))
# getcontext().prec = n1
# print(Decimal(n2) / n3)


# Задайте натуральное число N.
# Напишите программу, которая
# составит список простых множителей числа N.

# def mn():
#     num = int(input("Введите число: "))
#     l1 = []
#     if num >= 2:
#         for i in range(2, num + 1):
#             while i <= num:
#                 if num % i == 0:
#                     num = num / i
#                     l1.append(i)
#                 else:
#                     i +=1
#         print('Список простых множителей:  ', l1)
#     else:
#         print('Введите другое число ')
#
# mn()
#
# while True:
#     start = input('Запустить программу ещё раз ? (Y/N) : ')
#     if start == 'Y' or start == 'y':
#         mn()
#     elif start == 'N' or start == 'n':
#         print("Всего хорошего !")
#         break

# Задайте последовательность чисел.
# Напишите программу, которая выведет
# список неповторяющихся элементов
# исходной последовательности.

# def list_nonrec_number():
#     l1 = list(map(int, input('Введите числа через пробел: ').split()))
#     l2 = []
#     print('Список введёных элементов: ', l1)
#     [l2.append(i) for i in l1 if i not in l2]
#     print('Список из неповторяющихся элементов: ', l2)
#
# list_nonrec_number()
#
# while True:
#     start = input('Запустить программу ещё раз ? (Y/N) : ')
#     if start == 'Y' or start == 'y':
#         list_nonrec_number()
#     elif start == 'N' or start == 'n':
#         print("Всего хорошего !")
#         break

# Задана натуральная степень k.
# Сформировать случайным образом
# список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
#
# Пример:
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# import random
# import sys
#
# def create_mn(k):
#  l = random.randint(0, k - 1)
#  rand_list_k = [random.randint(-sys.maxsize, sys.maxsize) for i in range(l, k + 1)]
#  return rand_list_k
#
# def create_str(revers_r_l_k):
#  rand_list_k = revers_r_l_k[::-1]
#  str_mn = ''
#  if len(rand_list_k) <= 1:
#   str_mn = 'x = 0'
#  else:
#   for i in range(len(rand_list_k)):
#    if i != len(rand_list_k) - 1 and rand_list_k[i] != 0 and i != len(rand_list_k) - 2:
#     str_mn += f'{rand_list_k[i]}x^{len(rand_list_k) - i - 1}'
#     if rand_list_k[i + 1] != 0:
#      str_mn += ' + '
#    elif i == len(rand_list_k) - 2 and rand_list_k[i] != 0:
#     str_mn += f'{rand_list_k[i]}x'
#     if rand_list_k[i + 1] != 0:
#      str_mn += ' + '
#    elif i == len(rand_list_k) - 1 and rand_list_k[i] != 0:
#     str_mn += f'{rand_list_k[i]} = 0'
#    elif i == len(rand_list_k) - 1 and rand_list_k[i] == 0:
#     str_mn += ' = 0'
#  return str_mn
#
# def create_str2(revers_r_l_k):
#  rand_list_k = revers_r_l_k[::-1]
#  str_mn = ''
#  if len(rand_list_k) <= 1:
#   str_mn = 'x = 0'
#  else:
#   for i in range(len(rand_list_k)):
#    if i != len(rand_list_k) - 1 and rand_list_k[i] != 0 and i != len(rand_list_k) - 2:
#     str_mn += f'{rand_list_k[i]}x^{len(rand_list_k) - i - 1}'
#     if rand_list_k[i + 1] != 0:
#      str_mn += ' + '
#    elif i == len(rand_list_k) - 1 and rand_list_k[i] != 0:
#     str_mn += f'{rand_list_k[i]} = 0'
#    elif i == len(rand_list_k) - 1 and rand_list_k[i] == 0:
#     str_mn += ' = 0'
#  return str_mn
#
# func_names = [create_str, create_str2]
#
# def mn_rand():
#  k = int(input("Введите натуральную степень k = "))
#  rand_mn_k = create_mn(k)
#  d1 = random.choice(func_names)
#  with open('file1.txt', 'w+') as data:
#   data.write(d1(rand_mn_k))
#
# mn_rand()
#
# while True:
#     start = input('Запустить программу ещё раз ? (Y/N) : ')
#     if start == 'Y' or start == 'y':
#         mn_rand()
#     elif start == 'N' or start == 'n':
#         print("Всего хорошего !")
#         break