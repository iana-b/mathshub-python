# Functions_seminar
# Блок 1
# Задачка 1
# def sum_even(numbers):
#     res = 0
#     for n in numbers:
#         if n % 2 == 0:
#             res += n
#     return res
#
#
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print("Сумма четных чисел в списке:", sum_even(my_list))

# Задачка 2
# def calculate_grade(grades):
#     average = round(sum(grades) / len(grades))
#     g = 2
#     if average >= 85:
#         g = 5
#     elif 70 <= average < 85:
#         g = 4
#     elif 50 <= average < 69:
#         g = 3
#     return average, g
#
#
# my_list = [85, 92, 78, 60, 45]
# print(calculate_grade(my_list))
# print(type(calculate_grade(my_list)))

# Задачка 3
# def find_max(numbers):
#     maximum = 0
#     for n in numbers:
#         if n > maximum:
#             maximum = n
#     return maximum
#
#
# my_list = [85, 92, 78, 60, 45]
# print(find_max(my_list))

# Задачка 4
# def delete_punctuation(string):
#     answer = string
#     for s in string:
#         if 32 < ord(s) < 64:
#             answer = answer.replace(s, '')
#     return answer
#
#
# my_string = "Jane\'s \"toyota\" in the street"
# print(delete_punctuation(my_string))

# 2 способ
# def delete_punctuation(string):
#     punctuanions = '?!.,:;-\"\''
#     answer = string
#     for s in string:
#         if s in punctuanions:
#             answer = answer.replace(s, '')
#     return answer
#
#
# my_string = "Jane\'s \"toyota\" in the street"
# print(delete_punctuation(my_string))

# print("Jane\'s \"toyota\" in the street")

# Задачка 5
# def find_factors(number: int):
#     numbers_list = []
#     for i in range(1, number + 1):
#         if number % i == 0:
#             numbers_list.append(i)
#     return numbers_list
#
#
# my_number = 24
# print(find_factors(my_number))

# Задача 6
# def is_palindrome(s: str) -> bool:
#     punctuanions = ' ?!.,:;-\"\''
#     string = s.lower()
#     for element in string:
#         if element in punctuanions:
#             string = string.replace(element, '')
#     reverse_string = string[::-1]
#     return reverse_string == string
#
#
# my_s = 'fghjkjhgf'
# print(is_palindrome(my_s))
# #
# tests = [
#     'A nut for a jar of tuna.',
#     'Borrow or rob?',
#     'Was it a car or a cat I saw?',
#     'Murder for a jar of red rum.'
# ]
#
#
# def test_palindrome(palindrom_func, tests_list):
#     for phrase in tests_list:
#         if not palindrom_func(phrase):
#             print(f"Failed on phrase {phrase}")
#         else:
#             print(f"Success")
#
#
# test_palindrome(is_palindrome, tests)


# list_a = [1, -2, -3, 4, -5, -6, 7]
#
# def only_positive(x):
#     if x > 0:
#         return x
#     else:
#         return 0
#
#
# print(list(map(lambda x: x if x > 0 else 0, list_a)))
#
# print(list(map(only_positive, list_a)))
#
# answer = []
# for x in list_a:
#     new_x = only_positive(x)
#     answer.append(new_x)
# print(answer)

# a = [1, 2, 3, 4, 5]
# b = [2, 1, 3, 6, 1]
# print(list(map(lambda x, y: x if x > y else y, a, b)))
#
#
# def maximum(x, y):
#     if x > y:
#         return x
#     else:
#         return y
#
#
# print(list(map(maximum, a, b)))
#
# lst = []
# for i in range(len(a)):
#     lst.append(maximum(a[i], b[i]))
# print(lst)

# рекурсия
# 5! = 1 * 2 * 3 * 4 * 5 = 120

# Задачка 7
# 1 способ
# def fibonacci(n):
#     n1 = 0
#     n2 = 1
#     res = 0
#     if n == 1:
#         res = n1
#     elif n == 2:
#         res = n2
#     for i in range(3, n + 1):
#         res = n1 + n2
#         n1 = n2
#         n2 = res
#     return res
#
#
# print(fibonacci(10))

# 2 способ с рекурсией
# def fibonacci(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     return fibonacci(n - 2) + fibonacci(n - 1)
#
#
# print(fibonacci(10))

# Задачка 8
# a = [1, 2, 3, 4, 5]
# b = [2, 1, 3, 6, 1]
#
#
# def summa_or_zero(list1, list2):
#     return list(map(lambda x, y: x + y if x != y else 0, list1, list2))
#
#
# print(summa_or_zero(a, b))

# Задачка 9
# def sort_list(list1):
#     return sorted(list1, key=lambda string: string[::-1])
#
#
# a = ['ab', 'sdsda', 'saae', 'wdsdq', 'ssdz']
# print(sort_list(a))

# Задачка 10
# def remove_from_list(list1, number):
#     return list(filter(lambda x: (x < number), list1))
#
#
# a = [1, 2, 3, 4, 5, 7, 8, 3]
# n = 5
# print(remove_from_list(a, n))

