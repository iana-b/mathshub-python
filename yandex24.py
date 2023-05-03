# flag = False
# for i in range(26):
#     for j in range(26):
#         text = f"{chr(ord('a') + i)}{chr(ord('a') + j)}"
#         if text == "ya":
#             print(text)
#             flag = True
#             break
#         print(text)
#     if flag:
#         break

# while (text := input("Введите строку (СТОП для остановки): ")) != "СТОП":
#     if text == "ignore_else":
#         break
# else:
#     print("Цикл завершён")

# A - Таблица умножения
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(i * j, end=' ')
#     print(end='\n')

# B - Не таблица умножения
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(f'{j} * {i} = {i * j}')

# C - Новогоднее настроение
# первый способ
# n = int(input())
# r = 1
# c = 0
# for i in range(1, n + 1):
#     print(i, end=' ')
#     c += 1
#     if c == r:
#         print()
#         c = 0
#         r += 1

# второй способ
# n = int(input())
# r = 1
# i = 1
# while i <= n:
#     for j in range(r):
#         print(i) if j == r - 1 else print(i, end=' ')
#         i += 1
#         if i > n:
#             break
#     r += 1

# третий способ
# n = int(input())
# i = 1
# r = 1
# while i <= n:
#     lst = []
#     for j in range(r):
#         lst.append(str(i))
#         i += 1
#         if i > n:
#             break
#     print(' '.join(lst))
#     r += 1

