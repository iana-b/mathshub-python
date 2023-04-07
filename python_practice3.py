# Блок 1
# Задача 0 - Перевернуть список
# list1 = [1, 2, 3, 4, 5, 6, 7]
# list2 = [1, 2, 3, 4]
#
# lst = list1
# print(lst[len(lst) // 2:] + lst[:len(lst) // 2])
#
# print(list1[3:7] + list1[0:3])
# print(list1[3:] + list1[:3])
# print(list1[len(list1) // 2: len(list1) + 1] + list1[0:len(list1) // 2])
# print(list1[len(list1) // 2:] + list1[:len(list1) // 2])

# len1 = len(list1)
# len2 = len(list2)
# list1_new1 = list1[:(len1 // 2)]
# list1_new2 = list1[(len1 // 2):]
# print(list1_new2 + list1_new1)
#
# list2_new1 = list2[:(len2 // 2)]
# list2_new2 = list2[(len2 // 2):]
# print(list2_new2 + list2_new1)

# lst = list2

# list_new1 = list[:(len(list) // 2)]
# list_new2 = list[(len(list) // 2):]
# print(list_new2 + list_new1)

# print(lst[(len(lst) // 2):] + lst[:(len(lst) // 2)])

# Задача 1 - Сдвиг вправо
# list1 = [1, 2, 3, 4, 5, 6, 7]
# list_new = list1[:len(list1) - 1]
# print(list_new)
# list_last = list1[len(list1) - 1:]
# print(list_last)
# print(list_last + list_new)
#
# print(list1[-1:] + list1[:-1])

# Задача 2 - Отрабатываем операции над списками
# result = [1, 100, -100, 23, 13, 78, 89, 90, 100, 0]
#
# result = result[:len(result) // 2]          # первая половина элементов
# print(f"Результат: {result}")
#
# result = result + [0] * len(result)         # добавление нулей
# print(f"Результат: {result}")
#
# result[-2] = 100                            # предпоследний элемент 100
# print(f"Результат: {result}")
#
# print(f"Ответ = {sum(result)}")             # сумма элементов

# Задача 3 - Перестановка минимума и максимума
# result = [1, 100, -1000, 23, 13, 78, 89, 90, 12345, 12000]
# # maximum = max(result)
# # minimum = min(result)
# # index_max = result.index(maximum)
# # index_min = result.index(minimum)
#
# print(result)
# maximum = result[0]
# minimum = result[0]
# for i in result:
#     if i > maximum:
#         maximum = i
#     elif i < minimum:
#         minimum = i
# print(f"Минимум: {minimum}, максимум: {maximum}")
#
# index_max = result.index(maximum)
# index_min = result.index(minimum)
# print(f"Индекс минимума: {index_min}, Индекс максимума: {index_max}")
#
# result[index_min] = maximum
# result[index_max] = minimum
# print(result)

# Задача 4 - Соседи
# lst = [1, 2, 100, 99, 88, -1, 0, 0, 10]
#
# for i in range(0, len(lst)):
#     if lst[i] > lst[i - 1]:
#         print(lst[i])

# Задача 5 - Найти все вхождения числа в список
# s = input("Введите список чисел через пробел: ")
# count = s.count("1 ")
# print(f"Количество единиц равно {count}")

# s = input("Введите список чисел через пробел: ").split()
# count = s.count("1")
# print(f"Количество единиц равно {count}")

# s = "1 3 1 3 1 3 1 3 1 3 12 12"

# через цикл
# s = input("Введите список чисел через пробел: ").split()
# count = 0
# for i in range(0, len(s) - 1):
#     if s[i] == "1":
#         count += 1
# print(f"Количество единиц равно {count}")

# s = input("Введите список чисел через пробел: ").split()
# count = 0
# for i in s:
#     if i == "1":
#         count += 1
# print(f"Количество единиц равно {count}")

# Задача 6 - Больше всех своих соседей (Дополнительная!)
# lst = input("Введите список чисел через пробел: ").split()
# count = 0
# answer = []
#
# for i in range(1, (len(lst) - 2)):
#     if (int(lst[i]) > int(lst[i - 1])) and (int(lst[i]) > int(lst[i + 1])):
#         count += 1
#         answer += [lst[i]]
#
# print(f"Список чисел: {' '.join(answer)}. Общее количество = {count}")

# Задача 7 - Проредить массив (Дополнительная!)
# 1 0 1 0 2 0 3 0 0 4 0 0 0
# s = input("Введите список чисел через пробел: ")
# lst = s.split()
# for n in lst:
#     if n == "0":
#         lst.remove(n)
#         lst.append(n)
# lst_new = []
# for i in range(len(lst)):
#     lst_new.append(int(lst[i]))
#
# print(f"result = {lst_new}")

# второй способ
# s = input("Введите список чисел через пробел: ").split()
# a = []
# b = []
# for n in s:
#     if n == "0":
#         b.append(int(n))
#     else:
#         a.append(int(n))
# print(a + b)


# Блок 2
# Задача 0 - Общие элементы
# list1 = [1, 2, 3, 'p', -1, 20, 0.2, 'u']
# list2 = [11, 22, 33, 'p', -1, 20.2, 0.2]
# # a = set(list1) & set(list2)
# a = set(list1).intersection(set(list2))
# print(len(a))

# Задача 1 - Уникальные элементы
# n = input().split()
# n_set = set(n)
# print(n_set)
# print(len(n_set))

