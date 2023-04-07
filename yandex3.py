# A - Раз, два, три! Елочка, гори!
# scream = input()
# while scream != 'Три!':
#     print("Режим ожидания...")
#     scream = input()
# else:
#     print("Ёлочка, гори!")

# с помощью моржового оператора
# while (scream := input()) != "Три!":
#     print("Режим ожидания...")
# print("Ёлочка, гори!")

# B - Зайка - 3
# count = 0
# while (text := input()) != "Приехали!":
#     if 'зайка' in text:
#         count += 1
# print(count)

# C - Считалочка
# a = int(input())
# b = int(input())
# for i in range(a, b + 1):
#     print(i, end=" ")

# D - Считалочка 2.0
# a = int(input())
# b = int(input())
# if a <= b:
#     for i in range(a, b + 1):
#         print(i, end=" ")
# elif a > b:
#     for i in range(a, b - 1, - 1):
#         print(i, end=" ")

# E - Внимание! Акция!
# summa = 0
# while (price := float(input())) != 0:
#     if price >= 500:
#         price = price * 0.9
#         summa += price
#     else:
#         summa += price
# print(summa)

# F - НОД
# a = int(input())
# b = int(input())
#
# while a != 0 and b != 0:
#     if a > b:
#         a = a % b
#     else:
#         b = b % a
#
# print(a + b)

# G - НОК
# a = int(input())
# b = int(input())
# c = a * b
# while a != 0 and b != 0:
#     if a > b:
#         a = a % b
#     else:
#         b = b % a
#
# print(int(c / (a + b)))

# H - Излишняя автоматизация 2.0
# a = input()
# N = int(input())
# for i in range(1, N + 1):
#     print(a)

# I - Факториал
# n = int(input())
# f = 1
# for i in range(2, n + 1):
#     f = f * i
# print(f)

# J - Маршрут построен
# x = 0
# y = 0
# while (instruction := input()) != "СТОП":
#     steps = int(input())
#     if instruction == "СЕВЕР":
#         y += steps
#     if instruction == "ЮГ":
#         y -= steps
#     if instruction == "ВОСТОК":
#         x += steps
#     if instruction == "ЗАПАД":
#         x -= steps
# print(y, x, sep="\n")

# способ с match:
# x = 0
# y = 0
# while (instruction := input()) != "СТОП":
#     steps = int(input())
#     match instruction:
#         case "СЕВЕР":
#             y += steps
#         case "ЮГ":
#             y -= steps
#         case "ВОСТОК":
#             x += steps
#         case "ЗАПАД":
#             x -= steps
# print(y, x, sep="\n")

# K - Цифровая сумма
# n = input()
# summa = 0
# for i in n:
#     summa += int(i)
# print(summa)

# L - Сильная цифра
# n = input()
# maximum = 0
# for i in n:
#     if int(i) > maximum:
#         maximum = int(i)
# print(maximum)

# M - Первому игроку приготовиться 2.0
# N = int(input())
# name1 = "Яяяяяя"
# for i in range(1, N + 1):
#     name = input()
#     if name < name1:
#         name1 = name
# print(name1)

# N = int(input())
# name1 = input()
# for i in range(2, N + 1):
#     name = input()
#     if name < name1:
#         name1 = name
# print(name1)

# N = int(input())
# minimal = ""
# for i in range(0, N):
#     name = input()
#     if name < minimal or minimal == "":
#         minimal = name
# print(minimal)

# N - Простая задача
# n = int(input())
# sqrt = n ** (1 / 2)
# N = int(sqrt)
# count = 0
# if n == 1:
#     count += 1
# for i in range(2, N + 1):
#     if n % i == 0:
#         count += 1
# if count > 0:
#     print("NO")
# else:
#     print("YES")

# O - Зайка - 4
# N = int(input())
# count = 0
# for i in range(1, N + 1):
#     text = input()
#     if 'зайка' in text:
#         count += 1
# print(count)

# P - А роза упала на лапу Азора 2.0
# n = input()
# m = n[::-1]
# if n == m:
#     print("YES")
# else:
#     print("NO")

# n = input()
# answer = "NO"
# for i in range(0, len(n)):
#     if n[i] == n[len(n) - 1 - i]:
#         answer = "YES"
#     else:
#         answer = "NO"
#         break
# print(answer)

