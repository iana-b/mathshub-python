# 2.2 Условный оператор
# A - Просто здравствуй, просто как дела
# name = input()
# answer = input()
# print("Как Вас зовут?")
# print(f"Здравствуйте, {name}!")
# print("Как дела?")
# if answer == "хорошо":
#     print("Я за вас рада!")
# elif answer == "плохо":
#     print("Всё наладится!")

# B - Кто быстрее?
# speed_p = int(input())
# speed_v = int(input())
# distance = 43872
# if distance / speed_p < distance / speed_v:
#     print("Петя")
# else:
#     print("Вася")

# C - Кто быстрее на этот раз?
# speed_p = int(input())
# speed_v = int(input())
# speed_t = int(input())
# if max(speed_v, speed_t, speed_p) == speed_p:
#     print("Петя")
# elif max(speed_v, speed_t, speed_p) == speed_v:
#     print("Вася")
# else:
#     print("Толя")

# D - Список победителей
# speed_p = int(input())
# speed_v = int(input())
# speed_t = int(input())
# max_speed = max(speed_t, speed_p, speed_v)
# min_speed = min(speed_t, speed_p, speed_v)
# if max_speed == speed_p:
#     print("1. Петя")
# elif max_speed == speed_v:
#     print("1. Вася")
# else:
#     print("1. Толя")
# if max_speed != speed_p != min_speed:
#     print("2. Петя")
# elif max_speed != speed_v != min_speed:
#     print("2. Вася")
# else:
#     print("2. Толя")
# if min_speed == speed_p:
#     print("3. Петя")
# elif min_speed == speed_v:
#     print("3. Вася")
# else:
#     print("3. Толя")

# E - Яблоки
# N = int(input())
# M = int(input())
# petya = 7 - 3 + 2 + N
# vasya = 6 + 3 + 5 - 2 + M
# if petya > vasya:
#     print("Петя")
# else:
#     print("Вася")

# F - Сила прокрастинации
# year = int(input())
# if year % 400 == 0:
#     print("YES")
# else:
#     if year % 100 == 0:
#         print("NO")
#     else:
#         if year % 4 == 0:
#             print("YES")
#         else:
#             print("NO")

# G - А роза упала на лапу Азора
# number = input()
# if number[0] == number[3] and number[1] == number[2]:
#     print("YES")
# else:
#     print("NO")

# H - Зайка - 1
# what_i_see = input()
# if "зайка" in what_i_see:
#     print("YES")
# else:
#     print("NO")

# I - Первому игроку приготовиться
# name_1 = input()
# name_2 = input()
# name_3 = input()
# if name_1 < name_2 and name_1 < name_3:
#     print(name_1)
# elif name_2 < name_1 and name_2 < name_3:
#     print(name_2)
# else:
#     print(name_3)

# другой способ
# minimum = name_1
# if name_2 < minimum:
#     minimum = name_2
# if name_3 < minimum:
#     minimum = name_3
# print(minimum)

# J - Лучшая защита - шифрование
# password = input()
# part1 = int(password[2]) + int(password[1])
# part2 = int(password[0]) + int(password[1])
# if part1 < part2:
#     print(str(part2) + str(part1))
#     # print(f"{part2}{part1}")
#     # f"{part1}"
#     # str(part1)
# else:
#     print(str(part1) + str(part2))

# K - Красота спасет мир
# первый способ:
# number = input()
# minimum = min(number)
# maximum = max(number)
# middle = 0
# if number[0] != minimum and number[0] != maximum:
#     middle = number[0]
# elif number[1] != minimum and number[1] != maximum:
#     middle = number[1]
# elif number[2] != minimum and number[2] != maximum:
#     middle = number[2]
# if int(minimum) + int(maximum) == int(middle) * 2:
#     print("YES")
# else:
#     print("NO")
# второй способ:
# number = input()
# minimum = min(number)
# maximum = max(number)
# summa = int(number[0]) + int(number[1]) + int(number[2])
# middle = summa - int(minimum) - int(maximum)
# if int(minimum) + int(maximum) == middle * 2:
#     print("YES")
# else:
#     print("NO")

# L - Музыкальный инструмент
# a = int(input())
# b = int(input())
# c = int(input())
# if a < (b + c) and b < (a + c) and c < (a + b):
#     print("YES")
# else:
#     print("NO")

# M - Властелин чисел: Братство общей цифры
# a = input()
# b = input()
# c = input()
# if a[0] == b[0] == c[0]:
#     print(a[0])
# elif a[1] == b[1] == c[1]:
#     print(a[1])

