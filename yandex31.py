# text = input()
# for i, letter in enumerate(text):
#     print(f"{i}. {letter}")
#
# help(enumerate)

# print(print("Эту строку выведет функция до возврата значения."))

# text = "Привет, мир!"
# print(text[8:11])
# print(text[:6])
# print(text[8:])
# print(text[:])
# print(text[::2])

# s = 'fjfjfjfjfaBBBAAA BBBA'
# new_s = s.rstrip('AB')
# print(new_s)

# one = (1,)
# print(type(one))

# text = "Привет, мир!"
# list_symbols = list(text)
# tuple_symbols = tuple(text)
# text_from_list = str(list_symbols)
# print(list_symbols)
# print(tuple_symbols)
# print(text_from_list)

# 3.1. Строки, кортежи, списки

# A - Азбука
# N = int(input())
# count = 0
# for i in range(N):
#     word = input()
#     if (word[0] == 'а') or (word[0] == 'б') or (word[0] == 'в'):
#         count += 1
# if count == N:
#     print('YES')
# else:
#     print('NO')

# как бы сделал я
# N = int(input())
# answer = "YES"
# for i in range(N):
#     word = input()
#     if word[0] not in 'абв':
#         answer = "NO"
# print(answer)

# B - Кручу-верчу
# text = input()
# for n in text:
#     print(n)

# C - Анонс новости
# первый способ
# L = int(input())
# N = int(input())
# new_text = ()
# for n in range(N):
#     text = input()
#     if len(text) > L:
#         new_text = text[:(L - 3)] + str('...')
#     else:
#         new_text = text
#     print(new_text)

# второй способ
# L = int(input())
# N = int(input())
# new_text = ()
# lst = []
# for n in range(N):
#     text = input()
#     if len(text) > L:
#         new_text = text[:(L - 3)] + str('...')
#     else:
#         new_text = text
#     lst.append(new_text)
# for n in lst:
#     print(n)