# n = input()
# answer = "YES"
# for i in range(0, len(n)):
#     if n[i] != n[len(n) - 1 - i]:
#         answer = "NO"
#         break
# print(answer)

# n = input()
# firstIndex = 0
# lastIndex = len(n) - 1
# halfIndex = round(len(n) / 2)
# answer = "YES"
# for i in range(0, halfIndex):
#     if n[firstIndex + i] != n[lastIndex - i]:
#         answer = "NO"
#         break
# print(answer)

# Q - Чётная чистота
# n = input()
# answer = ""
# for i in n:
#     if int(i) % 2 != 0:
#         answer += i
# print(answer)

# R - Простая задача 2.0
# n = int(input())
# N = int(n ** (1 / 2))
# answer = ""
# for i in range(2, N):
#     while n % i == 0:
#         n = n / i
#         answer += str(f"{i} * ")
# print(answer)

# n = int(input())
# for i in range(2, n + 1):
#     while n % i == 0:
#         n /= i
#         print(i, end=" ")
#         if n != 1:
#             print("*", end=" ")

# n = int(input())
# i = 2
# while n != 1:
#     if n % i == 0:
#         n /= i
#         print(i, end=" ")
#         if n != 1:
#             print("*", end=" ")
#     else:
#         i += 1

# n = int(input())
# for i in range(2, n + 1):
#     while n % i == 0:
#         n /= i
#         print(i, end=" ")
#         if n != 1:
#             print("*", end=" ")
#     if n == 1:
#         break

# S - Игра в "Угадайку"
# max_n = 1000
# min_n = 1
# count = 0
#
# while count < 10:
#     count += 1
#     n = (max_n + min_n) // 2
#     print(n)
#     answer = input()
#     if answer == "Меньше":
#         max_n = n - 1
#     elif answer == "Больше":
#         min_n = n + 1
#     elif answer == "Угадал!":
#         break

# T - Хайпанем немножечко!
# решение с break
# N = int(input())
# h = 0
# answer = -1
#
# for n in range(N):
#     b = int(input())
#     m = b // (256 ** 2)
#     r = b % (256 ** 2) // 256
#     h = (37 * (m + r + h)) % 256
#     hb = b - r * 256 - m * 256 ** 2
#
#     if h >= 100 or h != hb:
#         answer = n
#         break
#
# print(answer)

# решение с count
# N = int(input())
# h = 0
# answer = -1
# count = 0
#
# for n in range(N):
#     b = int(input())
#     m = b // (256 ** 2)
#     r = b % (256 ** 2) // 256
#     h = (37 * (m + r + h)) % 256
#     hb = b - r * 256 - m * 256 ** 2
#
#     if h >= 100 or h != hb:
#         if count == 0:
#             answer = n
#             count += 1
#
# print(answer)

# решение с answer
# N = int(input())
# h = 0
# answer = -1
#
# for n in range(N):
#     b = int(input())
#     m = b // (256 ** 2)
#     r = b % (256 ** 2) // 256
#     h = (37 * (m + r + h)) % 256
#     hb = b - r * 256 - m * 256 ** 2
#
#     if h >= 100 or h != hb:
#         if answer == -1:
#             answer = n
#
# print(answer)



# min_num = 1
# max_num = 1000
# guess = (max_num - min_num) // 2 + min_num
# print(guess)
#
# for i in range(1, 11):
#     feedback = input()
#     if feedback == 'Угадал!':
#         break
#     elif feedback == 'Меньше':
#         max_num = guess - 1
#         guess = (max_num - min_num) // 2 + min_num
#         print(guess)
#     elif feedback == 'Больше':
#         min_num = guess + 1
#         guess = (max_num - min_num) // 2 + min_num
#         print(guess)

# min_num = 1
# max_num = 1000
# guess = max_num / 2
# print(int(guess))
#
# for i in range(1, 11):
#     feedback = input()
#     if feedback == 'Угадал!':
#         break
#     elif feedback == 'Меньше':
#         max_num = guess - 1
#         guess = (max_num + min_num) / 2
#         print(int(guess))
#     elif feedback == 'Больше':
#         min_num = guess + 1
#         guess = (max_num + min_num) / 2
#         print(int(guess))
