# a = int(input())
# print("Купи слона!\n" * a)

# n = int(input())
# a = input()
# print(f"Я больше никогда не буду писать \"{a}\"!\n" * n)

# n = int(input())  # минут
# m = int(input())  # детей
# v = 2 / 2 / 2
# print(int(m * n * v))

# 10 task:
# name = input()
# number = input()
# print(f"Группа №{number[0]}.\n{number[2]}. {name}.\nШкафчик: {number}.\nКроватка:{number[1]}.")

# name = input()
# number = input()
# print(f"Группа №{number[0]}.\n{number[2]}. {name}.\nШкафчик: {number}.\nКроватка: {number[1]}.")

# abcd = input()
# print(abcd[1], abcd[0], abcd[3], abcd[2], sep="")
#
# a = int(input())
# b = int(input())
# a_1 = a % 10
# a_10 = a // 10 % 10
# a_100 = a // 100
# b_1 = b % 10
# b_10 = b // 10 % 10
# b_100 = b // 100
# c = (a_100 + b_100) % 10
# d = (a_10 + b_10) % 10
# e = (a_1 + b_1) % 10
# print(c, d, e, sep="")

# children = int(input())
# candy = int(input())
# print(candy // children, "\n", candy % children, sep="")

# red = int(input())
# green = int(input())
# blue = int(input())
# print(red + blue + 1)

# n = int(input())  # часов от 0 до 24
# m = int(input())  # минут от 0 до 60
# t = int(input())  # минут от 30 до 10**9
# # n = 10
# # m = 15
# # t = 2752
# hh = (n + (m + t) // 60) % 24
# mm = (m + t) % 60
# print(hh // 10, hh % 10, ":", mm // 10, mm % 10, sep="")

# 16
# A = int(input())
# B = int(input())
# C = int(input())
# time = (B - A) / C
# print(f"{time:.2f}")

# all_sum = int(input())
# last_sum = int(input(), 2)
# print(all_sum + last_sum)

# price = int(input(), 2)
# cash = int(input())
# print(int(cash - price))


# name = input()
# price = int(input())
# weight = int(input())
# money = int(input())
# # print((35 - len("Чек")) / 2)
# print("=" * 16 + "Чек" + "=" * 16)
# cost = weight * price
# change = money - cost
# a = len(f"Товар:{name}")
# print(a)
# b = len(f"Цена:{weight}кг * {price}руб/кг")
# c = len(f"Итого:{cost}руб")
# d = len(f"Внесено:{money}руб")
# e = len(f"Сдача:{change}руб")
# print("Товар:" + (" " * (35 - a)) + f"{name}")
# print("Цена:" + (" " * (35 - b)) + f"{weight}кг * {price}руб/кг")
# print("Итого:" + (" " * (35 - c)) + f"{cost}руб")
# print("Внесено:" + (" " * (35 - d)) + f"{money}руб")
# print("Сдача:" + (" " * (35 - e)) + f"{change}руб")
# print("=" * 35)

# N = int(input())
# M = int(input())
# K1 = int(input())
# K2 = int(input())
# # K2 < K1
# # M2, M1 - вес котлет - ?
# # M2 = N - M1
# # M1 * K1 + M2 * K2 = N * M
# # M1 * K1 + (N - M1) * K2 = N * M
# # M1 * (K1 - K2) + N * K2 = N * M
# M1 = (N * M - N * K2) / (K1 - K2)
# M2 = N - M1
# print(int(M1), int(M2))
