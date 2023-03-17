# name = input("Введите имя: ")
# print(f"{name} - великий программист !")

# word = "булочка с корицей"
# print(word[10], word[1], word[12], word[3], word[4], word[5], word[6], sep="")

# number = input("Введите число: ")
# if number[-1] == "3":
#     print("Число классное")
# else:
#     print("Число не очень")

# who = input("Кто проезжает ? ")
# if who == "король":
#     print("Первый мост")
# elif who == "рыцарь" or who =="фрейлина":
#     print("Второй мост")
# else:
#     print("Третий мост")

# jump = int(input("Сколько прыжков ? "))
# start = 5
# for i in range(jump):
#     print(f"Персонаж прыгнул на {start} метров")
#     start = start * 2

# name = "Alyosha"
# print(f"Добро пожаловать, {name}")

# def print_name(name):
#     print(f"Добро пожаловать, {name}")
# print_name("sfsf")
# print_name("fweafawef")
# print_name("dsfsf")

# def sum_ab(a, b):
#     print(a+b)
# sum_ab(5, 6)
# sum_ab(5, 8)
# sum_ab(5, 10)

# def equal_or_not(a, b):
#     if a == b:
#         print("equal")
#     else:
#         print("NOT")
# equal_or_not(66, 66)

# def calc(a, b):
#     print(a + b)
#     print(a - b)
#     print(a * b)
#     print(a / b)


# calc(5, 2)

# def calc(a, b, oper):
#     if oper == "+":
#         print(a + b)
#     if oper == "-":
#         print(a - b)
#     if oper == "*":
#         print(a * b)
#     if oper == "/":
#         print(a / b)
#
#
# calc(5, 6, "*")

# def print_name(name):
#     print(f"Добро пожаловать, {name}")
#
#
# print(print_name("Alyosha"))

# def buy_bread(money, price_of_bread):
#     return(money - price_of_bread)
#
#
# money = buy_bread(100, 65)
# print(money)

# def func(a):
#     return(a % 2)
#
#
# a = int(input("Введите число: "))
# print(f"Остаток от деления {a} на 2 = {func(a)}")

# def reverse(string):
#     new_string = ""
#     for each in string:
#         new_string = each + new_string
#     print(new_string)
#
#
# reverse("СТРОКА")

# def two_arg(string, symbol):
#     count = 0
#     for each in string:
#         if each == symbol:
#             count = count + 1
#     return count
#
#
# count2 = two_arg("яблоко", "я")
# print(count2)

# def max_length(strings_list):
#     max_len = ""
#     for each in strings_list:
#         if len(each) > len(max_len):
#             max_len = each
#     return max_len
#
#
# maxlen = func(["яблоко", "клубника", "ананас"])
# print(maxlen)

# def check_repeat(number_list):
#     i = 0
#     len_n = len(number_list)
#     for each in number_list:
#         for n in range(i + 1, len_n):
#             if each == number_list[n]:
#                 return(True)
#         i = i + 1
#     return (False)
#
#
# print(check_repeat([1, 2, 4, 4, 5, 6]))

# def median_num_list(num_list):
#     counter = 0
#     sum_num = 0
#     for each in num_list:
#         sum_num += each
#     sum_num = sum_num / len(num_list)
#     for each in num_list:
#         if each > sum_num:
#             counter += 1
#     return(counter)
#
#
# print(median_num_list([2, 3, 5, 4, 2]))