# N - Властелин чисел: Две башни
# number = input()
# minimum = min(number)
# maximum = max(number)
# middle = int(number[0]) + int(number[1]) + int(number[2]) - int(minimum) - int(maximum)
# if minimum == str(0):
#     print(f"{middle}{minimum} {maximum}{middle}")
# else:
#     print(f"{minimum}{middle} {maximum}{middle}")

# O - Властелин чисел: Возвращение Цезаря
# number_1 = int(input())
# number_2 = int(input())
# a = number_1 // 10
# b = number_1 % 10
# c = number_2 // 10
# d = number_2 % 10
# maximum = max(a, b, c, d)
# minimum = min(a, b, c, d)
# summa = a + b + c + d
# middle = (summa - minimum - maximum) % 10
# print(f"{maximum}{middle}{minimum}")

# P - Легенды велогонок возвращаются: кто быстрее?
# p = int(input())
# v = int(input())
# t = int(input())
# first = max(p, v, t)
# second = 0
# third = min(p, v, t)
# if p != first and p != third:
#     second = "Петя"
# elif v != first and v != third:
#     second = "Вася"
# elif t != first and t != third:
#     second = "Толя"
# if p == first:
#     first = "Петя"
# elif v == first:
#     first = "Вася"
# elif t == first:
#     first = "Толя"
# if p == third:
#     third = "Петя"
# elif v == third:
#     third = "Вася"
# elif t == third:
#     third = "Толя"
# print(f"{' ' * 10}{first}{' ' * 10}\n{' ' * 2}{second}{' ' * 18}\n{' ' * 18}{third}{' ' * 2}")
# print(f"{' ' * 3}II{' ' * 6}I{' ' * 6}III{' ' * 2}")

# Q - Корень зла
# a = float(input())
# b = float(input())
# c = float(input())
# D = b ** 2 - 4 * a * c
# minimum = 0
# maximum = 0
# if a == 0 and b == 0 and c == 0:
#     print("Infinite solutions")
# elif a == 0 and b == 0:
#     print("No solution")
# elif a == 0:
#     x1 = - c / b
#     print(f"{x1:.2f}")
# elif D > 0:
#     x1 = (- b - (D ** (1 / 2))) / (2 * a)
#     x2 = (- b + (D ** (1 / 2))) / (2 * a)
#     if x1 > x2:
#         print(f"{x2:.2f} {x1:.2f}")
#     else:
#         print(f"{x1:.2f} {x2:.2f}")
# elif D == 0:
#     x1 = x2 = - b / (2 * a)
#     print(f"{x1:.2f}")
# elif D < 0:
#     print("No solution")

# R - Территория зла
# a = int(input())
# b = int(input())
# c = int(input())
# maximum = max(a, b, c)
# minimum = min(a, b, c)
# middle = a + b + c - maximum - minimum
# if maximum ** 2 == minimum ** 2 + middle ** 2:
#     print("100%")
# if maximum ** 2 < minimum ** 2 + middle ** 2:
#     print("крайне мала")
# if maximum ** 2 > minimum ** 2 + middle ** 2:
#     print("велика")

# S - Автоматизация безопасности
# x = float(input())
# y = float(input())
# r = 10
# if x ** 2 + y ** 2 > r ** 2:
#     print("Вы вышли в море и рискуете быть съеденным акулой!")
# elif x > 0 and y > 0 and x ** 2 + y ** 2 < 25:
#     print("Опасность! Покиньте зону как можно скорее!")
# # y = kx + b уравнение прямой
# # 0 = -7 * k + b
# # 5 = -4 * k + b
#
# # b = 35 / 3
# # k = 5 / 3
# # y = (5 / 3) * x + (35 / 3)
# elif x < 0 and (0 < y < 5) and y < ((5 / 3) * x + (35 / 3)):
#     print("Опасность! Покиньте зону как можно скорее!")
# elif y < 0 and (-7 < x < 5) and (y > ((1 / 4) * (x ** 2) + (x / 2) - (35 / 4))):
#     print("Опасность! Покиньте зону как можно скорее!")
# else:
#     print("Зона безопасна. Продолжайте работу.")

# T - Зайка - 2
# text1 = input()
# text2 = input()
# text3 = input()
# maximum = max(text1, text2, text3)
# answer = maximum
# if 'зайка' in text1:
#     answer = text1
# if 'зайка' in text2 and text2 < answer:
#     answer = text2
# if 'зайка' in text3 and text3 < answer:
#     answer = text3
# if len(answer) > 0:
#     print(answer, len(answer))
