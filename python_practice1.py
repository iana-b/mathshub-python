# Блок 1

# Задача 0 - Пользовательская информация
# name = input("Введите имя: ")
# year = input("Введите год рождения: ")
# print(f"Приветствуем тебя\n{name}\n{year} года рождения")

# Задача 1 - Поделить торт
# cake_weight = float(input("Сколько весит ваш торт?"))
# guests = int(input("Сколько у вас гостей?"))
# cake_portion = cake_weight / guests
# print(f"Каждый гость получит по {cake_portion:.2f}")

# Задача 2 - Стоимость обедов
# a = 100
# b = 99
# how_much = int(input())
# result_a = how_much * a + (how_much * b) // 100
# result_b = (how_much * b) % 100
# print(f"Итого {result_a} рублей {result_b} копеек")

# Задача 3 - Предыдущее и следующее
# number = int(input())
# print(f"предыдущее = {number - 1}\nследующее = {number + 1}")

# Задача 4 - Следующее нечетное число
# number = int(input())
# next_number = number % 2 + number + 1
# print(f"Нечетное число: {next_number}")

# Задача 5 - Расчет суммы и произведения чисел
# number = input()
# summa = int(number[0]) + int(number[1]) + int(number[2])
# proizvedenie = int(number[0]) * int(number[1]) * int(number[2])
# print(f"сумма = {summa}\nпроизведение = {proizvedenie}")

# второй способ:
# number = int(input())
# n1 = number // 100
# n2 = number % 10
# n3 = number // 10 % 10
# print(f"сумма = {n1 + n2 + n3}\nпроизведение = {n1 * n2 * n3}")

# Блок 2

# Задача 0 - Минимум из 2 чисел
# a = int(input())
# b = int(input())
# if a <= b:
#     min_ab = a
# else:
#     min_ab = b
# print(f"min={min_ab}")

# Задача 1 - Опросник
# answer = int(input("Чему равно 2 в степени 3 ? "))
# if answer == 8:
#     print("Молодец!")
# else:
#     print("Ответ неверный")
# print("Удачи!")

# Задача 2 - Рассчитать сдачу
# price = int(input())
# money = int(input())
# if money < price:
#     print("недостаточно средств")
# else:
#     change = money - price
#     print(float(change))

# Задача 3 - Скидка на копеечку
# price = float(input())
# money = float(input())
# if money < price:
#     print("недостаточно средств")
# else:
#     change = money - price
#     if change % 1 != 0:
#         print(f"Сдача = {int(change) + 1}")
#     else:
#         print(f"Сдача = {change}")

# второй способ:
# price = float(input())
# money = float(input())
#
# result = money - price
# if result < 0:
#     print("Недостаточно средств")
# elif int(result) != result:
#     print(f"Сдача = {result} + 1")
# else:
#     print(f"Сдача = {result}")

# Задача 4 - Високосный год
# year = int(input())
# if year % 400 == 0:
#     print("високосный")
# else:
#     if year % 100 == 0:
#         print("невисокосный")
#     else:
#         if year % 4 == 0:
#             print("високосный")
#         else:
#             print("невисокосный")
# второй способ:
# year = int(input())
# if (year % 400 == 0) or ((year % 100 != 0) & (year % 4 == 0)):
#     print("високосный")
# else:
#     print("невисокосный")

# Задача 6 - Округление
# candies = int(input())
# each = round(candies / 3)
# if candies % 3 == 0:
#     print(f"{each} " * 3)
# else:
#     print(each, each, candies - 2 * each)

# второй способ записи:
# total = int(input())
# if total % 3 != 0:
#     first = round(total / 3)
#     second = round(total / 3)
#     third = total - first - second
# else:
#     first = second = third = int(total / 3)
# print(first, second, third)

# Задача 7 - Минимальное из трех
# a = int(input())
# b = int(input())
# c = int(input())
# min_abc = a
# if b < min_abc:
#     min_abc = b
# if c < min_abc:
#     min_abc = c
# print(f"min = {min_abc}")

# Задача 8 - Одна программа двумя способами
# с помощью if
# a = input()
# if a == "":
#     print("Ничего не получено")
# else:
#     print(a)
# с помощью or
# a = input()
# print(a or "Ничего не получено")

# Задача 9 - Сортировка
# a = int(input())
# b = int(input())
# c = int(input())
# min_abc = min(a, b, c)
# max_abc = max(a, b, c)
# mid_abc = a + b + c - min_abc - max_abc
# print(min_abc, mid_abc, max_abc)

# второй способ:
# min1 = float(input())
# min2 = float(input())
# min3 = float(input())
#
# if min1 > min2:
#     min1, min2 = min2, min1
# if min2 > min3:
#     min2, min3 = min3, min2
# if min1 > min2:
#     min1, min2 = min2, min1
#
# print(min1, min2, min3)

# Задача Дополнительная
# a = int(input())
# b = int(input())
# # print(b and a / b)

# Блок 3

# Задача 0
# replica = input()
# replica_lower = replica.lower()         # приведение к нижнему регистру
# hi = replica_lower.find("привет")       # поиск слова
# how = replica_lower.find("как дела")
# weather = replica_lower.find("какая погода")
# if hi != -1:
#     print("Здравствуйте!")
# if how != -1:
#     print("Отлично!")
# if weather != -1:
#     print("Солнечно!")

# Задача 1
# a = input()
# if len(a) == 1:
#     n = ord(a)
#     if (n >= ord("А")) and (n <= ord("я")):
#         print(chr(n + 1))
#     else:
#         print("Вы ввели символ")
# else:
#     print("Ошибка")

# второй способ
# предположим, что посторонние символы - все, что находятся за пределами букв русского и английского алфавитов
# char = input()
# if len(char) != 1:
#     print("некорректное кол-во символов")
# else:
#     char_num = ord(char)
#     if ((char_num >= ord("а")) and (char_num <= ord("я"))) | ((char_num >= ord("a")) and (char_num <= ord("z"))):
#         print(f"следующая буква {chr(char_num + 1)}")       # символ |, а не or
#     else:
#         print("введен неверный символ")