# Задача 2 - Площадь
# coords = [(100, 20), (20, 20)]
# a = coords[0]
# b = coords[1]
# d = (((a[0] - b[0]) ** 2) + (a[1] - b[1]) ** 2) ** (1/2)
# print(d)

# coords = [(100, 91, 87), (80, 35, 70)]
# a = coords[0]
# b = coords[1]
# d = (((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) + (a[2] - b[2]) ** 2) ** (1/2)
# print(d)
#
# coords = [(100, 91, 87), (80, 35, 70)]
# a = coords[0]
# b = coords[1]
# dist = 0
# for i in range(len(a)):
#     d = (a[i] - b[i]) ** 2
#     dist += d
# dist = dist ** (1/2)
# print(dist)

# Задача 3 - Количество повторений слов
# text = '''She sells sea shells on the sea shore \
# The shells that she sells are sea shells I'm sure \
# So if she sells sea shells on the sea shore \
# I'm sure that the shells are sea shore shells'''
# lst_text = text.split()
# lst_low_text = [word.lower() for word in lst_text]
# set_text = set(lst_low_text)
# # print(set_text)
# count = 0
# answer = {}
# for word in set_text:
#     count = lst_low_text.count(word)
#     answer[word] = count
# print(answer)

# второй способ
# text = '''She sells sea shells on the sea shore \
# The shells that she sells are sea shells I'm sure \
# So if she sells sea shells on the sea shore \
# I'm sure that the shells are sea shore shells'''
# lst_text = text.split()
# dic = {}
# for s in lst_text:
#     s_low = s.lower()
#     if s_low in dic:
#         dic[s_low] = dic[s_low] + 1
#     else:
#         dic[s_low] = 1
# print(dic)

# obj = {}
# obj["she"] = 1
# # { "she": 1 }
# print(obj)

# Задача 4 - Средний балл
# grades = {
#     '11A': [4, 5, 4, 5, 4, 5, 5, 5, 5, 5, 5, 3],
#     '11B': [3, 5, 3, 4, 4, 5, 4, 5, 4, 5, 5, 5],
#     '11C': [3, 3, 4, 4, 4, 5, 5, 5, 5, 5],
#     '11D': [4, 4, 4, 5, 4, 5, 5, 5, 4, 4, 4, 4],
#     '11E': [3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 4, 3]
# }
# number_of_classes = len(grades)
# average_all = 0
# for key in grades.keys():
#     lst = grades[key]
#     average = round(sum(lst) / len(lst), 2)
#     print(f"Средний балл {key} = {average}")
#     average_all = average_all + average
# average_all = round(average_all / number_of_classes, 2)
# print(f"Средний балл параллели = {average_all}")

# lst_11A = grades.get('11A')
# average_11A = round(sum(lst_11A) / len(lst_11A), 2)
# print(average_11A)

# Задача 5 - Проверка на новизну
# n = input().split()
# new = []
# for number in n:
#     if number in new:
#         print("y", end=" ")
#     else:
#         new += number
#         print("n", end=" ")

# второй способ
# numbers = input().split()
# new = set()
# for n in numbers:
#     if n in new:
#         print("y", end=" ")
#     else:
#         new.add(n)
#         print("n", end=" ")

# Задача 6 - Значения роста (Дополнительная!)
# students = {
#     'ИвановИИ': 170,
#     'ЖдановИЮ': 183,
#     'ИвановаАА': 168,
#     'МаркинаГА': 169,
#     'ПетроваАВ': 172,
#     'ПотаповЮР': 175,
#     'ЛарионовСБ': 177
# }
#
# name = input("Введите ФИО ")
# students[name] = int(input("Введите рост "))
# lst = list(students.values())
# new_list = list()
#
# for n in range(len(lst)):
#     maximum = max(lst)
#     new_list.append(maximum)
#     lst.remove(maximum)
# answer = new_list.index(students[name])
# count = new_list.count(students[name])
# print(new_list)
# print(f"Номер в шеренге = {answer + count}")

# второй способ
# students = {
#     'ИвановИИ': 170,
#     'ЖдановИЮ': 183,
#     'ИвановаАА': 168,
#     'МаркинаГА': 169,
#     'ПетроваАВ': 172,
#     'ПотаповЮР': 175,
#     'ЛарионовСБ': 177
# }
#
# name = input("Введите ФИО ")
# height = int(input("Введите рост "))
# students[name] = height
# order = 0
#
# for n in students.values():
#     if height <= n:
#         order += 1
#
# print(f"Номер в шеренге = {order}")

# с помощью sorted
# students = {
#     'ИвановИИ': 170,
#     'ЖдановИЮ': 183,
#     'ИвановаАА': 168,
#     'МаркинаГА': 169,
#     'ПетроваАВ': 172,
#     'ПотаповЮР': 175,
#     'ЛарионовСБ': 177
# }
# name = input("Введите ФИО ")
# students[name] = int(input("Введите рост "))
# s = sorted(students.values(), reverse=True)
# answer = s.index(students[name])
# count = s.count(students[name])
# print(answer + count)

# Блок 3

# Задача 0 - Отрабатываем умение писать генераторы
# 1. сгенерируйте список строк: user1, user2, user3 итд до user15
# res = [f'user{i}' for i in range(1, 16)]
# print(res)

# res = ['user' + str(i) for i in range(1, 16)]
# print(res)

# 2. сгенерируйте список из 10 случайных значений от -10 до 10
import random
