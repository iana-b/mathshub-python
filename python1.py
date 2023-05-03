# a = 101 % 10
# b = 98 // 12
# c = 27 ** (1/3)
# d = a + b + c
# e = d ** -1
# print(a, b, c, d, e)

# print(not False)
# print(True or False)
# print(True and False)
# print((1 < 0) and (9 <= 10))
# print((1 < 0) or (9 <= 10))
# print(10 == "10")
#
# a = int(1.222)
# print(type(a))
#
# b = ""
# print(type(b))
# print(type(b * (- 1)))
# print(type("" * (- 1)))
#

# a = str(1234/100)
# print(a)
# print(type(a))
#
# a = "f45rdsgF_ff"
# b = len(a)
# c = float(b)
# print(b, c)
#
# a = "123456789abc"
# b = len(a)
# c = bool(b)
# print(b, c)
#
# a1 = ""
# b1 = len(a1)
# c1 = bool(b1)
# print(b1, c1)
#
# a = 0
# b = bool(a)
# print(b)

# a = "ggg"
# print(a * -1)
#
# all good
#
# 23 МАРТА
#
# print("<<привет".replace("<<", ""))
#
# for i in [1, 2, 3]:
#     print(i)
# print(i)
#
# несколько действий в теле цикла
# for i in [1, 2, 3]:
#     print("мы в теле цикла")
#     print(i)
#
# for i in range(0, 10):
#     print(i)
#
# for i in range(0, 10, 2):
#     print(i)
#
# for i in range(1, 10, 2):
#     print(i, end=" ")
#
# for i in range(5):
#     print(i, end=" ")
#
# for i in range(5):
#     print(i * 2)
#
# answer = input("сколько будет 2 + 2 = ")
# while int(answer) != 4:
#     answer = input("сколько будет 2 + 2 = ")
#
# answer = input("сколько будет 2 + 2 = ")
# while int(answer) != 4:
#     answer = input("сколько будет 2 + 2 = ")
# else:
#     print("Молодец!")
#
# i = 0
# while i < 10:
#     print(i)
#     i += 1
#
# while True:
#     answer = input("Введите сколько будет 2 + 2 = ")
#     print(answer)
#
# while True:
#     answer = input("Введите сколько будет 2 + 2 = ")
#     if int(answer) == 4:
#         print("молодец")
#         break
#
# for number in range(10):
#     if number == 5:
#         continue
#     print(number)
#
# count = 0
# while count < 3:
#     answer = input("Введите сколько будет 2 + 2 = ")
#     count += 1
#     if int(answer) == 4:
#         print("молодец")
#         break
#
# a = int(input())
# b = int(input())
# if b == 0:
#     print("Ошибка деления на 0")
# else:
#     print(a/b)
#
# a = int(input())
# b = int(input())
# if b == 0:
#     print("Ошибка деления на 0")
#     b = 1
# print(a/b)
#
# a, b = 1, 0
# try:
#     print(t / b)
# except Exception:
#     print("Что-то пошло не так")
#
# a, b = 1, 0
# try:
#     print(a / b)
# except ZeroDivisionError:
#     print("Что-то пошло не так")
#
# a = 1
# b = 0
# try:
#     print(1 + 1)
# except ZeroDivisionError:
#     print('Деление на ноль')
# except NameError:
#     print('Нет такой переменной')
# except Exception:
#     print('Что-то, чего мы не ожидали')
# except TypeError:
#     print('ошибка типов')
#
# a, b = 100, 1
# try:
#     result = int(a) / int(b)
# except (ValueError, ZeroDivisionError):
#     print('Что-то пошло не так')
# else:
#     print('Результат в квадрате:', result ** 2)
#
# a, b = 100, 0
# try:
#     result = int(a) / int(b)
# except (ValueError, ZeroDivisionError):
#     print('Что-то пошло не так')
# else:
#     print('Результат в квадрате:', result ** 2)
# finally:
#     print('наконец-то все закончилось')
#
# raise NameError('просто захотелось выбросить ошибку')
#
# raise
#
# try:
#     10 / 0
# except Exception as e:
#     raise
