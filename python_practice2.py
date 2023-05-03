# Задача 0
# a = int(input("a= "))
# b = int(input("b= "))
# for i in range(a, b + 1):
#     print(i)

# Задача 1
# b = int(input("Введите число b "))
# for i in range(1, b):
#     print(f"квадратный корень числа {i} = {(i ** (1/2)):.2f}")

# Задача 2
# N = int(input("Введите число N "))
# for i in range(3, 3 * (N + 1), 3):
#     print(i, end=" ")

# Задача 3
# N = int(input("N = "))
# summa = 0
# for i in range(1, N + 1):
#     summa += i
# print(f"сумма чисел от 1 до {N} = {summa}")

# Задача 4
# a = None
# summa = 0
# while a != 0:
#     a = int(input("Введите число, которое хотите просуммировать "))
#     summa += a
# else:
#     print(f"сумма введенных чисел = {summa}")

# Задача 5
# initial_money = int(input("введите начальную сумму "))
# interest_rate = int(input("введите процентную ставку от 1 до 100 "))
# target_money = int(input("введите сколько хотите получить в итоге "))
# years = 0
# money = initial_money
#
# while money < target_money:
#     money += money * (interest_rate / 100)
#     years += 1
# print(f"через количество лет {years} у вас на счету будет {money}")

# Блок 2

# Задача 0
# a = int(input())
# i = 2
# while a % i != 0:
#     i += 1
#
# print(i)

# Задача 1 - Максимум чисел
# maximum = 0
# for i in range(1, 11):
#     b = float(input("Введите число "))
#     if b > maximum:
#         maximum = b
#
# print(f"max = {maximum}")

# Задача 2 - Числа с заданной цифрой
# a = input("цифра ")
# for i in range(0, 100):
#     if str(i).find(a) != -1:
#         print(i)

# Задача 3 - Число наоборот
# a = input("Введите число ")

# метод интенсив
# print(f"число наоборот {a[::-1]}")

# метод суммы
# reversed_a = ""
# for i in a:
#     reversed_a = i + reversed_a
# print(reversed_a)

# метод отрицательных индексов
# for i in range(1, len(a)+1):
#     print(a[-i], end="")

# метод индексов
# for i in range(0, len(a)):
#     print(a[len(a) - 1 - i], end="")


# Задача 4 - Лесенка
# n = int(input("Введите цифру "))
# answer = ""
# for i in range(1, n + 1):
#     answer += str(i)
#     print(answer)

# # Задача 5 - Угадать число
# import random
# n = int(input())
# count = 0
# min_a = 0
# max_a = 100
# while count < 5:
#     count += 1
#     a = random.randint(min_a, max_a)
#     print(f"попытка {count}, ваше число {a}?")
#     answer = input()
#     if answer == 'больше':
#         min_a = a
#     elif answer == 'меньше':
#         max_a = a
#     else:
#         print("ура!")
#         break

# Задача 6 - Модификация угадайки
# import random
# n = int(input())
# count = 0
# min_a = 0
# max_a = 100
# while count < 5:
#     count += 1
#     a = random.randint(min_a, max_a)
#     print(f"попытка {count}, ваше число {a}?")
#     answer = input()
#     if answer == 'больше':
#         min_a = a
#     elif answer == 'меньше':
#         max_a = a
#     else:
#         print("ура!")
#         break
# if n != a:
#   print("Число не удалось угадать!")

# Задача 7 - Тестирование (повышенной сложности)
# import random
# a = random.randint(0, 999)
# b = random.randint(0, 999)
# answer = input(f"сколько будет {a} + {b} = ? ")
# while answer != "конец":
#     if int(answer) == (a + b):
#         a = random.randint(0, 999)
#         b = random.randint(0, 999)
#         answer = input(f"сколько будет {a} + {b} = ? ")
#     elif int(answer) != (a + b):
#         print("Ответ неверный")
#         answer = input(f"сколько будет {a} + {b} = ? ")
# print("Приходите еще !")

# Блок 3

# Задача 0 - Ошибка типа данных / значения
# a = input()
# b = input()
# try:
#     print(int(a) + int(b))
# except ValueError:
#     print(a + b)

# Задача 1 - Ошибка типа данных
# answer = "да"
# while answer == "да":
#     time = input("Введите ваше время ")
#     try:
#         if int(time) < 0:
#             raise Exception("Время не может быть отрицательным")
#         print(f"Ваша скорость = {60 / int(time)} км/ч")
#     except ValueError:
#         print("Введите корректное значение времени")
#     except ZeroDivisionError:
#         print("Время не может быть равным нулю!")
#     except Exception as e:
#         print(e)
#     answer = input("Хотите рассчитать скорость еще раз? ")
# print("До свидания")
